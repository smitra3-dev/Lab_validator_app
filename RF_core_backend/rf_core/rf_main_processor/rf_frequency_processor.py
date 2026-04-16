from rf_core.rf_column_identifiers.rf_constants import RF_REQUIRED_BASE_COLS, RF_REQUIRED_SPARAM_COLS
from rf_core.rf_column_normalizer.rf_auto_normalizer import auto_detect_and_normalize_rf_input
from rf_core.rf_schema.rf_schema_preparer import prepare_rf_input_schema
from rf_core.rf_column_identifiers.rf_result_builder import build_rf_base_result
from rf_core.rf_schema.rf_row_filter import get_valid_rf_calculation_mask
from rf_core.rf_calculation.rf_sparam_builder import build_sparameters
from rf_core.rf_calculation.rf_yparam_calculator import calculate_yparameters
from rf_core.rf_calculation.rf_metric_pipeline import calculate_all_rf_metrics
from rf_core.rf_calculation.rf_metric_columns import get_rf_metric_output_columns

##updated 13/06/26 subfolder access

def process_rf_frequency_dataframe(df):
    """
    Main enterprise RF frequency processing block.

    Steps:
    1. Auto-detect USA / Singapore input style
    2. Normalize RF input columns
    3. Prepare schema and numeric columns
    4. Build base result dataframe
    5. Filter valid RF rows
    6. Calculate S parameters, Y parameters, and RF metrics
    7. Join calculated outputs back to base result

    Returns
    -------
    pandas.DataFrame
        Final processed RF dataframe
    """

    # ==========================================================
    # STEP 1: INPUT NORMALIZATION
    # ==========================================================
    df, detected_format = auto_detect_and_normalize_rf_input(df)
    print(f"[INFO] Detected RF input format: {detected_format}")

    # ==========================================================
    # STEP 2: PREPARE INPUT SCHEMA
    # ==========================================================
    df = prepare_rf_input_schema(df)

    # ==========================================================
    # STEP 3: BUILD BASE OUTPUT FRAME
    # ==========================================================
    result = build_rf_base_result(df)

    # ==========================================================
    # STEP 4: FIND VALID RF ROWS
    # ==========================================================
    valid_mask = get_valid_rf_calculation_mask(df)

    if not valid_mask.any():
        print("[WARNING] No valid RF rows found for S/Y/Ft/Fmax calculation")
        return result

    work = df.loc[valid_mask, RF_REQUIRED_BASE_COLS + RF_REQUIRED_SPARAM_COLS].copy()

    # ==========================================================
    # STEP 5: CALCULATION PIPELINE
    # ==========================================================
    try:
        work = build_sparameters(work)
        work = calculate_yparameters(work)
        work = calculate_all_rf_metrics(work)

        keep_cols = [
            "S11_comp", "S12_comp", "S21_comp", "S22_comp",
            "S11", "S12", "S21", "S22",
            "S11_dB", "S12_dB", "S21_dB", "S22_dB",
            "Y11_comp", "Y12_comp", "Y21_comp", "Y22_comp",
            "Y11_mag", "Y12_mag", "Y21_mag", "Y22_mag",
            "Y11_dB", "Y12_dB", "Y21_dB", "Y22_dB",
        ] + get_rf_metric_output_columns()

        result.loc[valid_mask, keep_cols] = work[keep_cols].values

    except Exception as e:
        print(f"[WARNING] RF calculation skipped due to: {e}")

    return result
