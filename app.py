import streamlit as st
import pandas as pd
import os
from agents import run_agents
from PIL import Image

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(
    page_title="Agentic AI – B2B RFP Automation",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ======================
# CUSTOM CSS (EY STYLE)
# ======================
st.markdown("""
<style>
body {
    background-color: #0E1117;
}
.block-container {
    padding-top: 2rem;
}
.card {
    background-color: #161B22;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 20px;
    box-shadow: 0px 0px 12px rgba(0,0,0,0.4);
}
h1, h2, h3 {
    color: #F9FAFB;
}
.small-text {
    color: #9CA3AF;
}
.highlight {
    color: #FACC15;
    font-weight: 600;
}
.center {
    display: flex;
    justify-content: center;
}
</style>
""", unsafe_allow_html=True)

# ======================
# HEADER WITH EY LOGO
# ======================
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    try:
        logo = Image.open("eylogo.jpg")
        st.image(logo, width=140)
    except:
        st.warning("EY_Logo.png not found")

st.markdown(
    "<h1 style='text-align:center;'>Agentic AI – B2B RFP Automation System</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='small-text' style='text-align:center;'>Automating RFP Discovery, Technical Matching & Pricing using Multi-Agent AI</p>",
    unsafe_allow_html=True
)

st.divider()

# ======================
# RUN AGENTS
# ======================
data = run_agents()

# ======================
# STEP 1 – SALES AGENT
# ======================
st.markdown("## RFP Detection & Summary (Sales Agent)")
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.text(data["rfp_text"])
    st.markdown("</div>", unsafe_allow_html=True)

# ======================
# STEP 2 – TECHNICAL AGENT
# ======================
st.markdown("## Technical SKU Matching (Technical Agent)")
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.dataframe(data["matches"], use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ======================
# STEP 3 – PRICING AGENT
# ======================
st.markdown("## Pricing Estimation (Pricing Agent)")
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.json(data["pricing"])
    st.markdown("</div>", unsafe_allow_html=True)

# ======================
# FINAL OUTPUT
# ======================
st.success("RFP Response Generated Successfully")

st.markdown("## 📄 Final Output (Master Agent)")
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown(f"""
    **Recommended SKU:** <span class='highlight'>{data['pricing']['SKU']}</span><br>
    **Total Cost:** <span class='highlight'>₹ {int(data['pricing']['Total Cost']):,}</span>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ======================
# ACTION BUTTONS
# ======================
colA, colB = st.columns(2)

with colA:
    st.button("📥 Download Final RFP Quotation (PDF)", use_container_width=True)

with colB:
    if st.button("💾 Save RFP Data (For Records)", use_container_width=True):
        os.makedirs("saved_rfps", exist_ok=True)

        data["matches"].to_csv("saved_rfps/sku_matching.csv", index=False)
        pd.DataFrame([data["pricing"]]).to_csv("saved_rfps/pricing.csv", index=False)

        with open("saved_rfps/rfp_summary.txt", "w") as f:
            f.write(data["rfp_text"])

        st.success("RFP data saved successfully")
