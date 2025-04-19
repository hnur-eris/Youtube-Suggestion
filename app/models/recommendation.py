from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.session import Base


class VideoCluster(Base):
    __tablename__ = "video_clusters"

    id = Column(Integer, primary_key=True, index=True)
    cluster_id = Column(Integer, index=True)
    video_id = Column(Integer, ForeignKey("videos.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class UserRecommendation(Base):
    __tablename__ = "user_recommendations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    video_id = Column(Integer, ForeignKey("videos.id"))
    score = Column(Float)  # Recommendation score
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now()) 