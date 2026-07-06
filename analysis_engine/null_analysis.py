def analyze_null_values(df):

    total_rows = df.shape[0]

    total_columns = df.shape[1]

    total_cells = total_rows * total_columns

    total_missing_cells = df.isnull().sum().sum()

    overall_missing_percentage = (
        (total_missing_cells / total_cells) * 100
        if total_cells > 0 else 0
    )

    return {
        "total_rows": total_rows,
        "total_columns": total_columns,
        "total_cells": total_cells,
        "total_missing_cells": total_missing_cells,
        "overall_missing_percentage": round(overall_missing_percentage, 2)
    }