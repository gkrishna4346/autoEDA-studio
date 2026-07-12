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
if st.button("◀ Return to Missing Value Analysis"):
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

    with st.expander("📖 What are Missing Values?"):

        st.markdown("""
Missing values represent the absence of data for one or more observations
within a dataset. They are commonly represented as **NaN**, **NULL**, or blank
cells depending on the data source.

Missing values are inevitable in real-world datasets and can occur due to
multiple reasons during data collection, storage, migration, or business
processes.
""")

    with st.expander("❓ Common Reasons for Missing Values"):

        st.markdown("""

- Customer skipped a question.

- Data was unavailable during collection.

- System or application failure.

- Data entry errors.

- Sensor malfunction.

- Data migration issues.

- Confidential or restricted information.

""")

    with st.expander("🧠 Should Every Missing Value Be Treated?"):

        st.markdown("""

**No.**

Not every missing value requires treatment.

Sometimes retaining the missing values is the most appropriate decision,
especially during exploratory analysis.

Before selecting any treatment technique, always evaluate the dataset from
both statistical and business perspectives.

""")

    with st.expander("📋 Consider Before Choosing a Treatment"):

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


with st.expander("🟢 No Treatment (Leave As Is)"):

    st.markdown("""

### 📖 Definition

Leave the missing values unchanged without performing any deletion or imputation.

---

### ✅ Best Used When

- Very few observations contain missing values.
- Missing values do not significantly affect the analysis.
- Certain algorithms can handle missing values internally.
- Further treatment will be performed during later stages.

---

### 👍 Advantages

- Preserves the original dataset.
- No artificial values are introduced.
- Avoids unnecessary data manipulation.

---

### ⚠ Limitations

- Some machine learning algorithms cannot process missing values.
- Missing values may affect downstream analysis and model performance.

---

### 💼 Example

Dataset contains **100,000** records.

Only **12** records have missing values.

Keeping them unchanged has negligible impact during exploratory analysis.

---

### 📝 Note

Pandas and most Seaborn visualizations automatically ignore missing (`NaN`) values while computing statistics and generating visualizations. However, the missing values remain in the dataset and should be treated appropriately before model building if required.

""")


with st.expander("🗑 Delete Rows"):

    st.markdown("""

### 📖 Definition

Remove records (rows) containing missing values from the dataset.

---

### ✅ Best Used When

- Missing values represent only a very small percentage of the dataset.
- Removing the affected rows has minimal business impact.

---

### 👍 Advantages

- Easy to implement.
- Produces a clean dataset.
- No artificial values are introduced.

---

### ⚠ Limitations

Loss of valuable information from **other variables (columns)** within the deleted records.

---

### 💼 Example

| Customer | Age | Salary |
|----------|----:|-------:|
|101|35|45000|
|102|NaN|72000|
|103|41|68000|

Deleting **Row 102** also removes the valid Salary value (**72000**).

""")

with st.expander("🗑 Delete Columns"):

    st.markdown("""

### 📖 Definition

Remove an entire feature (column) containing excessive missing values.

---

### ✅ Best Used When

- The column contains a very high percentage of missing values.
- The feature provides limited analytical or business value.

---

### 👍 Advantages

- Simplifies the dataset.
- Eliminates highly incomplete features.
- Reduces unnecessary complexity.

---

### ⚠ Limitations

Permanent loss of potentially useful information if the feature becomes important for future analysis.

---

### 💼 Example

Suppose the **Occupation** column contains **90%** missing values.

If the column is removed today,

future analysis such as

**"Customer Churn by Occupation"**

will no longer be possible.

""")

with st.expander("📈 Mean Imputation"):

    st.markdown("""

### 📖 Definition

Replace missing values using the arithmetic mean of the available observations.

---

### ✅ Best Used When

- Numerical variables.
- Approximately normally distributed data.

---

### 👍 Advantages

- Simple.
- Fast.
- Maintains dataset size.

---

### ⚠ Limitations

Sensitive to outliers because extreme values influence the mean.

---

### 💼 Example

40

45

50

55

NaN

↓

Mean = **47.5**

Missing value becomes **47.5**

""")

