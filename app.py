import streamlit as st

from datasources.csv_loader import load_csv


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="AutoEDA Studio",
    page_icon="📊",
    layout="wide"
)

st.title("🏠 Welcome")
# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("📊 AutoEDA Studio")

st.subheader("Analyze Data. Support Decisions.")

st.write(
    """
Welcome to AutoEDA Studio.

AutoEDA Studio helps Data Analysts, Business Analysts and Data Scientists
perform structured Exploratory Data Analysis through a guided workflow.
"""
)

# Initialize Session State
if "analysis_started" not in st.session_state:
    st.session_state.analysis_started = False

# Start Analysis Button
if st.button("🚀 Start Analysis"):
    st.session_state.analysis_started = True

# Show analysis options after button is clicked
if st.session_state.analysis_started:

    st.subheader("Select Data Source")

    source = st.radio(
        "Choose your data source",
        [
            "📄 CSV",
            "📗 Excel (Coming Soon)",
            "🐘 PostgreSQL (Coming Soon)",
            "🗄 SQL Server (Coming Soon)",
            "🏛 Oracle (Coming Soon)",
            "❄️ Snowflake (Coming Soon)"
        ]
    )

    if source == "📄 CSV":

        uploaded_file = st.file_uploader(
            "Upload CSV File",
            type=["csv"]
        )



        if uploaded_file is not None:

            df = load_csv(uploaded_file)

            # Save for next page
            st.session_state["df"] = df
            st.session_state["file_name"] = uploaded_file.name

            st.success("✅ Dataset uploaded successfully!")

            st.write(f"**Dataset:** {uploaded_file.name}")

            st.write(f"**Rows Detected:** {df.shape[0]:,}")

            st.write(f"**Columns Detected:** {df.shape[1]}")

            if st.button("Next ▶︎"):
                st.switch_page("pages/1_Dataset_Overview.py")

st.divider()

st.markdown(
    "<div style='text-align: center; color: gray; font-size: 14px;'>"
    "AutoEDA Studio • Built by Gopikrishna"
    "</div>",
    unsafe_allow_html=True
)