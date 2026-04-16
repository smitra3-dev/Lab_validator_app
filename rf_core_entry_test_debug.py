import os
import pandas as pd
from RF_core_backend.rf_core.rf_main_processor.rf_frequency_processor import process_rf_frequency_dataframe


def process_single_excel_sheet(file_path, sheet_name=0, output_path=None):
    """
    Read one Excel sheet, process it through rf_core, and optionally save output.
    """
    print(f"[INFO] Reading Excel file: {file_path}")
    df = pd.read_excel(file_path, sheet_name=sheet_name)

    print(f"[INFO] Processing RF frequency data...")
    result = process_rf_frequency_dataframe(df)

    if output_path is not None:
        result.to_excel(output_path, index=False)
        print(f"[INFO] Output saved to: {output_path}")

    return result


if __name__ == "__main__":
    # ==========================================================
    # INPUT EXCEL FILE
    # ==========================================================
    file_path = input("Enter Excel file path: ").strip().strip('"')

    if not os.path.exists(file_path):
        print("[ERROR] File not found.")
    else:
        sheet_name = input("Enter sheet name or sheet index (press Enter for first sheet): ").strip()

        if sheet_name == "":
            sheet_name = 0
        else:
            try:
                sheet_name = int(sheet_name)
            except ValueError:
                pass

        output_path = os.path.splitext(file_path)[0] + "_rf_processed.xlsx"

        result = process_single_excel_sheet(
            file_path=file_path,
            sheet_name=sheet_name,
            output_path=output_path
        )

        print("\n[INFO] Processing completed successfully.")
        print(result.head())