with st.expander("📊 Median Imputation"):

    st.markdown("""

### 📖 Definition

Replace missing values using the median of the available observations.

---

### ✅ Best Used When

- Skewed numerical data.
- Data containing outliers.

---

### 👍 Advantages

- Robust against outliers.
- Better represents the central tendency of skewed data.

---

### ⚠ Limitations

May not preserve the original distribution perfectly.

---

### 💼 Example

40

45

50

55

500

NaN

↓

Median = **50**

Notice that the extreme value **500** does not influence the replacement.

""")

with st.expander("📌 Mode Imputation"):

    st.markdown("""

### 📖 Definition

Replace missing values using the most frequently occurring value.

---

### ✅ Best Used When

- Categorical variables.
- Binary variables.
- Discrete numerical variables.

---

### 👍 Advantages

- Simple.
- Preserves common categories.
- Easy to interpret.

---

### ⚠ Limitations

May over-represent the most frequent category.

---

### 💼 Example

Department

HR

Finance

HR

Missing

HR

↓

Replace Missing with **HR**

""")

# ==========================================================
# 🔷 Advanced Techniques
# ==========================================================

st.markdown("## 🔷 Advanced Techniques")

with st.expander("🤝 K-Nearest Neighbour (KNN) Imputation"):

    st.markdown("""

### 📖 Definition

Replace missing values by identifying the **K most similar observations**
(nearest neighbours) based on other available features and estimating the
missing value from those neighbours.

---

### 🎯 Best Used When

- Numerical datasets.
- Features have meaningful relationships.
- Missing values are moderate.
- Dataset contains sufficient observations.

---

### 👍 Advantages

- Preserves relationships between variables.
- Often more accurate than Mean or Median imputation.
- Produces realistic estimates.

---

### ⚠ Limitations

- Computationally expensive for large datasets.
- Sensitive to feature scaling.
- Choosing an inappropriate value for **K** may reduce accuracy.

---

### 💼 Example

| Age | Experience | Salary |
|----:|-----------:|-------:|
|25|2|30000|
|26|3|32000|
|25|2|NaN|

Based on similar customers,
the missing Salary is estimated to be approximately **31000**.

---

### 📝 Note

KNN Imputation is generally more accurate than simple statistical
imputation methods but requires additional computation and careful
parameter tuning.

""")

with st.expander("📉 Linear Interpolation"):

    st.markdown("""

### 📖 Definition

Estimate missing values by assuming a straight-line relationship between
the previous and next available observations.

---

### 🎯 Best Used When

- Time-series datasets.
- Sensor readings.
- Weather data.
- Financial data.
- Sequential measurements.

---

### 👍 Advantages

- Preserves overall trends.
- Produces smooth transitions.
- Easy to implement.

---

### ⚠ Limitations

- Assumes linear change between observations.
- Not suitable for categorical variables.
- May not perform well when values fluctuate rapidly.

---

### 💼 Example

| Day | Temperature |
|----:|------------:|
|1|20|
|2|22|
|3|NaN|
|4|26|

Linear interpolation estimates

**Day 3 = 24**

---

### 📝 Note

Interpolation works best when neighbouring observations follow a
reasonably smooth trend.

""")

with st.expander("➡️ Forward Fill (Forward Propagation)"):

    st.markdown("""

### 📖 Definition

Replace missing values using the **previous available observation**.

---

### 🎯 Best Used When

- Time-series datasets.
- Inventory data.
- Sequential business records.
- Sensor measurements.

---

### 👍 Advantages

- Simple.
- Fast.
- Maintains continuity in sequential data.

---

### ⚠ Limitations

- Can propagate outdated values.
- Not suitable when values change frequently.

---

### 💼 Example

| Time | Stock Price |
|-----:|------------:|
|10:00|150|
|10:05|NaN|
|10:10|152|

Forward Fill

**10:05 = 150**

---

### 📝 Note

Forward Fill assumes that the previous observation remains valid until a
new observation becomes available.

""")

with st.expander("⬅️ Backward Fill (Backward Propagation)"):

    st.markdown("""

### 📖 Definition

Replace missing values using the **next available observation**.

---

### 🎯 Best Used When

- Time-series datasets.
- Sequential observations.
- Future observations are considered more representative.

---

### 👍 Advantages

- Simple.
- Easy to implement.
- Maintains continuity in sequential datasets.

---

### ⚠ Limitations

- Uses future information which may not always be appropriate.
- May introduce unrealistic assumptions in some scenarios.

---

### 💼 Example

| Time | Stock Price |
|-----:|------------:|
|10:00|150|
|10:05|NaN|
|10:10|152|

Backward Fill

**10:05 = 152**

---

### 📝 Note

Backward Fill is commonly used when future observations better represent
the missing value than previous observations.

""")

