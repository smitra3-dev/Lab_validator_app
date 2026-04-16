import pandas as pd

from rf_core.rf_main_processor.rf_frequency_processor import process_rf_frequency_dataframe
from Gain_block.gain_processor import process_gain_dataframe
from DC_block.dc_processor import process_dc_dataframe

#Updated reference import 14/04/26

def process_full_pipeline(sheet_name, df):
    print(f"Processing Sheet: {sheet_name}")

    try:
        rf_df = process_rf_frequency_dataframe(df)
        print(f"[DEBUG RF] {sheet_name} columns:")
        print(rf_df.columns.tolist())
    except Exception as e:
        print(f"[RF ERROR] {sheet_name}: {e}")
        rf_df = pd.DataFrame()

    try:
        gain_df = process_gain_dataframe(rf_df) if not rf_df.empty else pd.DataFrame()
        print(f"[DEBUG GAIN] {sheet_name} columns:")
        print(gain_df.columns.tolist())
    except Exception as e:
        print(f"[GAIN ERROR] {sheet_name}: {e}")
        gain_df = pd.DataFrame()

    try:
        dc_df = process_dc_dataframe(rf_df, gain_df) if (not rf_df.empty and not gain_df.empty) else pd.DataFrame()
        print(f"[DEBUG DC] {sheet_name} columns:")
        print(dc_df.columns.tolist())
    except Exception as e:
        print(f"[DC ERROR] {sheet_name}: {e}")
        dc_df = pd.DataFrame()

    return sheet_name, rf_df, gain_df, dc_df






'''
def process_full_pipeline(sheet_name, df):
    print(f"Processing Sheet: {sheet_name}")

    try:
        rf_df = process_rf_frequency_dataframe(df)
    except Exception as e:
        print(f"[RF ERROR] {sheet_name}: {e}")
        rf_df = pd.DataFrame()

    try:
        gain_df = process_gain_dataframe(rf_df) if not rf_df.empty else pd.DataFrame()
    except Exception as e:
        print(f"[GAIN ERROR] {sheet_name}: {e}")
        gain_df = pd.DataFrame()

    try:
        dc_df = process_dc_dataframe(rf_df, gain_df) if (not rf_df.empty and not gain_df.empty) else pd.DataFrame()
    except Exception as e:
        print(f"[DC ERROR] {sheet_name}: {e}")
        dc_df = pd.DataFrame()

    return sheet_name, rf_df, gain_df, dc_df
'''