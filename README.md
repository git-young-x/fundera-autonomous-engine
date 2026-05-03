# Fundera Autonomous Engine: The Invisible CFO

This prototype transforms the SMB lending experience from a reactive "apply-and-wait" process into a proactive, data-driven "Invisible CFO" service. 

## 🚀 The Product Vision
Most SMBs only apply for loans during a cash-flow crisis. The **Fundera Autonomous Engine** uses connected Plaid data to identify seasonal trends and pre-approve capital *before* the need arises. By moving the trigger from a user's panic to a background data sync, we increase conversion and position Fundera as a strategic financial partner.

## 🧠 Agentic Architecture
We use a multi-agent swarm (built on **LangGraph**) to handle the financial logic. This ensures that the "AI thinking" is observable, auditable, and grounded in deterministic math.

![Architecture Map](docs/architecture.png)

### **The Multi-Agent Workflow:**
1. **Ingestion Agent:** Parses 90-day transactions to identify MRR and seasonal spend patterns (e.g., Q4 inventory prep).
2. **Underwriting Agent:** Executes strict Python-based amortization and DSCR math. No LLM "hallucinated" numbers.
3. **Sentinel Agent (The Auditor):** The safety layer. It verifies that the loan matches the user’s historical growth cycle and passes all compliance thresholds.
4. **Execution Agent:** Synthesizes the data into a consultative "Action Card" for the UI, explaining the "Why" and the "Proof."

## 🛡️ The "Safe CFO" Logic
A major risk in Fintech AI is providing advice based on incomplete data. Since Plaid only sees cash-flow (not pending invoices), our engine:
* **Assigns a Confidence Score:** Based on data density.
* **Includes CFO Micro-Queries:** Instead of a hard "Take this loan," it asks, *"I see a cash dip—are you waiting on invoices, or do you need bridge capital?"*

## 🛠️ Setup
1. Clone the repo and activate your `venv`.
2. Install requirements: `pip install -r requirements.txt`
3. Add your `OPENAI_API_KEY` to a `.env` file.
4. Run the UI: `streamlit run app.py`
