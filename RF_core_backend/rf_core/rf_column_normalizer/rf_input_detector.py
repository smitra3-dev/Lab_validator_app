from rf_core.rf_helper.rf_column_utils import clean_column_names

#updated 13/4/26 subfolder access

def detect_rf_input_format(df) -> str:
    out = clean_column_names(df)
    cols = [str(c).strip() for c in out.columns]

    has_usa_pattern = ("loopBias" in cols) or ("loopHeadConstants" in cols)
    has_sg_pattern = ("vd`" in cols) or ("vg`" in cols)

    if has_usa_pattern and not has_sg_pattern:
        return "usa"
    if has_sg_pattern and not has_usa_pattern:
        return "singapore"
    if has_usa_pattern and has_sg_pattern:
        return "singapore"

    return "unknown"
