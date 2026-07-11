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

if "df" not in st.session_state:

    st.warning("⚠️ Please upload a dataset first.")

    st.stop()

df = st.session_state["df"]

file_name = st.session_state["file_name"]

st.write(f"**📄 Dataset Name:** {file_name}")

st.write(f"**📊 Total Rows:** {df.shape[0]:,}")

st.write(f"**📑 Total Columns:** {df.shape[1]}")

st.divider()

st.subheader("Purpose")

st.write("""
Univariate Analysis examines each variable independently to understand
its distribution, characteristics, and overall data quality before
exploring relationships with other variables.
""")

st.divider()

st.subheader("Upcoming Analysis Modules")

st.write("📈 Distribution Analysis")

st.write("📉 Histogram")

st.write("📦 Box Plot")

st.write("📐 Skewness")

st.write("📏 Kurtosis")

st.write("🔢 Frequency Distribution")

st.write("📋 Value Counts")

st.divider()

st.success("✅ Dataset is ready for Univariate Analysis.")

# -------




# -----
st.divider()

left, middle, right = st.columns([1, 8, 1])

with left:
    if st.button("⬅ Previous"):
        st.switch_page("pages/3_Duplicate_Row_Analysis.py")

with right:
    if st.button("Next ➜"):
        st.switch_page("pages/5_Outlier_Analysis.py")

st.divider()

st.markdown(
    "<div style='text-align: center; color: gray; font-size: 14px;'>"
    "AutoEDA Studio • Built by Gopikrishna"
    "</div>",
    unsafe_allow_html=True
)