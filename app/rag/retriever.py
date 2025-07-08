import chromadb
from app.utils.llm import UltraSafeClient
from app.utils.config import get_settings
from typing import List, Dict

async def retrieve_style_guidance(
    target_style: str, 
    target_format: str,
    top_k: int = 3
) -> str:
    """Retrieve relevant style guidance using vector search"""
    try:
        settings = get_settings()
        client = chromadb.PersistentClient(path=settings.chroma_db_path)
        collection = client.get_collection("style_guides")
        
        # Create query embedding
        query_text = f"Style: {target_style}, Format: {target_format}"
        llm = UltraSafeClient()
        query_embedding = await llm.get_embeddings(query_text)
        
        # Query vector store
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            where={"style": target_style, "format": target_format},
            include=["documents", "metadatas"]
        )
        
        # Format results as context
        context = "\n\n".join([
            f"Document {i+1}:\n{doc}"
            for i, doc in enumerate(results["documents"][0])
        ])
        
        return f"Relevant Style Guidance:\n{context}"
    except Exception as e:
        raise RuntimeError(f"Retrieval failed: {str(e)}")