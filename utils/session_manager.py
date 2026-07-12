import streamlit as st


# --------------------------------------------------
# Initialize Session
# --------------------------------------------------

def initialize_session():
    defaults = {
        # Project
        "project_active": False,
        "df_original": None,
        "df_working": None,
        "file_name": None,
        "processing_history": [],

        # Univariate Analysis
        "selected_univariate_columns": [],
        "univariate_analysis_completed": False,

        # Bivariate Analysis (future)
        "selected_bivariate_columns": [],
        "bivariate_analysis_completed": False,
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


# --------------------------------------------------
# Create Project
# --------------------------------------------------

def create_project(df, file_name):

    st.session_state.project_active = True
    st.session_state.df_original = df.copy()
    st.session_state.df_working = df.copy()
    st.session_state.file_name = file_name
    st.session_state.processing_history = []


# --------------------------------------------------
# Reset Project
# --------------------------------------------------

def reset_project():

    for key in list(st.session_state.keys()):
        del st.session_state[key]


# --------------------------------------------------
# Check Project Status
# --------------------------------------------------

def is_project_active():

    return st.session_state.get("project_active", False)


# --------------------------------------------------
# Get Working Dataset
# --------------------------------------------------

def get_working_dataframe():

    return st.session_state.get("df_working")