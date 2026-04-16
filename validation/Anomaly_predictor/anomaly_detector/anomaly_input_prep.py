#anomaly_input_prep
import pandas as pd


def prepare_anomaly_dataframe(df, x_col, y_col):
    """
    Sort and clean dataframe for anomaly detection.
    """
    if x_col not in df.columns or y_col not in df.columns:
        return None

    temp = df[[x_col, y_col]].copy()
    temp = temp.dropna(subset=[x_col, y_col])
    temp = temp.sort_values(x_col).reset_index(drop=True)

    if len(temp) == 0:
        return None

    return temp
