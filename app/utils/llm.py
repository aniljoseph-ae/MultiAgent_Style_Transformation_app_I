from openai import AsyncOpenAI
from app.utils.config import get_settings
from typing import List, Dict, Any

class UltraSafeClient:
    """Client for UltraSafe API with retry logic"""
    
    def __init__(self):
        settings = get_settings()
        self.client = AsyncOpenAI(
            api_key=settings.ultrasafe_api_key,
            base_url=settings.ultrasafe_base_url,
            timeout=30.0
        )
    
    async def chat_completion(
        self,
        system_prompt: str,
        user_message: str,
        model: str = "usf1-mini",  # Updated to usf1-mini
        temperature: float = 0.3
    ) -> str:
        """Get chat completion with structured output"""
        try:
            response = await self.client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ],
                temperature=temperature,
                max_tokens=1000
            )
            return response.choices[0].message.content
        except Exception as e:
            raise ConnectionError(f"Chat completion failed: {str(e)}")
    
    async def get_embeddings(
        self, 
        text: str, 
        model: str = "text-embedding-3-large"  # IMP: Placeholder; update if UltraSafe supports embeddings
    ) -> List[float]:
        """Get embeddings for text"""
        try:
            response = await self.client.embeddings.create(
                input=[text],
                model=model
            )
            return response.data[0].embedding
        except Exception as e:
            raise ConnectionError(f"Embedding failed: {str(e)}")