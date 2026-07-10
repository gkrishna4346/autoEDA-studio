import streamlit as st

from analysis_engine.metadata import generate_metadata

st.set_page_config(
    page_title="Univariate Analysis",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Univariate Analysis")

st.caption("Understand the distribution and characteristics of individual variables.")

st.divider()

# -----




# -----
st.divider()

col1, col2 = st.columns([1,1])

with col1:
    if st.button("⬅ Previous"):
        st.switch_page("pages/3_Duplicate_Row_Analysis.py")
with col2:
    if st.button("Next ➜"):
        st.switch_page("pages/5_Outlier_Analysis.py")


st.divider()

st.markdown(
    "<div style='text-align: center; color: gray; font-size: 14px;'>"
    "AutoEDA Studio • Built by Gopikrishna"
    "</div>",
    unsafe_allow_html=True
)