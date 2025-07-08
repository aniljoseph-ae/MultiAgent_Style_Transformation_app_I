from app.utils.llm import UltraSafeClient
from typing import Dict, Any

class StyleAnalysisAgent:
    """Analyzes content style and characteristics"""
    
    def __init__(self):
        self.llm = UltraSafeClient()
        self.system_prompt = """
        You are a professional content analyst. Analyze the provided content and identify:
        - Tone (formal, casual, technical, etc.)
        - Complexity level (low, medium, high)
        - Format structure (paragraphs, bullet points, etc.)
        - Key linguistic features (vocabulary, sentence structure)
        - Potential biases or sensitive content
        """

    async def analyze(self, content: str) -> Dict[str, Any]:
        """Perform comprehensive style analysis"""
        try:
            response = await self.llm.chat_completion(
                system_prompt=self.system_prompt,
                user_message=f"Analyze this content:\n\n{content}"
            )
            
            # Parse structured response
            return {
                "tone": self._extract_value(response, "tone"),
                "complexity": self._extract_value(response, "complexity"),
                "format": self._extract_value(response, "format"),
                "linguistic_features": self._extract_features(response)
            }
        except Exception as e:
            raise RuntimeError(f"Style analysis failed: {str(e)}")

    def _extract_value(self, response: str, key: str) -> str:
        """Helper to extract values from LLM response"""
        # Implementation would parse response text
        return "formal"  # Simplified for example

    def _extract_features(self, response: str) -> Dict[str, str]:
        """Extract linguistic features"""
        # Implementation would parse response text
        return {"sentence_length": "mixed", "vocabulary": "advanced"}