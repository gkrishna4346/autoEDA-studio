import streamlit as st

# ----------------------------------------------------------
# Page Configuration
# ----------------------------------------------------------

st.set_page_config(
    page_title="Missing Value Playbook",
    page_icon="📚",
    layout="wide"
)

# ----------------------------------------------------------
# Custom CSS
# ----------------------------------------------------------

st.markdown("""
<style>

.main-title{
    font-size:40px;
    font-weight:bold;
    color:#1F4E79;
    text-align:center;
    margin-bottom:0px;
}

.sub-title{
    font-size:18px;
    color:gray;
    text-align:center;
    margin-top:0px;
    margin-bottom:30px;
}

.info-box{
    background-color:#F8FAFC;
    padding:20px;
    border-left:8px solid #1F77B4;
    border-radius:10px;
    margin-top:10px;
    margin-bottom:20px;
}

.note-box{
    background-color:#FFF8E6;
    padding:15px;
    border-left:6px solid #F4B400;
    border-radius:8px;
    margin-top:15px;
}

.green-box{
    background-color:#F0FFF4;
    padding:15px;
    border-left:6px solid #2E8B57;
    border-radius:8px;
    margin-top:15px;
}

.warning-box{
    background-color:#FFF5F5;
    padding:15px;
    border-left:6px solid #E74C3C;
    border-radius:8px;
    margin-top:15px;
}

h4{
    color:#1F4E79;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# Header
# ----------------------------------------------------------
if st.button("◀ Back to Previous page"):
    st.switch_page("pages/2_Missing_Value_Analysis.py")

st.markdown(
"""
<div class='main-title'>
📚 Missing Value Playbook
</div>

<div class='sub-title'>
Learn • Decide • Apply
</div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class='info-box'>

Missing values are one of the most common challenges encountered during
Exploratory Data Analysis (EDA).

Choosing the appropriate treatment technique is not about following a fixed
rule. It requires understanding the nature of the data, business objective,
distribution, and analytical requirements.

This playbook serves as a practical reference guide to help analysts
understand various missing value treatment techniques, their advantages,
limitations, and suitable use cases before making an informed decision.

</div>
""",
unsafe_allow_html=True
)

st.divider()

# ==========================================================
# 🎯 Understanding Missing Values
# ==========================================================

with st.expander("🎯 Understanding Missing Values", expanded=True):

    st.markdown("""

### What are Missing Values?

Missing values represent the absence of data for one or more observations
within a dataset. They are commonly represented as **NaN**, **NULL**, or blank
cells depending on the data source.

Missing values are inevitable in real-world datasets and can occur due to
multiple reasons during data collection, storage, migration, or business
processes.

---

### Common Reasons for Missing Values

- Customer skipped a question.
- Data was unavailable during collection.
- System or application failure.
- Data entry errors.
- Sensor malfunction.
- Data migration issues.
- Confidential or restricted information.

---

### Should Every Missing Value Be Treated?

**No.**

Not every missing value requires treatment.

Sometimes retaining the missing values is the most appropriate decision,
especially during exploratory analysis.

Before selecting any treatment technique, always evaluate the dataset from
both statistical and business perspectives.

""")

    st.markdown("""
<div class='note-box'>

<b>Consider the following before choosing a treatment:</b>

<ul>

<li>Business Objective</li>

<li>Percentage of Missing Values</li>

<li>Importance of the Feature</li>

<li>Data Type (Numerical / Categorical / Text / Time Series)</li>

<li>Distribution of the Data</li>

<li>Domain Knowledge</li>

<li>Project Requirements</li>

</ul>

</div>
""",
unsafe_allow_html=True)

st.divider()

# ==========================================================
# 🟢 Basic Techniques
# ==========================================================

st.markdown("## 🟢 Basic Techniques")

# ==========================================================
# 🟢 Basic Techniques
# ==========================================================

st.markdown("## 🟢 Basic Techniques")

with st.expander("No Treatment (Leave As Is)"):
    st.write("Content will be added here.")

with st.expander("Delete Rows"):
    st.write("Content will be added here.")

with st.expander("Delete Columns"):
    st.write("Content will be added here.")

with st.expander("Mean Imputation"):
    st.write("Content will be added here.")

with st.expander("Median Imputation"):
    st.write("Content will be added here.")

with st.expander("Mode Imputation"):
    st.write("Content will be added here.")

# ==========================================================
# 🔷 Advanced Techniques
# ==========================================================

st.markdown("## 🔷 Advanced Techniques")

with st.expander("K-Nearest Neighbour (KNN) Imputation"):
    st.write("Content will be added here.")

with st.expander("Linear Interpolation"):
    st.write("Content will be added here.")

with st.expander("Forward Fill"):
    st.write("Content will be added here.")

with st.expander("Backward Fill"):
    st.write("Content will be added here.")

# ==========================================================
# 📊 Reference
# ==========================================================

st.markdown("## 📊 Reference")

with st.expander("Treatment by Data Type"):
    st.write("Content will be added here.")

with st.expander("Best Practices"):
    st.write("Content will be added here.")

with st.expander("Final Thought"):
    st.write("Content will be added here.")