# Video Recommendation System

A content-based recommendation system for videos using FastAPI, PostgreSQL, and machine learning techniques.

## Features

- Content-based video recommendations using BERT and KMeans clustering
- User interaction tracking
- RESTful API endpoints
- PostgreSQL database with proper normalization
- Modern FastAPI backend

## Prerequisites

- Python 3.8+
- PostgreSQL
- pip

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd recommendation-system
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up PostgreSQL:
- Create a new database named `recommendation_db`
- Update the database credentials in `app/core/config.py` if needed

5. Run the application:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

- `GET /api/v1/videos/recommendations/{user_id}` - Get video recommendations for a user
- `POST /api/v1/videos/clusters/update` - Update video clusters based on content
- `POST /api/v1/videos/{video_id}/watch` - Record a video watch event

## Database Schema

The database is normalized to 3NF with the following tables:

- `users` - User information
- `videos` - Video content and metadata
- `user_interactions` - Tracks user video interactions
- `video_clusters` - Stores video cluster assignments
- `user_recommendations` - Stores user-specific recommendations

## Recommendation Algorithm

1. Text Processing:
   - Video titles and descriptions are processed using BERT
   - Text is converted to vector representations

2. Clustering:
   - Vectors are clustered using KMeans
   - Videos in the same cluster are considered similar

3. Recommendations:
   - Based on user's watched videos
   - Recommends videos from the same clusters
   - Fallback to popular videos for new users

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License. 