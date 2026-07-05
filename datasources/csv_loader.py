import pandas as pd


def load_csv(uploaded_file):
    """
    Reads an uploaded CSV file
    and returns a Pandas DataFrame.
    """
    return pd.read_csv(uploaded_file)