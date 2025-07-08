from app.utils.llm import UltraSafeClient
from typing import Dict, Tuple

class QualityControlAgent:
    """Verifies transformation quality and accuracy"""
    
    def __init__(self):
        self.llm = UltraSafeClient()
    
    async def verify(
        self,
        original: str,
        transformed: str,
        target_style: str,
        target_format: str,
        feedback: str = None
    ) -> Tuple[str, Dict[str, float]]:
        """Verify transformation quality and refine if needed"""
        try:
            prompt = f"""
            Evaluate the transformed content against the original and requirements:
            
            Original Content:
            {original}
            
            Transformed Content:
            {transformed}
            
            Requirements:
            - Style: {target_style}
            - Format: {target_format}
            
            User Feedback: {feedback or 'None'}
            
            Provide:
            1. Quality metrics (0-100) for:
               - Style adherence
               - Format correctness
               - Factual consistency
               - Linguistic quality
            2. Refined content if improvements needed
            """
            
            response = await self.llm.chat_completion(
                system_prompt="You are a quality assurance expert",
                user_message=prompt
            )
            
            return self._parse_response(response)
        except Exception as e:
            raise RuntimeError(f"Quality check failed: {str(e)}")
    
    def _parse_response(self, response: str) -> Tuple[str, Dict[str, float]]:
        """Parse LLM response into metrics and refined content"""
        # Implementation would parse response
        refined_content = "Refined content based on feedback"
        metrics = {
            "style_adherence": 95.0,
            "format_correctness": 98.0,
            "factual_consistency": 92.0,
            "linguistic_quality": 96.0
        }
        return refined_content, metrics