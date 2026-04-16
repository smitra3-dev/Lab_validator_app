import pandas as pd


def load_excel_sheets(input_file):
    all_sheets = pd.read_excel(input_file, sheet_name=None)
    return all_sheets
