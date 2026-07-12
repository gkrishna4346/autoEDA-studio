import streamlit as st

from analysis_engine.dataset_metadata import generate_metadata

from utils.session_manager import (
    initialize_session,
    is_project_active,
    get_working_dataframe
)

initialize_session()

st.title("📊 Dataset Overview")

st.caption("Understand your dataset before proceeding with further analysis.")

st.divider()


if not is_project_active():

    st.warning("⚠️ No active project found.")

    st.switch_page("app.py")

    st.stop()

df = get_working_dataframe()

file_name = st.session_state.get("file_name", "")

metadata = generate_metadata(df)

statistical_summary = df.describe(include="all").transpose()

left, right = st.columns(2)

with left:

    st.markdown(
        f"""
        <div style="text-align:center; line-height:2.2;">
            📄 <b>Dataset Name:</b> {file_name}<br>
            📊 <b>Rows:</b> {metadata['rows']:,}<br>
            📑 <b>Columns:</b> {metadata['columns']}<br>
            🔢 <b>Numeric Columns:</b> {metadata['numeric_columns']}<br>
            🔤 <b>Categorical Columns:</b> {metadata['categorical_columns']}
        </div>
        """,
        unsafe_allow_html=True
    )
with right:

    memory_mb = metadata["memory_usage_kb"] / 1024

    datetime_text = (
        "ℹ️ <b>Datetime Columns:</b> No datetime columns detected"
        if metadata["datetime_columns"] == 0
        else f"📅 <b>Datetime Columns:</b> {metadata['datetime_columns']}"
    )

    boolean_text = (
        "ℹ️ <b>Boolean Columns:</b> No boolean columns detected"
        if metadata["boolean_columns"] == 0
        else f"✅ <b>Boolean Columns:</b> {metadata['boolean_columns']}"
    )

    missing_text = (
        "✅ <b>Missing Values:</b> No missing values found"
        if metadata["missing_values"] == 0
        else f"⚠️ <b>Missing Values:</b> {metadata['missing_values']:,} detected"
    )

    duplicate_text = (
        "✅ <b>Duplicate Rows:</b> No duplicate rows found"
        if metadata["duplicate_rows"] == 0
        else f"⚠️ <b>Duplicate Rows:</b> {metadata['duplicate_rows']:,} detected"
    )

    st.markdown(
        f"""
        <div style="text-align:center; line-height:2.2;">
            {datetime_text}<br>
            {boolean_text}<br>
            {missing_text}<br>
            {duplicate_text}<br>
            💾 <b>Memory Usage:</b> {memory_mb:.2f} MB
        </div>
        """,
        unsafe_allow_html=True
    )


st.divider()



categorical_df = df.select_dtypes(
    include=["object", "category"]
)

if not categorical_df.empty:
    categorical_summary = (
        categorical_df
        .describe()
        .transpose()
    )
else:
    categorical_summary = None

numeric_summary = df.describe().transpose()

numeric_summary["count"] = (
    numeric_summary["count"]
    .astype(int)
)

for col in numeric_summary.columns:
    if col != "count":
        numeric_summary[col] = numeric_summary[col].round(2)

numeric_summary["count"] = (
    numeric_summary["count"]
    .astype(int)
)

if categorical_summary is not None:

    categorical_summary["count"] = (
        categorical_summary["count"]
        .astype(int)
    )

    categorical_summary["freq"] = (
        categorical_summary["freq"]
        .astype(int)
    )


left, center, right = st.columns([2, 8, 2])

with center:
    st.subheader("🔢 Numerical Statistical Summary")
    st.table(numeric_summary)

st.write("")

left, center, right = st.columns([3, 6, 3])

with center:
    st.subheader("🔤 Categorical Statistical Summary")

    if categorical_summary is not None:
        st.table(categorical_summary)
    else:
        st.info("ℹ️ No categorical columns found in the dataset.")



st.divider()

left, middle, right = st.columns([1, 8, 1])

with left:
    if st.button("◀︎ Previous"):
        st.switch_page("app.py")

with right:
    if st.button("Next ▶︎"):
        st.switch_page("pages/2_Missing_Value_Analysis.py")




st.divider()

st.markdown(
    "<div style='text-align:left; margin-left:20px; color: gray; font-size: 14px;'>"
    "AutoEDA Studio • Built by Gopikrishna"
    "</div>",
    unsafe_allow_html=True
)