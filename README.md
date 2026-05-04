# Fundera Autonomous Engine: Proactive Capital Routing

## Project Overview
The Fundera Autonomous Engine is a financial analysis prototype designed to identify and fulfill capital needs for Small and Medium Businesses (SMBs) through automated transaction analysis. 

## The Problem: Reactive Lending Models
Traditional SMB lending is **reactive**. Business owners typically apply for capital only after a cash-flow gap is identified, leading to high friction, urgent timelines, and a manual application process. This "apply-and-wait" model creates a disconnect between the timing of a capital need and the availability of funds.

## The Objective: Proactive Financial Advisory
The objective of this system is to move from a reactive model to a **proactive routing model**. By analyzing connected banking data (Plaid), the system identifies historical spending patterns and upcoming seasonal needs, automating the underwriting and audit process to present a pre-verified recommendation before the user initiates a request.

## System Architecture

The system utilizes an agentic orchestration framework to separate contextual pattern recognition from deterministic financial calculation.

<img width="3025" height="1712" alt="image" src="https://github.com/user-attachments/assets/cc60efeb-7491-499c-aacc-1d47293e5a24" />


### **Core Components:**

1. **Data Ingress (Plaid):**
   The engine parses 90-day transaction payloads, extracting revenue velocity (MRR), fixed-cost structures, and significant historical capital expenditures.

2. **Pattern Recognition (Agentic Reasoning):**
   Identifies contextual signals, such as recurring inventory purchases or seasonal growth cycles, to determine the *purpose* of the capital requirement.

3. **Underwriting Engine (Deterministic):**
   All financial math—including DSCR, amortization schedules, and loan capacity—is executed via **hard-coded Python logic**. This ensures 100% accuracy and prevents the "hallucinations" associated with large language models in numerical contexts.

4. **Governance Layer (Sentinel Audit):**
   An independent audit node that verifies the underwriting results against internal compliance thresholds (e.g., DSCR ≥ 1.25) and ensures the recommended timing aligns with the user’s historical data.

5. **Recommendation UI:**
   Synthesizes the audited data into a consultative dashboard, providing a primary recommendation with clear rationale and a side-by-side comparison of alternative capital products.

## Reliability & Compliance Design

* **Safety Gating:** The system is designed to provide a "Confidence Score" based on data density. 
* **Cash vs. Accrual Awareness:** Since banking data only reflects cash-basis accounting, the engine is programmed to flag pending obligations (Accounts Payable) as a required user-verification step.
* **Observability:** Every stage of the decision-making process is logged, creating a transparent audit trail for compliance and risk management.

## Setup & Local Execution
1. Clone the repository and initialize a virtual environment (`python -m venv venv`).
2. Install dependencies: `pip install -r requirements.txt`.
3. Add an `OPENAI_API_KEY` to a `.env` file for orchestration.
4. Run the dashboard: `streamlit run app.py`.
