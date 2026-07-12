import streamlit as st

from utils.session_manager import (
    initialize_session,
    is_project_active,
    get_working_dataframe
)

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Duplicate Record Analysis",
    page_icon="🟢",
    layout="wide"
)

initialize_session()

# --------------------------------------------------
# Check Active Project
# --------------------------------------------------

if not is_project_active():

    st.warning("⚠ No active project found.")

    st.switch_page("app.py")

    st.stop()

df = get_working_dataframe()

# --------------------------------------------------
# Page Header
# --------------------------------------------------

st.title("🟢 Duplicate Record Analysis")

st.caption(
    "Identify duplicate records and apply the appropriate treatment before proceeding with further analysis."
)

st.divider()

# --------------------------------------------------
# Duplicate Record Playbook (Reserved)
# --------------------------------------------------

st.info(
    """
**Treatment Framework**

This page helps you identify duplicate records, review the affected rows,
choose an appropriate treatment technique, and apply the selected method
before proceeding with further analysis.
"""
)

st.divider()

# --------------------------------------------------
# Overall Summary
# --------------------------------------------------

st.subheader("Overall Duplicate Record Summary")

st.info(
    "Summary will appear after analyzing the uploaded dataset."
)

st.divider()

# --------------------------------------------------
# Duplicate Record Summary
# --------------------------------------------------

st.subheader("Duplicate Record Summary")

st.info(
    "Duplicate record statistics will be displayed here."
)

st.divider()

# --------------------------------------------------
# Treatment Selection
# --------------------------------------------------

st.subheader("Treatment Selection")

left, right = st.columns(2)

with left:

    st.selectbox(
        "Treatment Scope",
        [
            "Entire Dataset"
        ],
        disabled=True
    )

with right:

    st.radio(
        "Treatment Method",
        [
            "No Treatment (Leave as Is)"
        ]
    )

st.write("")

if st.button(
    "Apply Treatment",
    use_container_width=True
):

    st.success(
        """
Treatment completed successfully.

Selected Method : No Treatment (Leave as Is)

The working dataset remains unchanged.
"""
    )

st.divider()

# --------------------------------------------------
# Treatment Summary
# --------------------------------------------------

st.subheader("Treatment Summary")

st.info(
"""
**Scope**

Entire Dataset

**Treatment**

No Treatment (Leave as Is)

**Status**

Completed
"""
)

st.divider()

# --------------------------------------------------
# Navigation
# --------------------------------------------------

left, middle, right = st.columns([1,8,1])

with left:

    if st.button("◀ Previous"):

        st.switch_page("pages/2_Missing_Value_Analysis.py")

with right:

    if st.button("Next ▶"):

        st.switch_page("pages/4_Univariate_Analysis.py")

st.divider()

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown(
    """
    <div style="
        text-align:left;
        margin-left:20px;
        color:gray;
        font-size:14px;">
        AutoEDA Studio • Built by Gopikrishna
    </div>
    """,
    unsafe_allow_html=True
)