import time
from concurrent.futures import ProcessPoolExecutor, as_completed

from pipeline.pipeline_worker.output_naming import generate_output_folders
from pipeline.parquet_operation.loader.excel_loader import load_excel_sheets
from pipeline.pipeline_worker.sheet_worker import process_full_pipeline
from pipeline.parquet_operation.parquet_writer_worker.parquet_writer import save_parquet_dict

#updated 14/04/26


def run_pipeline(input_file, max_workers=None):
    start = time.time()

    print("\n================ RF PIPELINE START ================\n")

    rf_folder, gain_folder, dc_folder = generate_output_folders(input_file)

    print(f"Input File : {input_file}")
    print(f"RF Folder : {rf_folder}")
    print(f"Gain Folder : {gain_folder}")
    print(f"DC Folder : {dc_folder}\n")

    all_sheets = load_excel_sheets(input_file)
    print(f"Found {len(all_sheets)} sheets\n")

    rf_results = {}
    gain_results = {}
    dc_results = {}

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = [
            executor.submit(process_full_pipeline, name, df)
            for name, df in all_sheets.items()
        ]

        for future in as_completed(futures):
            try:
                sheet, rf_df, gain_df, dc_df = future.result()
            except Exception as e:
                print(f"[PIPELINE ERROR] Worker failed: {e}")
                continue

            rf_results[sheet] = rf_df
            gain_results[sheet] = gain_df
            dc_results[sheet] = dc_df

            print(f"Completed: {sheet}")

    print("\nSaving Parquet datasets...\n")

    save_parquet_dict(rf_results, rf_folder)
    save_parquet_dict(gain_results, gain_folder)
    save_parquet_dict(dc_results, dc_folder)

    end = time.time()

    print("\n================ PIPELINE COMPLETE ================\n")
    print(f"Total Runtime: {round(end - start, 2)} seconds\n")

    return rf_folder, gain_folder, dc_folder
