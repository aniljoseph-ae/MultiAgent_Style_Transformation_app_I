Content Transformation Agent System
Overview
The Content Transformation Agent System is a Python-based application that dynamically transforms text content to match desired styles, formats, and complexity levels. It combines a multi-agent architecture with retrieval-augmented generation (RAG) to deliver high-quality, context-aware content transformations. Built with FastAPI for API functionality, LangGraph for agent coordination, and ChromaDB for knowledge retrieval, the system is designed for developers needing flexible content processing, such as automated style conversion or document reformatting.
Key Features

Agent-Based Workflow: Four agents handle distinct tasks—style analysis, transformation planning, content conversion, and quality assurance—for robust processing.
RAG Integration: Retrieves relevant style guides and examples from a ChromaDB vector store to inform transformations.
Quality Control: Assesses output for style, format, and linguistic accuracy, ensuring high-quality results.
Scalable Architecture: Supports local development and Docker-based deployment for production environments.
Modular Design: Easily extensible for adding new agents or integrating additional LLMs.

Technology Stack

Python: 3.10+
FastAPI: RESTful API framework (v0.109.0)
LangGraph: Agent orchestration (v0.0.39)
ChromaDB: Vector database for RAG (v0.4.24)
UltraSafe API: OpenAI-compatible language model for text generation
Docker: Containerization for deployment
Pytest: Testing framework for unit and integration tests

Prerequisites

Python 3.10 or higher
Conda (recommended for environment management)
Docker and Docker Compose (for containerized deployment)
UltraSafe API key (obtain from UltraSafe)

Installation and Local Setup

Clone the Repository:Navigate to your project directory and clone the repo:
git clone https://github.com/your-repo/content-transformer.git
cd content-transformer


Set Up Conda Environment:Create and activate a Conda environment to manage dependencies:
conda create -n win-gpu-env python=3.10
conda activate win-gpu-env


Install Dependencies:Use the provided requirements.txt to install dependencies:
fastapi==0.109.0
uvicorn[standard]==0.27.1
langgraph==0.0.39
langchain_core>=0.1.0,<0.2.0
langsmith>=0.0.70,<0.1.0
chromadb==0.4.24
openai==1.14.2
python-dotenv==1.0.1
pydantic-settings==2.2.1
pydantic==2.7.1
httpx==0.27.0
pytest==7.4.0
numpy<2.0.0

Install with:
pip install -r requirements.txt


Configure Environment Variables:Create a .env file in the project root with the following:
ULTRASAFE_API_KEY=your_api_key_here
ULTRASAFE_BASE_URL=https://api.us.inc/usf/v1/
CHROMA_DB_PATH=./chroma_db
OPENAI_TELEMETRY_DISABLE=1

Replace your_api_key_here with your UltraSafe API key.

Prepare Data and Storage:Ensure the data/ directory contains style_guides.json and transformation_examples.json (sample files provided in the repo). Create a directory for ChromaDB:
mkdir -p data chroma_db


Generate Project Structure:Run the project_setup.py script to create the directory structure and empty files:
python project_setup.py

Populate the files with the provided code (refer to the project repository or documentation).

Launch the API:Start the FastAPI server:
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

Access the Swagger UI at http://localhost:8000/docs to explore endpoints.


Docker Deployment

Verify Docker Installation:Ensure Docker and Docker Compose are installed:
docker --version
docker-compose --version


Set Up Environment:Use the same .env file as above.

Prepare Directories:Create data/ and chroma_db/ directories if not already present:
mkdir -p data chroma_db


Build and Run:Launch the application using Docker Compose:
docker-compose up --build

The API will be available at http://localhost:8000/docs.

Stop Containers:Shut down the containers when done:
docker-compose down



Testing
The project includes unit and integration tests in app/tests/. Run tests to verify functionality:
pytest app/tests/

Tests cover agent logic and API endpoints, ensuring the transformation workflow operates correctly.
Notes and Troubleshooting

UltraSafe API: The system uses the usf1-mini model for text generation. Embedding support is disabled due to endpoint limitations. Contact UltraSafe support for details on enabling embeddings if needed.
Dependency Compatibility: The pinned versions in requirements.txt (e.g., langgraph==0.0.39, langchain_core>=0.1.0,<0.2.0) resolve import errors. Recreate the Conda environment if issues persist:conda env remove -n win-gpu-env
conda create -n win-gpu-env python=3.10
pip install -r requirements.txt


Windows Permissions: Ensure write access to data/ and chroma_db/:chmod -R 777 data chroma_db


Debugging: If the API fails to start, temporarily comment out await initialize_knowledge_base() in app/main.py to isolate issues, then test the transformation endpoint.

Future Enhancements

Integrate UltraSafe's embedding endpoint for improved RAG performance.
Add more test cases for edge scenarios and mocked API responses.
Expand the data/ directory with additional style guides and examples.
Implement logging and monitoring for production-grade deployments.
