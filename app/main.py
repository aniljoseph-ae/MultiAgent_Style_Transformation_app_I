from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import router as api_router
from app.utils.config import get_settings

# Initialize application with metadata
app = FastAPI(
    title="Content Transformation Agent System",
    description="Multi-agent system for content transformation with RAG integration",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Apply CORS middleware for cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(api_router, prefix="/api/v1")

@app.on_event("startup")
async def startup_event():
    """Initialize application resources on startup"""
    from app.rag.knowledge_base import initialize_knowledge_base
    await initialize_knowledge_base()
    print("Knowledge base initialized")