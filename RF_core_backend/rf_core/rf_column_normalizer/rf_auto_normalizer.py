from rf_core.rf_helper.rf_column_utils import clean_column_names
from rf_core.rf_column_normalizer.rf_input_detector import detect_rf_input_format
from rf_core.rf_column_normalizer.rf_normalizer_singapore import normalize_singapore_rf_columns
from rf_core.rf_column_normalizer.rf_normalizer_usa import normalize_usa_rf_columns

#updated 13/06/26 subfolder access

def auto_detect_and_normalize_rf_input(df):
    out = clean_column_names(df)
    detected_format = detect_rf_input_format(out)

    if detected_format == "usa":
        out = normalize_usa_rf_columns(out)

    elif detected_format == "singapore":
        out = normalize_singapore_rf_columns(out)

    else:
        temp = normalize_singapore_rf_columns(out.copy())

        need_usa_fallback = (
            ("Vd" not in temp.columns or temp["Vd"].isna().all()) or
            ("Vg" not in temp.columns or temp["Vg"].isna().all())
        )

        if need_usa_fallback:
            temp = normalize_usa_rf_columns(temp)

        out = temp

    return out, detected_format
