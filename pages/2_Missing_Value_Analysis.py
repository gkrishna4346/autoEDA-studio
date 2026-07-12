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
    page_title="Missing Value Analysis",
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

st.title("🟢 Missing Value Analysis")

st.caption(
    "Analyze missing values and apply the appropriate treatment before proceeding with further analysis."
)

st.divider()

# --------------------------------------------------
# Missing Value Playbook
# --------------------------------------------------

st.success(
    "📚 **Need help deciding?**\n\n"
    "Explore the **Missing Value Playbook** to understand each treatment "
    "technique, advantages, limitations, practical examples and recommended use cases."
)

if st.button("📖 Open Missing Value Playbook"):

    st.switch_page("pages/10_Missing_Value_Playbook.py")

st.divider()

# --------------------------------------------------
# Overall Summary
# --------------------------------------------------

st.subheader("Overall Missing Value Summary")

st.info(
    "Summary will appear after analyzing the uploaded dataset."
)

st.divider()

# --------------------------------------------------
# Column-wise Summary
# --------------------------------------------------

st.subheader("Column-wise Missing Value Summary")

st.info(
    "Column-wise missing value statistics will be displayed here."
)

st.divider()

# --------------------------------------------------
# Treatment Selection
# --------------------------------------------------

st.subheader("Treatment Selection")

left, right = st.columns(2)

with left:

    st.selectbox(
        "Select Column",
        [
            "Sample Column"
        ],
        disabled=True
    )

with right:

    st.radio(
        "Treatment Method",
        [
            "No Treatment (Leave as Is)"
        ],
        disabled=False
    )

st.write("")

if st.button(
    "Apply Treatment",
    use_container_width=True
):

    st.success(
        "Treatment completed successfully.\n\n"
        "Selected Method : No Treatment (Leave as Is)\n\n"
        "The working dataset remains unchanged."
    )

st.divider()

# --------------------------------------------------
# Treatment Summary
# --------------------------------------------------

st.subheader("Treatment Summary")

st.info(
"""
**Column**

Sample Column

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

        st.switch_page("pages/1_Dataset_Overview.py")

with right:

    if st.button("Next ▶"):

        st.switch_page("pages/3_Duplicate_Row_Analysis.py")

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