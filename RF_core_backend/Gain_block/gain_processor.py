import pandas as pd

from common.grouping_keys import GROUP_COLS
from common.dataframe_utils import sanitize_columns, ensure_columns
from common.numeric_utils import cast_numeric
from common.reference_selector import select_closest_rows

from Gain_block.gain_metric import compute_gain_means
from Gain_block.gain_schema import GAIN_EXCLUDE_COLS, GAIN_PREFERRED_COLS
from Gain_block.gain_formatter import format_gain_output

#updated import 14/04/26
def process_gain_dataframe(df):
    df = sanitize_columns(df)
    df = ensure_columns(df, GROUP_COLS + ["Ft", "Fmax"])
    df = cast_numeric(df, ["Ft", "Fmax"])

    bias_mean = compute_gain_means(df, GROUP_COLS)
    if bias_mean.empty:
        return pd.DataFrame(columns=GROUP_COLS + ["Ft_mean", "Fmax_mean"])

    merged = pd.merge(df, bias_mean, on=GROUP_COLS, how="inner")
    if merged.empty:
        return pd.DataFrame(columns=GROUP_COLS + ["Ft_mean", "Fmax_mean"])

    selected = select_closest_rows(merged, GROUP_COLS, "Ft", "Ft_mean")
    if selected.empty:
        return pd.DataFrame(columns=GROUP_COLS + ["Ft_mean", "Fmax_mean"])

    return format_gain_output(selected, GROUP_COLS, GAIN_PREFERRED_COLS, GAIN_EXCLUDE_COLS)
