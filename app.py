import streamlit as st

from datasources.csv_loader import load_csv
from utils.session_manager import (
    initialize_session,
    create_project,
    reset_project,
    is_project_active
)

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AutoEDA Studio",
    layout="wide"
)

# --------------------------------------------------
# Theme
# --------------------------------------------------

st.markdown("""
<style>

.stApp{
    background-color:#F5F7FC;
}

/* Main Container */

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

/* Headers */

h1,h2,h3{
    color:#1F2937;
}

/* Paragraph */

p{
    color:#4B5563;
}

/* Horizontal Line */

hr{
    border:1px solid #DCE3F0;
}

/* Card */

.custom-card{

    background:white;

    border:1px solid #DCE3F0;

    border-radius:18px;

    padding:24px;

    box-shadow:0px 2px 10px rgba(34,45,80,.08);

}

/* Success */

.success-box{

    background:#ECFDF5;

    border-left:6px solid #22C55E;

    padding:15px;

    border-radius:12px;

}

/* Information */

.info-box{

    background:#EEF2FF;

    border-left:6px solid #5569B0;

    padding:15px;

    border-radius:12px;

}

/* Warning */

.warning-box{

    background:#FFF8E6;

    border-left:6px solid #F59E0B;

    padding:15px;

    border-radius:12px;

}

/* Error */

.error-box{

    background:#FEF2F2;

    border-left:6px solid #EF4444;

    padding:15px;

    border-radius:12px;

}

/* Buttons */

.stButton>button{

    border-radius:10px;

    height:46px;

    font-weight:600;

}

/* Expander */

.streamlit-expanderHeader{

    font-size:18px;

    font-weight:600;

}

</style>
""", unsafe_allow_html=True)


initialize_session()

# --------------------------------------------------
# Header
# --------------------------------------------------

col_logo, col_title = st.columns([1, 8])

with col_logo:
    st.markdown(
        """
        <div style="
            width:70px;
            height:70px;
            border-radius:12px;
            background:#ECECEC;
            display:flex;
            align-items:center;
            justify-content:center;
            font-weight:bold;
            font-size:18px;">
            LOGO
        </div>
        """,
        unsafe_allow_html=True
    )

with col_title:

    st.title("AutoEDA Studio")

    st.markdown(
        "<h5 style='color:#666;'>"
        "Structured Exploratory Data Analysis for modern analytics teams"
        "</h5>",
        unsafe_allow_html=True
    )

st.write("")


# --------------------------------------------------
# Analysis Section
# --------------------------------------------------

if not is_project_active():

    left, right = st.columns([1,1], gap="large")

    # ------------------------------------------
    # Left Side
    # ------------------------------------------

    with left:

        st.subheader("Select Data Source")

        source = st.radio(
            "Choose your data source",
            (
                "📄 CSV",
                "📗 Excel (Coming Soon)",
                "🐘 PostgreSQL (Coming Soon)",
                "🗄 SQL Server (Coming Soon)",
                "🏛 Oracle (Coming Soon)",
                "❄️ Snowflake (Coming Soon)"
            )
        )

    # ------------------------------------------
    # Right Side
    # ------------------------------------------

    with right:

        if source == "📄 CSV":

            uploaded_file = st.file_uploader(
                "Upload CSV File",
                type=["csv"]
            )

            if uploaded_file is not None:

                df = load_csv(uploaded_file)

                create_project(df, uploaded_file.name)

                st.rerun()

else:

    left, right = st.columns([1,1], gap="large")

    with left:

        st.subheader("Select Data Source")

        st.radio(
            "Choose your data source",
            (
                "📄 CSV",
                "📗 Excel (Coming Soon)",
                "🐘 PostgreSQL (Coming Soon)",
                "🗄 SQL Server (Coming Soon)",
                "🏛 Oracle (Coming Soon)",
                "❄️ Snowflake (Coming Soon)"
            ),
            disabled=True
        )

    with right:

        st.markdown(
            f"""
            <div style="
                background:#CADBED;
                border-left:4px solid #16406B;
                padding:8px 12px;
                border-radius:8px;
                font-size:14px;
                color:#16406B;">
                ✅ <b>{st.session_state.file_name}</b><br>
                Project Status : <b>Active Session</b>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        c1, c2 = st.columns(2)

        with c1:

            if st.button("🗑 Reset Session", use_container_width=True):

                reset_project()

                st.rerun()

        with c2:

            if st.button("Next ▶", use_container_width=True):

                st.switch_page("pages/1_Dataset_Overview.py")

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.markdown(
    """
    <div style="
        text-align:center;
        color:gray;
        font-size:14px;">
        AutoEDA Studio • Built by Gopikrishna
    </div>
    """,
    unsafe_allow_html=True
)