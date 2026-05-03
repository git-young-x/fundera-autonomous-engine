import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from langgraph.graph import StateGraph, END
from state import AgentState
from agents import ingestion_agent, underwriting_agent, sentinel_agent, execution_agent


def build_graph() -> StateGraph:
    print("\n[GRAPH] Initializing Fundera Autonomous Engine...")
    print("[GRAPH] Registering agent nodes:")
    print("[GRAPH]   ingestion_agent -> underwriting_agent -> sentinel_agent -> execution_agent -> END")

    graph = StateGraph(AgentState)

    graph.add_node("ingestion_agent", ingestion_agent)
    graph.add_node("underwriting_agent", underwriting_agent)
    graph.add_node("sentinel_agent", sentinel_agent)
    graph.add_node("execution_agent", execution_agent)

    graph.set_entry_point("ingestion_agent")
    graph.add_edge("ingestion_agent", "underwriting_agent")
    graph.add_edge("underwriting_agent", "sentinel_agent")
    graph.add_edge("sentinel_agent", "execution_agent")
    graph.add_edge("execution_agent", END)

    print("[GRAPH] Graph compiled successfully.")
    return graph


def run_engine():
    print("\n" + "#" * 70)
    print("#       FUNDERA AUTONOMOUS ENGINE — STARTING RUN                 #")
    print("#" * 70)

    graph = build_graph()
    app = graph.compile()

    initial_state: AgentState = {
        "raw_data": {},
        "financial_metrics": {},
        "risk_profile": {},
        "audit_result": {},
        "action_card": {},
        "confidence_score": 0.0,
        "cfo_micro_query": "",
        "messages": [],
    }

    print("\n[GRAPH] Invoking graph with empty initial state...\n")
    final_state = app.invoke(initial_state)

    print("\n" + "#" * 70)
    print("#       FUNDERA AUTONOMOUS ENGINE — RUN COMPLETE                 #")
    print("#" * 70)

    print("\n[GRAPH] Final agent message log:")
    for msg in final_state["messages"]:
        print(f"  -> {msg}")

    print(f"\n[GRAPH] Final Risk Profile:")
    rp = final_state["risk_profile"]
    print(f"  • Risk Level:          {rp['risk_level']}")
    print(f"  • DSCR:                {rp['dscr']}")
    print(f"  • Monthly Payment:     ${rp['monthly_payment']:,.2f}")
    print(f"  • Cash Cushion/Month:  ${rp['monthly_cash_cushion_after_debt_service']:,.2f}")
    print(f"  • Max Loan Capacity:   ${rp['max_loan_capacity']:,.2f}")
    print(f"  • Rationale:           {rp['decision_rationale']}")

    ar = final_state["audit_result"]
    print(f"\n[GRAPH] Sentinel Audit Result:")
    print(f"  • Overall Audit:    {'PASSED' if ar.get('audit_passed') else 'FLAGGED'}")
    print(f"  • DSCR Check:       {'PASSED' if ar.get('dscr_check_passed') else 'FAILED'}")
    print(f"  • Timing Check:     {'PASSED' if ar.get('timing_check_passed') else 'NOTE'}")
    print(f"  • Note:             {ar.get('audit_note', 'N/A')}")

    print(f"\n[GRAPH] Transparent Action Card: generated and printed above by Execution Agent.")
    print("\n" + "#" * 70 + "\n")

    return final_state


if __name__ == "__main__":
    run_engine()
