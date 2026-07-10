import streamlit as st

from analysis_engine.metadata import generate_metadata

st.set_page_config(
    page_title="Duplicate Record Analysis",
    page_icon="🟢",
    layout="wide"
)

st.title("🟢 Duplicate Record Analysis")

st.caption("Understand your dataset before proceeding with further analysis.")

st.divider()

st.write(" * Duplicate Record treatment will be decided based on the percentage of Duplicate records vs Overall data.")

st.write(" * Since there are duplicate records in your current dataset, No Analysis will be performed in this stage.")


st.divider()

col1, col2 = st.columns([1,1])

with col1:
    if st.button("⬅ Previous"):
        st.switch_page("pages/2_Missing_Value_Analysis.py")
with col2:
    if st.button("Next ➜"):
        st.switch_page("pages/4_Univariate_Analysis.py")


st.divider()

st.markdown(
    "<div style='text-align: center; color: gray; font-size: 14px;'>"
    "AutoEDA Studio • Built by Gopikrishna"
    "</div>",
    unsafe_allow_html=True
)