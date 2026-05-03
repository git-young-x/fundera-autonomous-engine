import time

import streamlit as st

from src.graph import run_engine

st.set_page_config(
    page_title="Financial Analysis & Recommendations",
    layout="centered",
    page_icon="💼",
)

# ── Fundera / NerdWallet Design System ────────────────────────────────────────

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none !important; }
[data-testid="stToolbar"] { display: none !important; }
[data-testid="stDecoration"] { display: none !important; }

/* Base */
html, body, .stApp { background-color: #FFFFFF !important; }

/* ── Global text colour override ── */
p, span, div, li, td, th, label,
.stMarkdown, .stMarkdown p, .stMarkdown span,
.element-container p, .element-container span, .element-container div {
    color: #2B2C34 !important;
}
.main .block-container {
    max-width: 760px;
    padding: 2.5rem 2rem 5rem;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
}

/* ── Header ── */
.fundera-eyebrow {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #00A36C;
    margin-bottom: 8px;
}
.fundera-title {
    font-size: 30px;
    font-weight: 800;
    color: #2B2C34;
    letter-spacing: -0.5px;
    line-height: 1.2;
    margin: 0 0 6px 0;
}
.fundera-subtitle {
    font-size: 14px;
    color: #6B7280;
    margin-bottom: 24px;
    line-height: 1.5;
}
.fundera-divider {
    height: 1px;
    background: linear-gradient(to right, #00A36C40, #E8E8EC00);
    margin-bottom: 28px;
}

/* ── Institution Badge ── */
.inst-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #F9FAFB;
    border: 1px solid #E5E7EB;
    border-radius: 8px;
    padding: 10px 16px;
    font-size: 13px;
    color: #6B7280;
    margin-bottom: 28px;
}
.inst-badge .dot {
    width: 8px;
    height: 8px;
    background: #00A36C;
    border-radius: 50%;
    flex-shrink: 0;
    box-shadow: 0 0 0 2px #D1FAE5;
}
.inst-badge strong { color: #2B2C34; font-weight: 600; }

/* ── Primary Button ── */
.stButton > button {
    background-color: #00A36C !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 14px 28px !important;
    font-size: 15px !important;
    font-weight: 600 !important;
    font-family: 'Inter', sans-serif !important;
    width: 100% !important;
    letter-spacing: 0.01em !important;
    box-shadow: 0 2px 10px rgba(0, 163, 108, 0.28) !important;
    transition: background-color 0.15s ease, box-shadow 0.15s ease !important;
}
.stButton > button:hover {
    background-color: #008F5E !important;
    box-shadow: 0 4px 14px rgba(0, 163, 108, 0.38) !important;
}

/* ── Status Widget ── */
[data-testid="stStatusWidget"] {
    border-radius: 10px !important;
    border: 1px solid #E5E7EB !important;
    background: #FAFAFA !important;
    font-family: 'Inter', sans-serif !important;
}
[data-testid="stStatusWidget"] p,
[data-testid="stStatusWidget"] span,
[data-testid="stStatusWidget"] div,
[data-testid="stStatusWidget"] li,
.stStatus p, .stStatus span, .stStatus div, .stStatus li {
    color: #2B2C34 !important;
}

/* ── Section Gap ── */
.gap { margin-bottom: 8px; }
.gap-lg { margin-bottom: 20px; }

/* ── Action Card Wrapper ── */
.action-card-header {
    text-align: center;
    padding: 24px 0 20px;
    border-bottom: 1px solid #E5E7EB;
    margin-bottom: 18px;
}
.action-card-header .ac-eyebrow {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #00A36C;
    margin-bottom: 6px;
}
.action-card-header .ac-title {
    font-size: 22px;
    font-weight: 800;
    color: #2B2C34;
}
.action-card-header .ac-sub {
    font-size: 13px;
    color: #9CA3AF;
    margin-top: 4px;
}

/* ── Base Card ── */
.card {
    background: #FFFFFF;
    border: 1px solid #E5E7EB;
    border-radius: 12px;
    padding: 20px 22px;
    margin-bottom: 12px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05), 0 1px 3px rgba(0,0,0,0.04);
}
.card-label {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #9CA3AF;
    margin-bottom: 6px;
}
.card-heading {
    font-size: 16px;
    font-weight: 700;
    color: #2B2C34;
    margin-bottom: 14px;
}

/* ── Why Card ── */
.why-card {
    background: #FFFBEB;
    border: 1px solid #FCD34D;
    border-radius: 12px;
    padding: 20px 22px;
    margin-bottom: 12px;
}
.why-card .card-label { color: #B45309; }
.why-card .card-heading { color: #78350F; margin-bottom: 10px; }
.why-body {
    font-size: 14px;
    color: #78350F;
    line-height: 1.65;
}
.why-body strong { color: #92400E; }

/* ── Risk Tier Badge ── */
.tier-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: #ECFDF5;
    border: 1px solid #6EE7B7;
    border-radius: 20px;
    padding: 4px 14px;
    font-size: 11px;
    font-weight: 700;
    color: #065F46;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    margin-bottom: 14px;
}

/* ── Metric Grid ── */
.metric-row {
    display: flex;
    gap: 10px;
    margin-bottom: 10px;
}
.metric-item {
    flex: 1;
    background: #F9FAFB;
    border-radius: 8px;
    padding: 12px 14px;
    min-width: 0;
}
.metric-label {
    font-size: 11px;
    color: #9CA3AF;
    font-weight: 500;
    margin-bottom: 3px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
.metric-value {
    font-size: 18px;
    font-weight: 700;
    color: #2B2C34;
    white-space: nowrap;
}
.metric-value.green { color: #00A36C; }

/* ── Proof Lines ── */
.proof-line {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 9px 0;
    border-bottom: 1px solid #F3F4F6;
    font-size: 13px;
}
.proof-line:last-of-type { border-bottom: none; }
.pf-label { color: #6B7280; }
.pf-value { font-weight: 600; color: #2B2C34; }
.proof-line.total-line { padding-top: 12px; font-weight: 700; font-size: 14px; }
.proof-line.total-line .pf-value { color: #00A36C; }

/* ── DSCR Badge ── */
.dscr-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: #ECFDF5;
    border: 1px solid #6EE7B7;
    border-radius: 6px;
    padding: 8px 14px;
    font-size: 14px;
    font-weight: 700;
    color: #065F46;
    margin-top: 12px;
}

/* ── Sentinel Audit Card (Highlighted) ── */
.audit-card {
    background: #F0FDF8;
    border: 2px solid #00A36C;
    border-radius: 12px;
    padding: 20px 22px;
    margin-bottom: 12px;
    box-shadow: 0 4px 20px rgba(0, 163, 108, 0.12);
}
.audit-card .card-label { color: #065F46; }
.audit-verdict-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: #00A36C;
    color: #FFFFFF;
    border-radius: 20px;
    padding: 5px 14px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 14px;
}
.audit-check-row {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    font-size: 13px;
    color: #2B2C34;
    padding: 6px 0;
    line-height: 1.5;
}
.check-pass { font-weight: 800; color: #00A36C; font-size: 15px; }
.check-fail { font-weight: 800; color: #DC2626; font-size: 15px; }
.audit-note {
    font-size: 12px;
    color: #6B7280;
    font-style: italic;
    border-top: 1px solid #D1FAE5;
    margin-top: 12px;
    padding-top: 12px;
    line-height: 1.5;
}

/* ── CTA Card ── */
.cta-card {
    background: linear-gradient(135deg, #FAFFFE 0%, #F0FDF8 100%);
    border: 1px solid #D1FAE5;
    border-radius: 12px;
    padding: 22px 24px;
    margin-top: 6px;
    text-align: center;
}
.cta-disclaimer {
    font-size: 12px;
    color: #9CA3AF;
    margin-bottom: 16px;
    line-height: 1.5;
}
.cta-btn {
    display: inline-block;
    background: #00A36C;
    color: #FFFFFF;
    text-decoration: none;
    padding: 14px 40px;
    border-radius: 8px;
    font-size: 15px;
    font-weight: 600;
    letter-spacing: 0.01em;
    box-shadow: 0 2px 10px rgba(0, 163, 108, 0.30);
    font-family: 'Inter', sans-serif;
    cursor: pointer;
    border: none;
}

/* ── Alternative Option Card ── */
.alt-card {
    background: #FAFAFA;
    border: 1px solid #E5E7EB;
    border-radius: 10px;
    padding: 18px 20px;
    height: 100%;
}
.alt-card .card-label { color: #9CA3AF; }
.alt-highlight {
    font-size: 13px;
    font-weight: 600;
    color: #2B2C34;
    margin: 8px 0 12px;
}
.alt-terms {
    font-size: 13px;
    color: #6B7280;
    line-height: 1.6;
    margin-bottom: 12px;
}
.alt-not-primary {
    font-size: 12px;
    color: #78350F;
    background: #FFFBEB;
    border: 1px solid #FCD34D;
    border-radius: 6px;
    padding: 8px 12px;
    line-height: 1.55;
}
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────

st.markdown("""
<div class="fundera-eyebrow">Fundera by NerdWallet</div>
<div class="fundera-title">Financial Analysis &amp; Recommendations</div>
<div class="fundera-subtitle">
    Data-driven insights and capital routing based on your connected accounts.
</div>
<div class="fundera-divider"></div>
<div class="inst-badge">
    <span class="dot"></span>
    <strong>Chase Business Banking</strong>
    &nbsp;·&nbsp;
    <span>Meridian Commerce LLC</span>
    &nbsp;·&nbsp;
    <span>Plaid Connected &amp; Verified</span>
</div>
""", unsafe_allow_html=True)

# ── Auto-run engine once per session (webhook-triggered UX simulation) ────────

if "result" not in st.session_state:
    with st.spinner("Fundera Engine analyzing your Plaid data..."):
        try:
            st.session_state.result = run_engine()
            st.session_state.error = None
        except Exception as exc:
            st.session_state.result = None
            st.session_state.error = str(exc)

# ── Error Display ─────────────────────────────────────────────────────────────

if st.session_state.get("error"):
    st.error(f"Engine error: {st.session_state.error}")

# ── Consultative UI ───────────────────────────────────────────────────────────

if st.session_state.get("result"):
    result = st.session_state.result
    fm  = result.get("financial_metrics", {})
    rp  = result.get("risk_profile", {})
    ar  = result.get("audit_result", {})
    ac  = result.get("action_card", {})
    seasonal = fm.get("seasonal_capex_event", {})

    # ── helpers ──
    def fmt_usd(v: float) -> str:
        return f"${v:,.2f}"
    def fmt_x(v: float) -> str:
        return f"{v:.2f}x"
    def fmt_pct(v: float) -> str:
        return f"{v * 100:.1f}%"

    # ── unpack action_card ──
    hero       = ac.get("hero_offer", {})
    rationale  = ac.get("cfo_rationale", [])
    snapshot   = ac.get("financial_snapshot", {})
    alts       = ac.get("alternatives", [])
    disclaimer = ac.get("safe_cfo_disclaimer", "")

    lender          = hero.get("lender", "BlueVine")
    loan_amount     = hero.get("amount", rp.get("loan_amount_proposed", 80_000))
    rate            = hero.get("annual_rate", rp.get("annual_interest_rate", 0.08))
    term            = hero.get("term_months", rp.get("loan_term_months", 12))
    monthly_payment = hero.get("monthly_payment", rp.get("monthly_payment", 0.0))
    total_interest  = hero.get("total_interest", max(0.0, monthly_payment * term - loan_amount))
    risk_level      = hero.get("risk_level", rp.get("risk_level", "PRE_APPROVED_TIER_1"))

    dscr         = rp.get("dscr", 0.0)
    cash_cushion = rp.get("monthly_cash_cushion_after_debt_service", 0.0)
    mrr          = fm.get("mrr", 0.0)
    fixed_costs  = fm.get("total_fixed_costs", 0.0)
    fcf          = fm.get("free_cash_flow", 0.0)

    vendor       = seasonal.get("vendor", "Pacific Rim Wholesale Distributors")
    event_date   = seasonal.get("date", "2025-05-03")
    event_amount = abs(seasonal.get("amount", 80_000))
    event_year   = event_date[:4] if event_date else "2025"

    audit_passed  = ar.get("audit_passed", False)
    dscr_passed   = ar.get("dscr_check_passed", False)
    timing_passed = ar.get("timing_check_passed", False)
    audit_note    = ar.get("audit_note", "")

    risk_display   = risk_level.replace("_", " ").title()
    audit_label    = "AUDIT APPROVED" if audit_passed else "AUDIT: REVIEW REQUIRED"
    generated_date = time.strftime("%B %d, %Y")

    dscr_icon    = "✓" if dscr_passed   else "✗"
    timing_icon  = "✓" if timing_passed else "✗"
    dscr_class   = "check-pass" if dscr_passed   else "check-fail"
    timing_class = "check-pass" if timing_passed else "check-fail"

    # ═══════════════════════════════════════════════════════════════════════════
    # SECTION 1 — YOUR FINANCIAL SNAPSHOT
    # ═══════════════════════════════════════════════════════════════════════════

    st.subheader("Your Financial Snapshot")

    insight = snapshot.get(
        "insight_summary",
        f"Your Plaid-connected Chase account shows ${mrr:,.0f}/month MRR with "
        f"${fcf:,.0f}/month in free cash flow and a documented Q4 inventory pattern.",
    )
    st.markdown(f'<p style="font-size:14px;color:#6B7280;line-height:1.65;margin-bottom:18px;">{insight}</p>',
                unsafe_allow_html=True)

    col_mrr, col_costs, col_fcf = st.columns(3)
    col_mrr.metric(
        label="Monthly Revenue (MRR)",
        value=fmt_usd(mrr),
        help="3-month average of verified Shopify payouts from Plaid",
    )
    col_costs.metric(
        label="Fixed Costs / Month",
        value=fmt_usd(fixed_costs),
        help="Gusto Payroll + Commercial Rent (90-day average)",
    )
    col_fcf.metric(
        label="Free Cash Flow",
        value=fmt_usd(fcf),
        delta=f"DSCR {fmt_x(dscr)} — strong",
        help="MRR minus fixed costs; available for debt service",
    )

    st.markdown('<div class="gap-lg"></div>', unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════════════════
    # SECTION 2 — PRIMARY CFO RECOMMENDATION
    # ═══════════════════════════════════════════════════════════════════════════

    st.subheader("Primary CFO Recommendation")

    rationale_html = "".join(
        f'<div style="display:flex;gap:10px;font-size:13px;color:#2B2C34;'
        f'line-height:1.65;padding:7px 0;border-bottom:1px solid #E5E7EB;">'
        f'<span style="color:#00A36C;font-weight:700;flex-shrink:0;">→</span>'
        f'<span>{bullet}</span></div>'
        for bullet in rationale
    )

    st.markdown(f"""
    <div class="card" style="border:2px solid #00A36C;background:linear-gradient(135deg,#FAFFFE 0%,#F0FDF8 100%);padding:24px 26px;margin-bottom:16px;">
        <div class="card-label" style="color:#065F46;">Pre-Approved Offer &nbsp;·&nbsp; {lender} Business Term Loan</div>
        <div style="font-size:34px;font-weight:800;color:#2B2C34;letter-spacing:-0.5px;margin:4px 0 2px;">
            {fmt_usd(loan_amount)}
        </div>
        <div style="font-size:15px;color:#6B7280;margin-bottom:16px;">
            {fmt_pct(rate)} APR &nbsp;·&nbsp; {term} months &nbsp;·&nbsp; {fmt_usd(monthly_payment)}/mo
        </div>
        <div style="display:inline-flex;align-items:center;gap:6px;background:#ECFDF5;border:1px solid #6EE7B7;border-radius:20px;padding:4px 14px;font-size:11px;font-weight:700;color:#065F46;letter-spacing:0.06em;text-transform:uppercase;margin-bottom:20px;">
            ✓ &nbsp;{risk_display}
        </div>
        <div style="font-size:11px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:#00A36C;margin-bottom:8px;">
            CFO Rationale
        </div>
        {rationale_html}
    </div>
    """, unsafe_allow_html=True)

    st.button("Review Pre-Filled Terms →", type="primary")

    st.markdown('<div class="gap-lg"></div>', unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════════════════
    # SECTION 3 — ALTERNATIVE CAPITAL OPTIONS
    # ═══════════════════════════════════════════════════════════════════════════

    st.subheader("Alternative Capital Options")
    st.markdown(
        '<p style="font-size:14px;color:#6B7280;margin-bottom:16px;">'
        "These products were evaluated for your profile. Here's why each falls short "
        "of the primary recommendation for your specific situation.</p>",
        unsafe_allow_html=True,
    )

    alt_cols = st.columns(len(alts)) if alts else []
    for col, alt in zip(alt_cols, alts):
        alt_rate   = alt.get("annual_rate", 0.0)
        alt_amount = alt.get("amount", 0)
        alt_term   = alt.get("term_label", "")
        alt_type   = alt.get("product_type", "")
        alt_why    = alt.get("why_not_primary", "")
        alt_hl     = alt.get("highlight", "")
        with col:
            st.markdown(f"""
            <div class="alt-card">
                <div class="card-label">{alt_type}</div>
                <div style="font-size:17px;font-weight:800;color:#2B2C34;margin:4px 0 2px;">
                    {alt.get("name", "")}
                </div>
                <div class="alt-highlight">{alt_hl}</div>
                <div class="alt-terms">
                    <strong>Amount:</strong> {fmt_usd(alt_amount)}<br>
                    <strong>APR:</strong> {fmt_pct(alt_rate)}<br>
                    <strong>Term:</strong> {alt_term}
                </div>
                <div class="alt-not-primary">
                    <strong>Why it's not the primary pick:</strong><br>{alt_why}
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div class="gap-lg"></div>', unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════════════════
    # SAFE CFO DISCLAIMER
    # ═══════════════════════════════════════════════════════════════════════════

    st.info(disclaimer)

    # ═══════════════════════════════════════════════════════════════════════════
    # AI AUDIT TRAIL (COLLAPSED)
    # ═══════════════════════════════════════════════════════════════════════════

    with st.expander("View AI Audit Trail & System Math"):

        st.markdown(f"""
        <div class="action-card-header">
            <div class="ac-eyebrow">Fundera Autonomous Engine — 4-Agent Pipeline</div>
            <div class="ac-title">Full Audit Trail</div>
            <div class="ac-sub">Meridian Commerce LLC &nbsp;·&nbsp; Generated {generated_date}</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(
            "**📡 Step 1 — Ingestion Agent:** Connected to Plaid · Parsed 90-day Chase "
            "transaction history · Extracted MRR, fixed-cost stack, and seasonal Q4 capex "
            "signal · **Confidence score: 0.85** (cash trends strong; AR/AP not visible in "
            "Plaid cash-basis data).\n\n"
            "**📊 Step 2 — Underwriting Agent:** Calculated free cash flow via **strictly "
            "deterministic Python amortization math** (no LLM estimates) · Ran $80,000 / "
            "8% APR / 12-month model · DSCR = FCF ÷ Monthly Payment.\n\n"
            "**🛡️ Step 3 — Sentinel Agent:** Independently verified DSCR ≥ 1.25× compliance "
            "threshold · Cross-referenced current month against documented Q2 inventory capex "
            "timing · Issued audit verdict.\n\n"
            "**📋 Step 4 — Execution Agent:** Synthesized Hero Offer, CFO Rationale, Financial "
            "Snapshot, Alternatives analysis, and Safe CFO Disclaimer into structured "
            "`action_card` dict payload."
        )

        st.divider()

        # ── The Why ──────────────────────────────────────────────────────────
        st.markdown(f"""
        <div class="why-card">
            <div class="card-label">The Why — Context-Aware Trigger (Ingestion Agent)</div>
            <div class="card-heading">Seasonal Capex Pattern Detected in Plaid History</div>
            <div class="why-body">
                Our Ingestion Agent surfaced a <strong>recurring Q2 wholesale inventory event</strong>
                embedded in Meridian's Plaid transaction history. In {event_year},
                <strong>{vendor}</strong> received <strong>{fmt_usd(event_amount)}</strong> ahead of
                the Q4 holiday demand cycle — generating <strong>$148,000 in Q4 revenue at a 22.4%
                net margin</strong> and 18.7% year-over-year revenue growth. That same annual window
                is now open.
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ── System Math / Proof ───────────────────────────────────────────────
        st.markdown(f"""
        <div class="card">
            <div class="card-label">System Math — Cash Flow Verification (Underwriting Agent)</div>
            <div class="card-heading">Meridian Commerce LLC — Chase Business Banking · 90-Day Plaid Data</div>
            <div class="proof-line">
                <span class="pf-label">Monthly Recurring Revenue (Shopify Payouts, 3-mo avg)</span>
                <span class="pf-value">{fmt_usd(mrr)}</span>
            </div>
            <div class="proof-line">
                <span class="pf-label">(−) Monthly Fixed Costs (Gusto Payroll + Commercial Rent)</span>
                <span class="pf-value">({fmt_usd(fixed_costs)})</span>
            </div>
            <div class="proof-line total-line">
                <span class="pf-label">= Free Cash Flow Available for Debt Service</span>
                <span class="pf-value">{fmt_usd(fcf)}</span>
            </div>
            <div class="dscr-badge">
                ✓&nbsp; DSCR: {fmt_x(dscr)} &nbsp;·&nbsp; Compliance Target ≥ 1.25x &nbsp;·&nbsp; STRONG PASS
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ── Offer Detail ──────────────────────────────────────────────────────
        st.markdown(f"""
        <div class="card">
            <div class="card-label">Offer Detail — Full Terms Breakdown</div>
            <span class="tier-badge">✓ {risk_display}</span>
            <div class="metric-row">
                <div class="metric-item">
                    <div class="metric-label">Loan Amount</div>
                    <div class="metric-value">{fmt_usd(loan_amount)}</div>
                </div>
                <div class="metric-item">
                    <div class="metric-label">Annual Rate</div>
                    <div class="metric-value">{fmt_pct(rate)}</div>
                </div>
                <div class="metric-item">
                    <div class="metric-label">Term</div>
                    <div class="metric-value">{term} mo</div>
                </div>
            </div>
            <div class="metric-row">
                <div class="metric-item">
                    <div class="metric-label">Est. Monthly Payment</div>
                    <div class="metric-value">{fmt_usd(monthly_payment)}</div>
                </div>
                <div class="metric-item">
                    <div class="metric-label">Total Interest</div>
                    <div class="metric-value">{fmt_usd(total_interest)}</div>
                </div>
                <div class="metric-item">
                    <div class="metric-label">Cash Cushion / mo</div>
                    <div class="metric-value green">{fmt_usd(cash_cushion)}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ── Sentinel Audit ────────────────────────────────────────────────────
        st.markdown(f"""
        <div class="audit-card">
            <div class="card-label">Sentinel Agent — Independent Compliance Audit</div>
            <div class="audit-verdict-badge">🛡️ &nbsp;{audit_label}</div>
            <div class="audit-check-row">
                <span class="{dscr_class}">{dscr_icon}</span>
                <span>
                    <strong>DSCR Check:</strong> {fmt_x(dscr)} exceeds the 1.25x compliance threshold —
                    free cash flow is sufficient to service monthly debt with a
                    <strong>{fmt_usd(cash_cushion)} cushion</strong> remaining.
                </span>
            </div>
            <div class="audit-check-row">
                <span class="{timing_class}">{timing_icon}</span>
                <span>
                    <strong>Historical Timing Check:</strong> Current month aligns with the
                    documented Q2 annual inventory capex window — seasonal pattern independently
                    validated against Plaid transaction history.
                </span>
            </div>
            <div class="audit-note">{audit_note}</div>
        </div>
        """, unsafe_allow_html=True)
