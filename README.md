# MultiAgent_Style_Transformation_app_I

# Content Transformation Agent System

## Overview
Multi-agent system for transforming content between formats, styles, and complexity levels using:
- **FastAPI** for RESTful API
- **LangGraph** for agent coordination
- **ChromaDB** for RAG implementation
- **UltraSafe APIs** for LLM capabilities

## Features
- Four specialized agents for transformation workflow
- RAG-enhanced style guidance retrieval
- Quality control with metrics
- Scalable containerized architecture
- Comprehensive error handling

## Installation
```bash
# Clone repository
git clone https://github.com/your-repo/content-transformer.git
cd content-transformer

# Install dependencies
pip install -r requirements.txt

# Set environment variables
echo "ULTRASAFE_API_KEY=your_api_key" > .env
echo "ULTRASAFE_BASE_URL=https://api.ultrasafe.com/v1" >> .env
echo "CHROMA_DB_PATH=./chroma_db" >> .env

# Run application
uvicorn app.main:app --reload

# Run tests
pytest tests/