# ==========================================================
# 📊 Reference
# ==========================================================

st.markdown("## 📊 Reference")

with st.expander("📂 Treatment by Data Type"):

    st.markdown("""

Selecting an appropriate treatment technique depends on the type of data being analysed.

The table below provides general recommendations that can serve as a starting point. The final decision should always consider business requirements and domain knowledge.

""")

    st.table({

        "Data Type":[

            "Continuous Numerical",

            "Skewed Numerical",

            "Discrete Numerical",

            "Binary Variables",

            "Categorical Variables",

            "Text / Character",

            "Time-Series"

        ],

        "Recommended Treatment":[

            "Mean / Median",

            "Median",

            "Median / Mode",

            "Mode",

            "Mode or 'Unknown'",

            "'Unknown', 'Not Available' or Business Rule",

            "Linear Interpolation / Forward Fill / Backward Fill"

        ]

    })

with st.expander("📊 Comparison of Missing Value Treatment Techniques"):

    st.markdown("""

The following comparison provides a quick overview of the commonly used missing value treatment techniques.

""")

    st.table({

        "Technique":[

            "No Treatment",

            "Delete Rows",

            "Delete Columns",

            "Mean",

            "Median",

            "Mode",

            "KNN",

            "Interpolation",

            "Forward Fill",

            "Backward Fill"

        ],

        "Suitable For":[

            "Initial EDA",

            "Very Few Missing Values",

            "Highly Incomplete Features",

            "Normal Distribution",

            "Skewed Data",

            "Categorical Data",

            "Correlated Numerical Data",

            "Time Series",

            "Sequential Data",

            "Sequential Data"

        ],

        "Complexity":[

            "Low",

            "Low",

            "Low",

            "Low",

            "Low",

            "Low",

            "High",

            "Medium",

            "Low",

            "Low"

        ]

    })

with st.expander("💡 Best Practices & 🚫 Common Mistakes"):

    col1, col2 = st.columns(2)

    # ----------------------------------------------------
    # Best Practices
    # ----------------------------------------------------

    with col1:

        st.success("### 💡 Best Practices")

        st.markdown("""

- 🟢 Understand **why** the data is missing before selecting a treatment.

- 🟢 Never delete rows or columns without evaluating the business impact.

- 🟢 Prefer **Median** over **Mean** when the data is skewed or contains outliers.

- 🟢 Use **Mode** for categorical and binary variables.

- 🟢 For text variables, consider replacing missing values with meaningful labels such as **Unknown**, **Not Available**, or business-specific values.

- 🟢 Compare summary statistics before and after applying any treatment.

- 🟢 Preserve the original dataset whenever possible by working on a copy.

- 🟢 Validate the impact of the chosen treatment using domain knowledge.

""")

    # ----------------------------------------------------
    # Common Mistakes
    # ----------------------------------------------------

    with col2:

        st.error("### 🚫 Common Mistakes")

        st.markdown("""

- ❌ Treating every missing value without understanding its cause.

- ❌ Deleting rows without evaluating the loss of useful information.

- ❌ Dropping important features solely because they contain many missing values.

- ❌ Using **Mean** when extreme outliers are present.

- ❌ Applying the same treatment technique to every variable.

- ❌ Ignoring business rules while imputing missing values.

- ❌ Modifying the original dataset without keeping a backup copy.

- ❌ Assuming one treatment technique works for every project.

""")

with st.expander("🧭 Choosing the Right Treatment"):

    st.markdown("""

### There is no universally correct treatment.

The most appropriate technique depends on several factors rather than a fixed rule.

Before making a decision, consider:

- 🎯 Business Objective

- 📊 Nature of the Data

- 📈 Distribution of the Variable

- 📉 Percentage of Missing Values

- 📂 Importance of the Feature

- 🧠 Domain Knowledge

- 📋 Project Requirements

---

### Remember

The purpose of Exploratory Data Analysis is to understand the data before making decisions.

AutoEDA Studio provides educational guidance and practical recommendations to support your decision-making process.

The final treatment strategy should always align with the business objective, analytical goals and domain expertise.

""")