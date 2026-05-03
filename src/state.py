from typing import Annotated
from typing_extensions import TypedDict
import operator


class AgentState(TypedDict):
    raw_data: dict
    financial_metrics: dict
    risk_profile: dict
    audit_result: dict
    action_card: dict
    confidence_score: float
    cfo_micro_query: str
    messages: Annotated[list, operator.add]
