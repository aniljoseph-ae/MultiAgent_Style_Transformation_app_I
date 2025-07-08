from app.utils.llm import UltraSafeClient
from typing import List, Dict

class ContentConversionAgent:
    """Executes content transformations based on plan"""
    
    def __init__(self):
        self.llm = UltraSafeClient()
    
    async def transform(
        self,
        content: str,
        plan: List[Dict[str, str]],
        target_style: str,
        target_format: str
    ) -> str:
        """Execute transformation using step-by-step plan"""
        try:
            prompt = f"""
            Transform the following content according to the provided plan:
            
            Content:
            {content}
            
            Transformation Plan:
            {plan}
            
            Target Style: {target_style}
            Target Format: {target_format}
            
            Output only the transformed content with no additional commentary.
            """
            
            response = await self.llm.chat_completion(
                system_prompt="You are a content transformation specialist",
                user_message=prompt
            )
            
            return response.strip()
        except Exception as e:
            raise RuntimeError(f"Conversion failed: {str(e)}")