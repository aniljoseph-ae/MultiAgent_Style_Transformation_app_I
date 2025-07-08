import chromadb
import json
import os
from app.utils.llm import UltraSafeClient
from app.utils.config import get_settings

class KnowledgeBase:
    """Manages RAG knowledge base with ChromaDB"""
    
    def __init__(self):
        self.settings = get_settings()
        self.client = chromadb.PersistentClient(path=self.settings.chroma_db_path)
        self.collection = self._get_or_create_collection()
        self.llm = UltraSafeClient()
    
    def _get_or_create_collection(self):
        """Get existing collection or create new"""
        try:
            return self.client.get_collection("style_guides")
        except ValueError:
            return self.client.create_collection(
                "style_guides",
                metadata={"hnsw:space": "cosine"}
            )
    
    async def initialize(self):
        """Load and vectorize knowledge base documents"""
        # Load style guides
        with open("data/style_guides.json", "r") as f:
            style_guides = json.load(f)
        
        # Load transformation examples
        with open("data/transformation_examples.json", "r") as f:
            examples = json.load(f)
        
        # Combine documents
        documents = style_guides + examples
        embeddings = []
        metadatas = []
        ids = []
        
        # Process documents
        for idx, doc in enumerate(documents):
            # Generate embedding
            embedding = await self.llm.get_embeddings(doc["content"])
            embeddings.append(embedding)
            metadatas.append({
                "type": doc["type"],
                "style": doc["style"],
                "format": doc["format"]
            })
            ids.append(f"doc_{idx}")
        
        # Add to collection
        self.collection.add(
            embeddings=embeddings,
            metadatas=metadatas,
            documents=[d["content"] for d in documents],
            ids=ids
        )
        print(f"📚 Loaded {len(documents)} documents into knowledge base")

# Global initialization function
async def initialize_knowledge_base():
    """Initialize knowledge base on application startup"""
    kb = KnowledgeBase()
    await kb.initialize()