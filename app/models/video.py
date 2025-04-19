from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Float, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.session import Base


class Video(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    url = Column(String)
    thumbnail_url = Column(String)
    category = Column(String)
    duration = Column(Integer)  # in seconds
    views = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # For vector representation
    vector_representation = Column(String)  # Will store serialized vector
    
    # Relationships
    user_interactions = relationship("UserInteraction", back_populates="video")


class UserInteraction(Base):
    __tablename__ = "user_interactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    video_id = Column(Integer, ForeignKey("videos.id"))
    watch_time = Column(Float)  # in seconds
    is_completed = Column(Boolean, default=False)
    rating = Column(Float)  # Optional rating from 1-5
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    video = relationship("Video", back_populates="user_interactions") 