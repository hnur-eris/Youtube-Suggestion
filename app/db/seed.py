from sqlalchemy.orm import Session
from app.models.user import User
from app.models.video import Video, UserInteraction
import hashlib


def seed_database(db: Session):
    # Create sample users with diverse interests
    users = [
        # Tech Enthusiasts
        User(
            email="tech_enthusiast@example.com",
            username="tech_lover",
            hashed_password=hashlib.sha256("password1".encode()).hexdigest(),
            is_active=True
        ),
        User(
            email="ai_researcher@example.com",
            username="ai_expert",
            hashed_password=hashlib.sha256("password2".encode()).hexdigest(),
            is_active=True
        ),
        
        # Data Professionals
        User(
            email="data_scientist@example.com",
            username="data_analyst",
            hashed_password=hashlib.sha256("password3".encode()).hexdigest(),
            is_active=True
        ),
        User(
            email="data_engineer@example.com",
            username="big_data",
            hashed_password=hashlib.sha256("password4".encode()).hexdigest(),
            is_active=True
        ),
        
        # Web Developers
        User(
            email="web_developer@example.com",
            username="web_dev",
            hashed_password=hashlib.sha256("password5".encode()).hexdigest(),
            is_active=True
        ),
        User(
            email="frontend_dev@example.com",
            username="ui_expert",
            hashed_password=hashlib.sha256("password6".encode()).hexdigest(),
            is_active=True
        ),
        
        # New Users (no watch history)
        User(
            email="new_user1@example.com",
            username="newbie1",
            hashed_password=hashlib.sha256("password7".encode()).hexdigest(),
            is_active=True
        ),
        User(
            email="new_user2@example.com",
            username="newbie2",
            hashed_password=hashlib.sha256("password8".encode()).hexdigest(),
            is_active=True
        )
    ]
    
    for user in users:
        db.add(user)
    db.commit()
    
    # Create sample videos
    videos = [
        # Machine Learning & AI
        Video(
            title="Introduction to Machine Learning",
            description="Learn ML basics and applications",
            url="https://example.com/videos/ml-intro",
            thumbnail_url="https://example.com/thumbnails/ml-intro.jpg",
            category="AI",
            duration=1800,
            views=1000
        ),
        Video(
            title="Deep Learning Fundamentals",
            description="Neural networks and deep learning",
            url="https://example.com/videos/deep-learning",
            thumbnail_url="https://example.com/thumbnails/deep-learning.jpg",
            category="AI",
            duration=5400,
            views=800
        ),
        Video(
            title="Machine Learning Projects",
            description="Practical ML project walkthroughs",
            url="https://example.com/videos/ml-projects",
            thumbnail_url="https://example.com/thumbnails/ml-projects.jpg",
            category="AI",
            duration=7200,
            views=2000
        ),
        
        # Programming
        Video(
            title="Python Programming Tutorial",
            description="Python programming guide",
            url="https://example.com/videos/python-tutorial",
            thumbnail_url="https://example.com/thumbnails/python-tutorial.jpg",
            category="Programming",
            duration=3600,
            views=2500
        ),
        Video(
            title="Advanced Python Techniques",
            description="Advanced Python concepts",
            url="https://example.com/videos/advanced-python",
            thumbnail_url="https://example.com/thumbnails/advanced-python.jpg",
            category="Programming",
            duration=4500,
            views=1200
        ),
        
        # Data Science
        Video(
            title="Data Science Projects",
            description="Data science using Python",
            url="https://example.com/videos/data-science",
            thumbnail_url="https://example.com/thumbnails/data-science.jpg",
            category="Data Science",
            duration=2700,
            views=1500
        ),
        Video(
            title="Big Data Processing",
            description="Big data processing guide",
            url="https://example.com/videos/big-data",
            thumbnail_url="https://example.com/thumbnails/big-data.jpg",
            category="Data Science",
            duration=4800,
            views=900
        ),
        
        # Web Development
        Video(
            title="Web Development Basics",
            description="HTML, CSS, JavaScript basics",
            url="https://example.com/videos/web-dev",
            thumbnail_url="https://example.com/thumbnails/web-dev.jpg",
            category="Web Development",
            duration=2400,
            views=3000
        ),
        Video(
            title="Modern Frontend Development",
            description="Advanced frontend techniques",
            url="https://example.com/videos/frontend",
            thumbnail_url="https://example.com/thumbnails/frontend.jpg",
            category="Web Development",
            duration=3600,
            views=1800
        )
    ]
    
    for video in videos:
        db.add(video)
    db.commit()
    
    # Create user interactions
    interactions = [
        # Tech Enthusiast's watch history
        UserInteraction(
            user_id=1, video_id=1, watch_time=1800,
            is_completed=True, rating=4.5
        ),
        UserInteraction(
            user_id=1, video_id=2, watch_time=4000,
            is_completed=False, rating=4.0
        ),
        UserInteraction(
            user_id=1, video_id=4, watch_time=3600,
            is_completed=True, rating=5.0
        ),
        
        # AI Researcher's watch history
        UserInteraction(
            user_id=2, video_id=1, watch_time=1800,
            is_completed=True, rating=4.8
        ),
        UserInteraction(
            user_id=2, video_id=2, watch_time=5400,
            is_completed=True, rating=4.9
        ),
        UserInteraction(
            user_id=2, video_id=3, watch_time=6000,
            is_completed=False, rating=4.5
        ),
        
        # Data Scientist's watch history
        UserInteraction(
            user_id=3, video_id=6, watch_time=2700,
            is_completed=True, rating=4.7
        ),
        UserInteraction(
            user_id=3, video_id=7, watch_time=4000,
            is_completed=False, rating=4.2
        ),
        UserInteraction(
            user_id=3, video_id=4, watch_time=3000,
            is_completed=False, rating=4.0
        ),
        
        # Data Engineer's watch history
        UserInteraction(
            user_id=4, video_id=6, watch_time=2700,
            is_completed=True, rating=4.6
        ),
        UserInteraction(
            user_id=4, video_id=7, watch_time=4800,
            is_completed=True, rating=4.8
        ),
        UserInteraction(
            user_id=4, video_id=5, watch_time=3500,
            is_completed=False, rating=4.3
        ),
        
        # Web Developer's watch history
        UserInteraction(
            user_id=5, video_id=8, watch_time=2400,
            is_completed=True, rating=4.7
        ),
        UserInteraction(
            user_id=5, video_id=9, watch_time=3000,
            is_completed=False, rating=4.0
        ),
        UserInteraction(
            user_id=5, video_id=4, watch_time=2500,
            is_completed=False, rating=4.2
        ),
        
        # Frontend Developer's watch history
        UserInteraction(
            user_id=6, video_id=8, watch_time=2400,
            is_completed=True, rating=4.9
        ),
        UserInteraction(
            user_id=6, video_id=9, watch_time=3600,
            is_completed=True, rating=4.8
        ),
        UserInteraction(
            user_id=6, video_id=5, watch_time=2000,
            is_completed=False, rating=4.1
        )
    ]
    
    for interaction in interactions:
        db.add(interaction)
    db.commit()
    
    return {"message": "Database seeded successfully"} 