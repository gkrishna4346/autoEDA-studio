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

st.subheader("📈 Distribution Analysis")

st.write("""
Understand how numerical values are distributed across the dataset.
This helps identify data spread, central tendency, skewness and
potential anomalies before building machine learning models.
""")

st.write("""
The following analyses will be performed independently for each
variable in the dataset.
""")

st.markdown("""
- 📉 Histogram
- 📦 Box Plot
- 📐 Skewness Analysis
- 📏 Kurtosis Analysis
- 🔢 Frequency Distribution
- 📋 Value Counts
""")


st.divider()



import matplotlib.pyplot as plt

st.header("📊 Distribution Analysis")

numeric_columns = df.select_dtypes(include="number").columns.tolist()

selected_columns = st.multiselect(
    "Select numerical variables",
    numeric_columns,
    default=st.session_state.get("distribution_columns", [])
)

st.session_state.distribution_columns = selected_columns

if st.button("Generate Analysis"):

    for column in selected_columns:

        st.divider()

        st.subheader(f"{column}")

        col1, gap1, col2, gap2, col3 = st.columns([4, .1, 4,.3, 3])

        # ==========================================
        # Calculate Statistics (Only Once)
        # ==========================================

        mean = df[column].mean()

        median = df[column].median()

        mode = df[column].mode().iloc[0]

        std = df[column].std()

        skewness = df[column].skew()

        kurtosis = df[column].kurt()

        q1 = df[column].quantile(0.25)

        q3 = df[column].quantile(0.75)

        iqr = q3 - q1

        lower = q1 - (1.5 * iqr)

        upper = q3 + (1.5 * iqr)

        outliers = (
            (df[column] < lower) |
            (df[column] > upper)
        ).sum()

        outlier_percentage = (
            outliers /
            df[column].dropna().shape[0]
        ) * 100

        # Distribution

        if abs(skewness) < 0.5:
            distribution = "Approximately Symmetric"
        elif skewness > 0:
            distribution = "Right Skewed"
        else:
            distribution = "Left Skewed"

        # Kurtosis

        if kurtosis > 0.5:
            kurtosis_type = "Leptokurtic"
        elif kurtosis < -0.5:
            kurtosis_type = "Platykurtic"
        else:
            kurtosis_type = "Mesokurtic"

        # --------------------------------------------------
        # COLUMN 1 - HISTOGRAM
        # --------------------------------------------------

        with col1:
            st.markdown(
                "<h3 style='text-align:center;'>Histogram</h3>",
                unsafe_allow_html=True
            )

            fig, ax = plt.subplots(
                figsize=(6, 4)
            )

            ax.hist(
                df[column].dropna(),
                bins=20,
                edgecolor="black"
            )

            # Mean Line
            ax.axvline(
                mean,
                color="red",
                linestyle="--",
                linewidth=2,
                label=f"Mean = {mean:.2f}"
            )

            ax.set_xlabel(column)

            ax.set_ylabel("Frequency")

            ax.legend()

            plt.tight_layout()

            st.pyplot(fig)

        # --------------------------------------------------
        # COLUMN 2 - BOX PLOT
        # --------------------------------------------------

        with col2:

            st.markdown(
                "<h3 style='text-align:center;'>Box Plot</h3>",
                unsafe_allow_html=True
            )

            fig, ax = plt.subplots(
                figsize=(6, 4)
            )

            ax.boxplot(
                df[column].dropna(),
                vert=False,
                patch_artist=True
            )

            # Mean Marker
            ax.scatter(
                mean,
                1,
                color="red",
                marker="D",
                s=60,
                label=f"Mean = {mean:.2f}",
                zorder=3
            )

            ax.set_xlabel(column)

            ax.legend()

            plt.tight_layout()

            st.pyplot(fig)


        # --------------------------------------------------
        # COLUMN 3 - STATISTICAL KEY CALL-OUTS
        # --------------------------------------------------

        with col3:

            st.subheader("Statistical Key Call-outs")


            # --------------------------------------------------
            # Outlier Calculation (IQR Method)
            # --------------------------------------------------

            q1 = df[column].quantile(0.25)
            q3 = df[column].quantile(0.75)

            iqr = q3 - q1

            lower = q1 - (1.5 * iqr)
            upper = q3 + (1.5 * iqr)

            outliers = (
                (df[column] < lower) |
                (df[column] > upper)
            ).sum()

            outlier_percentage = (
                outliers /
                df[column].dropna().shape[0]
            ) * 100

            # --------------------------------------------------
            # Display Function
            # --------------------------------------------------

            def stat_row(label, value):

                left, right = st.columns([.5, 1])

                with left:
                    st.markdown(f"**{label}**")

                with right:
                    st.write(value)

            # --------------------------------------------------
            # Display Statistics
            # --------------------------------------------------

            stat_row("Mean", f"{mean:.2f}")

            stat_row("Median", f"{median:.2f}")

            stat_row("Mode", f"{mode:.2f}")

            stat_row("Std Deviation", f"{std:.2f}")

            stat_row("Skewness", f"{skewness:.2f}")

            stat_row("Distribution", distribution)

            stat_row(
                "Kurtosis",
                f"{kurtosis:.2f} ({kurtosis_type})"
            )

            stat_row(
                "Outliers",
                f"{outliers} ({outlier_percentage:.2f}%)"
            )






# st.info("ℹ️ Univariate Analysis visualizations will be available in the next release.")

# -------




# -----
st.divider()

left, middle, right = st.columns([1, 8, 1])

with left:
    if st.button("◀ Previous"):
        st.switch_page("pages/3_Duplicate_Row_Analysis.py")

with right:
    if st.button("Next ▶︎"):
        st.switch_page("pages/5_Outlier_Analysis.py")

st.divider()

st.markdown(
    "<div style='text-align: center; color: gray; font-size: 14px;'>"
    "AutoEDA Studio • Built by Gopikrishna"
    "</div>",
    unsafe_allow_html=True
)