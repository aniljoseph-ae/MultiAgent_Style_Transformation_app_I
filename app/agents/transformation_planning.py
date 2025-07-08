from app.utils.llm import UltraSafeClient
from app.rag.retriever import retrieve_style_guidance
from typing import List, Dict

class TransformationPlanningAgent:
    """Creates transformation plans using RAG guidance"""
    
    def __init__(self):
        self.llm = UltraSafeClient()
    
    async def create_plan(
        self,
        analysis: Dict[str, Any],
        target_style: str,
        target_format: str,
        complexity_level: str
    ) -> List[Dict[str, str]]:
        """Generate transformation plan with RAG guidance"""
        try:
            # Retrieve relevant style guidance
            rag_context = await retrieve_style_guidance(
                target_style, 
                target_format
            )
            
            prompt = f"""
            Based on the style analysis and target requirements, create a step-by-step 
            transformation plan. Use the following RAG context for guidance:
            
            RAG Context:
            {rag_context}
            
            Style Analysis:
            {analysis}
            
            Target:
            - Style: {target_style}
            - Format: {target_format}
            - Complexity: {complexity_level}
            
            Plan should include:
            1. Structural changes
            2. Tone adjustments
            3. Complexity modifications
            4. Format conversion steps
            """
            
            response = await self.llm.chat_completion(
                system_prompt="You are a transformation planning expert",
                user_message=prompt
            )
            
            return self._parse_plan(response)
        except Exception as e:
            raise RuntimeError(f"Planning failed: {str(e)}")
    
    def _parse_plan(self, response: str) -> List[Dict[str, str]]:
        """Parse LLM response into structured plan"""
        # Implementation would parse response
        return [
            {"step": "Convert tone", "action": "formalize language"},
            {"step": "Adjust complexity", "action": "simplify vocabulary"}
        ]