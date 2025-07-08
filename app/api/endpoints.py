from fastapi import APIRouter, HTTPException
from app.agents.workflow import run_transformation_workflow  
from app.models.schemas import TransformRequest, TransformResponse
from app.utils.llm import UltraSafeClient

router = APIRouter()

@router.post(
    "/transform",
    response_model=TransformResponse,
    summary="Transform content to target style/format",
    description="Endpoint for content transformation using multi-agent system"
)
async def transform_content(request: TransformRequest):
    """
    Transform content through agent workflow:
    1. Analyze input style
    2. Plan transformation
    3. Execute conversion
    4. Quality control
    """
    try:
        # Execute agent workflow
        result = await run_transformation_workflow(
            content=request.content,
            target_style=request.target_style,
            target_format=request.target_format,
            complexity_level=request.complexity_level,
            feedback=request.feedback
        )
        return TransformResponse(
            transformed_content=result["transformed_content"],
            quality_metrics=result["quality_metrics"]
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Transformation failed: {str(e)}"
        )