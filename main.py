from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import router
from app.db.session import engine
from app.models import user, video, recommendation


# Create database tables
user.Base.metadata.create_all(bind=engine)
video.Base.metadata.create_all(bind=engine)
recommendation.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Recommendation System",
    description="A recommendation system for videos using content-based filtering and clustering",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "Welcome to the Recommendation System API"} 