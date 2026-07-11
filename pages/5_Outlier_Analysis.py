import streamlit as st

from analysis_engine.metadata import generate_metadata

st.set_page_config(
    page_title="Outlier Analysis",
    page_icon="📍",
    layout="wide"
)

st.title("📍 Outlier Analysis")

st.caption("Identify unusual observations that may influence statistical analysis and predictive models.")

st.divider()

# -----




# -----


st.divider()

left, middle, right = st.columns([1, 8, 1])

with left:
    if st.button("◀ Previous"):
        st.switch_page("pages/4_Univariate_Analysis.py")

with right:
    if st.button("Next ▶︎"):
        st.switch_page("pages/6_Bivariate_Analysis.py")


st.divider()

st.markdown(
    "<div style='text-align: center; color: gray; font-size: 14px;'>"
    "AutoEDA Studio • Built by Gopikrishna"
    "</div>",
    unsafe_allow_html=True
)