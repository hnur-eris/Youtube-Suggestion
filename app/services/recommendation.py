from typing import List, Dict, Any
from sqlalchemy.orm import Session
from app.models.video import Video, UserInteraction
from app.models.recommendation import VideoCluster
from app.services.nlp import TextProcessor


class RecommendationService:
    def __init__(self, db: Session):
        self.db = db
        self.text_processor = TextProcessor()
        
    def update_video_clusters(self) -> None:
        """Update video clusters based on their content"""
        videos = self.db.query(Video).all()
        texts = [f"{video.title} {video.description}" for video in videos]
        
        self.text_processor.fit_clusters(texts)
        
        # Clear existing clusters
        self.db.query(VideoCluster).delete()
        
        # Create new clusters
        for video in videos:
            text = f"{video.title} {video.description}"
            cluster_id = self.text_processor.predict_cluster(text)
            
            cluster = VideoCluster(
                video_id=video.id,
                cluster_id=cluster_id
            )
            self.db.add(cluster)
        
        self.db.commit()
    
    def get_recommendations(
        self, 
        user_id: int, 
        limit: int = 10
    ) -> List[Dict[str, Any]]:
        """Get video recommendations for a user with detailed information"""
        # Get user's watched videos
        watched_videos = (
            self.db.query(UserInteraction.video_id)
            .filter(UserInteraction.user_id == user_id)
            .all()
        )
        watched_video_ids = [v[0] for v in watched_videos]
        
        if not watched_video_ids:
            # If user hasn't watched any videos, return popular videos
            videos = (
                self.db.query(Video)
                .order_by(Video.views.desc())
                .limit(limit)
                .all()
            )
            return [{
                "id": video.id,
                "title": video.title,
                "description": video.description,
                "category": video.category,
                "views": video.views,
                "duration": video.duration,
                "thumbnail_url": video.thumbnail_url,
                "recommendation_type": "popular"
            } for video in videos]
        
        # Get clusters of watched videos
        watched_clusters = (
            self.db.query(VideoCluster.cluster_id)
            .filter(VideoCluster.video_id.in_(watched_video_ids))
            .distinct()
            .all()
        )
        watched_cluster_ids = [c[0] for c in watched_clusters]
        
        # Get recommended videos from same clusters
        recommended_videos = (
            self.db.query(Video)
            .join(VideoCluster, Video.id == VideoCluster.video_id)
            .filter(
                VideoCluster.cluster_id.in_(watched_cluster_ids),
                ~Video.id.in_(watched_video_ids)
            )
            .order_by(Video.views.desc())
            .limit(limit)
            .all()
        )
        
        return [{
            "id": video.id,
            "title": video.title,
            "description": video.description,
            "category": video.category,
            "views": video.views,
            "duration": video.duration,
            "thumbnail_url": video.thumbnail_url,
            "recommendation_type": "similar_content"
        } for video in recommended_videos] 