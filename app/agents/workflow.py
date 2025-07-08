from langgraph.graph import StateGraph, END
from typing import TypedDict, Any
from .style_analysis import StyleAnalysisAgent
from .transformation_plan import TransformationPlanningAgent
from .content_converter import ContentConversionAgent
from .quality_control import QualityControlAgent

# Define workflow state
class TransformationState(TypedDict):
    content: str
    target_style: str
    target_format: str
    complexity_level: str
    feedback: str
    analysis: Dict[str, Any]
    plan: List[Dict[str, str]]
    transformed_content: str
    quality_metrics: Dict[str, float]

# Initialize agents
style_agent = StyleAnalysisAgent()
planning_agent = TransformationPlanningAgent()
conversion_agent = ContentConversionAgent()
qc_agent = QualityControlAgent()

# Create workflow graph
workflow = StateGraph(TransformationState)

# Define nodes
async def style_analysis(state: TransformationState) -> dict:
    """Execute style analysis"""
    state["analysis"] = await style_agent.analyze(state["content"])
    return state

async def plan_transformation(state: TransformationState) -> dict:
    """Create transformation plan"""
    state["plan"] = await planning_agent.create_plan(
        state["analysis"],
        state["target_style"],
        state["target_format"],
        state["complexity_level"]
    )
    return state

async def convert_content(state: TransformationState) -> dict:
    """Execute content transformation"""
    state["transformed_content"] = await conversion_agent.transform(
        state["content"],
        state["plan"],
        state["target_style"],
        state["target_format"]
    )
    return state

async def quality_control(state: TransformationState) -> dict:
    """Verify and refine transformation"""
    refined, metrics = await qc_agent.verify(
        state["content"],
        state["transformed_content"],
        state["target_style"],
        state["target_format"],
        state["feedback"]
    )
    state["transformed_content"] = refined
    state["quality_metrics"] = metrics
    return state

# Build workflow
workflow.add_node("analyze_style", style_analysis)
workflow.add_node("plan_transformation", plan_transformation)
workflow.add_node("convert_content", convert_content)
workflow.add_node("quality_check", quality_control)

# Define edges
workflow.set_entry_point("analyze_style")
workflow.add_edge("analyze_style", "plan_transformation")
workflow.add_edge("plan_transformation", "convert_content")
workflow.add_edge("convert_content", "quality_check")
workflow.add_edge("quality_check", END)

# Compile workflow
agent_workflow = workflow.compile()

# Public interface
async def run_transformation_workflow(
    content: str,
    target_style: str,
    target_format: str,
    complexity_level: str = "medium",
    feedback: str = None
) -> dict:
    """Execute full transformation workflow"""
    initial_state = TransformationState(
        content=content,
        target_style=target_style,
        target_format=target_format,
        complexity_level=complexity_level,
        feedback=feedback,
        analysis={},
        plan=[],
        transformed_content="",
        quality_metrics={}
    )
    result = await agent_workflow.run(initial_state)
    return {
        "transformed_content": result["transformed_content"],
        "quality_metrics": result["quality_metrics"]
    }