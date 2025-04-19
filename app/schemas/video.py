from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class VideoBase(BaseModel):
    title: str
    description: str
    url: str
    thumbnail_url: str
    category: str
    duration: int


class VideoCreate(VideoBase):
    pass


class VideoResponse(VideoBase):
    id: int
    views: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    recommendation_type: Optional[str] = None

    class Config:
        from_attributes = True


class RecommendationResponse(BaseModel):
    id: int
    title: str
    description: str
    category: str
    views: int
    duration: int
    thumbnail_url: str
    recommendation_type: str 