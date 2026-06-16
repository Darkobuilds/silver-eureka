import streamlit as st

# Page config
st.set_page_config(
    page_title="LeaseGuard Lite",
    layout="centered"
)

# Title
st.title("🏢 LeaseGuard Lite: CRE Risk Scanner")

st.markdown("""
Analyze commercial lease text for risky clauses and calculate  
**risk-adjusted Net Operating Income (NOI)**.
""")

# -----------------------------
# USER INPUTS
# -----------------------------
lease_text = st.text_area("📄 Paste Lease Text Here", height=200)

rent = st.number_input("💰 Annual Rent ($)", value=100000)
expenses = st.number_input("📉 Operating Expenses ($)", value=30000)

# -----------------------------
# ANALYSIS BUTTON
# -----------------------------
if st.button("🔍 Analyze Lease"):

    if not lease_text:
        st.warning("Please paste lease text before analyzing.")
    else:
        # Risk keywords
        risk_words = [
            "uncapped",
            "structural",
            "indemnify",
            "capital repairs",
            "liability",
            "termination penalty"
        ]

        lease_lower = lease_text.lower()

        # Detect risks
        risks = [word for word in risk_words if word in lease_lower]

        # Financial calculations
        noi = rent - expenses
        risk_penalty = 0.05 * noi * len(risks)  # more risks = higher penalty
        adjusted_noi = noi - risk_penalty

        # Risk score
        risk_score = min(len(risks) * 2, 10)

        # -----------------------------
        # OUTPUT RESULTS
        # -----------------------------
        st.subheader("📊 Results")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Net Operating Income", f"${noi:,.0f}")

        with col2:
            st.metric("Risk-Adjusted NOI", f"${adjusted_noi:,.0f}")

        st.metric("Risk Score", f"{risk_score}/10")

        # Risk details
        if risks:
            st.error("🔴 HIGH RISK DETECTED")
            st.write("⚠️ Risky clauses found:")
            for r in risks:
                st.write(f"- {r}")
        else:
            st.success("🟢 LOW RISK — No major clauses found")

        # Explanation
        st.markdown("""
        ---
        **How it works:**
        - Scans lease text for predefined high-risk clauses
        - Calculates NOI = Rent − Expenses
        - Applies penalty based on detected risks
        """)

# Footer
st.markdown("---")
st.caption("Built with Python + Streamlit | REPE Due Diligence Tool")
