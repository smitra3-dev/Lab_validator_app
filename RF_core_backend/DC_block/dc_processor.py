import pandas as pd

from common.grouping_keys import GROUP_COLS
from common.dataframe_utils import sanitize_columns, ensure_columns
from common.numeric_utils import cast_numeric
from common.reference_selector import select_closest_rows

from DC_block.dc_reference_merge import merge_dc_reference
from DC_block.dc_schema import DC_EXCLUDE_COLS, DC_PREFERRED_COLS
from DC_block.dc_formatter import format_dc_output


def process_dc_dataframe(primary_df, gain_df):
    primary_df = sanitize_columns(primary_df)
    gain_df = sanitize_columns(gain_df)

    primary_df = ensure_columns(primary_df, GROUP_COLS)
    gain_df = ensure_columns(gain_df, GROUP_COLS)

    if "Ft_mean" not in gain_df.columns:
        return pd.DataFrame(columns=GROUP_COLS + ["Ft_mean"])

    if "Ft" not in primary_df.columns:
        return pd.DataFrame(columns=GROUP_COLS + ["Ft_mean"])

    primary_df = cast_numeric(primary_df, ["Ft"])
    gain_df = cast_numeric(gain_df, ["Ft_mean"])

    merged = merge_dc_reference(primary_df, gain_df, GROUP_COLS)
    if merged.empty:
        return pd.DataFrame(columns=GROUP_COLS + ["Ft_mean"])

    selected = select_closest_rows(merged, GROUP_COLS, "Ft", "Ft_mean")
    if selected.empty:
        return pd.DataFrame(columns=GROUP_COLS + ["Ft_mean"])

    return format_dc_output(selected, GROUP_COLS, DC_PREFERRED_COLS, DC_EXCLUDE_COLS)
