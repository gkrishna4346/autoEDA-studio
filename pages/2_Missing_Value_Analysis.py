import streamlit as st

from analysis_engine.metadata import generate_metadata

st.set_page_config(
    page_title="Missing Value Analysis",
    page_icon="🟢",
    layout="wide"
)

st.title("🟢 Missing Value Analysis")

st.caption("Evaluate the completeness of your dataset by identifying missing values.")

st.divider()

st.write(" * Missing values treatment will be decided based on the percentage of missing values data vs overall data.")

st.write(" * Since there are no missing values in your current dataset, No Analysis will be performed in this stage.")

st.success(
    "📚 **Need help deciding?**\n\n"
    "Explore the **Missing Value Playbook** to understand each treatment technique, "
    "its advantages, limitations, practical examples, and recommended use cases."
)

if st.button("📖 Open Playbook"):
    st.switch_page("pages/10_Missing_Value_Playbook.py")

st.divider()

left, middle, right = st.columns([1, 8, 1])

with left:
    if st.button("◀ Previous"):
        st.switch_page("pages/1_Dataset_Overview.py")

with right:
    if st.button("Next ▶"):
        st.switch_page("pages/3_Duplicate_Row_Analysis.py")

st.divider()

st.markdown(
    "<div style='text-align: center; color: gray; font-size: 14px;'>"
    "AutoEDA Studio • Built by Gopikrishna"
    "</div>",
    unsafe_allow_html=True
)