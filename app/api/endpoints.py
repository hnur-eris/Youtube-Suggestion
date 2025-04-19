from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List

from app.db.session import get_db
from app.services.recommendation import RecommendationService
from app.models.video import Video, UserInteraction
from app.models.user import User
from app.schemas.video import (
    VideoResponse, VideoCreate, RecommendationResponse
)
from app.db.seed import seed_database


router = APIRouter()


@router.get("/videos", response_model=List[VideoResponse])
async def get_videos(
    skip: int = 0,
    limit: int = 10,
    category: str = None,
    db: Session = Depends(get_db)
):
    """Get all videos with optional filtering"""
    query = db.query(Video)
    
    if category:
        query = query.filter(Video.category == category)
    
    videos = query.offset(skip).limit(limit).all()
    return videos


@router.get("/videos/popular", response_model=List[VideoResponse])
async def get_popular_videos(
    limit: int = 10,
    db: Session = Depends(get_db)
):
    """Get most popular videos"""
    videos = db.query(Video).order_by(Video.views.desc()).limit(limit).all()
    return videos


@router.post("/videos", response_model=VideoResponse)
async def create_video(
    video: VideoCreate,
    db: Session = Depends(get_db)
):
    """Create a new video"""
    db_video = Video(**video.dict())
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video


@router.get(
    "/videos/recommendations/{user_id}",
    response_model=List[RecommendationResponse]
)
async def get_recommendations(
    user_id: int,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    """Get video recommendations for a user"""
    service = RecommendationService(db)
    recommendations = service.get_recommendations(user_id, limit)
    return recommendations


@router.post("/videos/clusters/update")
async def update_clusters(db: Session = Depends(get_db)):
    """Update video clusters based on content"""
    service = RecommendationService(db)
    service.update_video_clusters()
    return {"message": "Video clusters updated successfully"}


@router.post("/videos/{video_id}/watch")
async def record_watch(
    video_id: int,
    user_id: int,
    watch_time: float,
    db: Session = Depends(get_db)
):
    """Record a video watch event"""
    video = db.query(Video).filter(Video.id == video_id).first()
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    
    # Update video views
    video.views += 1
    
    # Record user interaction
    interaction = UserInteraction(
        user_id=user_id,
        video_id=video_id,
        watch_time=watch_time,
        is_completed=watch_time >= video.duration * 0.9
    )
    db.add(interaction)
    db.commit()
    
    return {"message": "Watch recorded successfully"}


@router.get("/test-db")
async def test_db_connection(db: Session = Depends(get_db)):
    """Test database connection and verify data"""
    try:
        # Test raw SQL query
        result = db.execute(text("SELECT * FROM users"))
        users = result.fetchall()
        
        # Test ORM query
        orm_users = db.query(User).all()
        
        return {
            "raw_sql_users": [dict(row) for row in users],
            "orm_users": [
                {
                    "id": u.id,
                    "username": u.username,
                    "email": u.email
                } for u in orm_users
            ],
            "message": "Database connection successful"
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )


@router.post("/seed")
async def seed_db(db: Session = Depends(get_db)):
    """Seed the database with sample data"""
    try:
        # First, verify if tables exist
        db.execute(text("SELECT 1 FROM users LIMIT 1"))
        return seed_database(db)
    except Exception:
        # If tables don't exist, create them first
        from app.db.session import Base
        Base.metadata.create_all(bind=db.get_bind())
        return seed_database(db) 