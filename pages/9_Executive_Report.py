import streamlit as st

from analysis_engine.metadata import generate_metadata

st.set_page_config(
    page_title="Executive Report",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Executive Report")

st.caption("Generate a consolidated summary of all completed analyses.")

st.divider()

# -----




# -----


st.divider()

left, middle, right = st.columns([1, 8, 3])

with left:
    if st.button("◀︎︎ Previous"):
        st.switch_page("pages/8_Multivariate_Analysis.py")

with right:
    if st.button("💾 Export Report", disabled=False):
        st.write("Report preparation in progress. Please wait...")


st.divider()

st.markdown(
    "<div style='text-align: center; color: gray; font-size: 14px;'>"
    "AutoEDA Studio • Built by Gopikrishna"
    "</div>",
    unsafe_allow_html=True
)