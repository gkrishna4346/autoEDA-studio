import streamlit as st

from analysis_engine.metadata import generate_metadata

st.set_page_config(
    page_title="Dataset Overview",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dataset Overview")

st.caption("Understand your dataset before proceeding with further analysis.")

st.divider()


if "df" not in st.session_state:

    st.warning("⚠️ Please upload a dataset first.")

    st.stop()

df = st.session_state["df"]

file_name = st.session_state["file_name"]

metadata = generate_metadata(df)

left, right = st.columns(2)

with left:

    st.write(f"**📄 Dataset Name:** {file_name}")

    st.write(f"**📊 Rows:** {metadata['rows']:,}")

    st.write(f"**📑 Columns:** {metadata['columns']}")

    st.write(f"**🔢 Numeric Columns:** {metadata['numeric_columns']}")

    st.write(f"**🔤 Categorical Columns:** {metadata['categorical_columns']}")

with right:

    if metadata["datetime_columns"] == 0:
        st.write("ℹ️ **Datetime Columns:** No datetime columns detected")
    else:
        st.write(f"📅 **Datetime Columns:** {metadata['datetime_columns']}")

    if metadata["boolean_columns"] == 0:
        st.write("ℹ️ **Boolean Columns:** No boolean columns detected")
    else:
        st.write(f"✅ **Boolean Columns:** {metadata['boolean_columns']}")

    if metadata["missing_values"] == 0:
        st.write("✅ **Missing Values:** No missing values found")
    else:
        st.write(f"⚠️ **Missing Values:** {metadata['missing_values']:,} detected")

    if metadata["duplicate_rows"] == 0:
        st.write("✅ **Duplicate Rows:** No duplicate rows found")
    else:
        st.write(f"⚠️ **Duplicate Rows:** {metadata['duplicate_rows']:,} detected")

    memory_mb = metadata["memory_usage_kb"] / 1024

    st.write(f"💾 **Memory Usage:** {memory_mb:.2f} MB")


st.divider()

col1, col2 = st.columns([1,1])

with col1:
    if st.button("⬅ Previous"):
        st.switch_page("app.py")
with col2:
    if st.button("Next ➜"):
        st.switch_page("pages/2_Missing_Value_Analysis.py")

st.divider()

st.markdown(
    "<div style='text-align: center; color: gray; font-size: 14px;'>"
    "AutoEDA Studio • Built by Gopikrishna"
    "</div>",
    unsafe_allow_html=True
)