
import pandas as pd

def generate_metadata(df):
    rows, columns = df.shape
    numeric_columns = len(
        df.select_dtypes(include="number").columns
    )
    categorical_columns = len(
        df.select_dtypes(include=["object", "category"]).columns
    )
    datetime_columns = len(
        df.select_dtypes(include="datetime").columns
    )
    boolean_columns = len(
        df.select_dtypes(include="bool").columns
    )
    missing_values = int(df.isnull().sum().sum())
    duplicate_rows = int(df.duplicated().sum())
    memory_usage = round(
        df.memory_usage(deep=True).sum() / 1024,
        2
    )

    return {
        "rows": rows,
        "columns": columns,
        "numeric_columns": numeric_columns,
        "categorical_columns": categorical_columns,
        "datetime_columns": datetime_columns,
        "boolean_columns": boolean_columns,
        "missing_values": missing_values,
        "duplicate_rows": duplicate_rows,
        "memory_usage_kb": memory_usage
    }