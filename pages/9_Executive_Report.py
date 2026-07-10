import streamlit as st

from analysis_engine.metadata import generate_metadata

st.set_page_config(
    page_title="Executive Report",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Executive Report")

st.caption("Understand your dataset before proceeding with further analysis.")

st.divider()

# -----




# -----
st.divider()

col1, col2 = st.columns([1,1])

with col1:
    if st.button("⬅ Previous"):
        st.switch_page("pages/8_Multivariate_Analysis.py")
with col2:
    if st.button("Export Report", disabled=False):
        st.write("Report preparation in progress. Please wait...")


st.divider()

st.markdown(
    "<div style='text-align: center; color: gray; font-size: 14px;'>"
    "AutoEDA Studio • Built by Gopikrishna"
    "</div>",
    unsafe_allow_html=True
)