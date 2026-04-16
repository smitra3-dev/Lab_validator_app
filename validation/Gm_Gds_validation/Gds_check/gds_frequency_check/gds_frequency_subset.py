#gds_frequency_subset.py
def build_gds_frequency_subset(group, cfg):
    """
    Build the minimum dataframe required for gds frequency checks.
    """
    fs_col = cfg["fs_col"]
    gds_col = cfg["gds_col"]
    ft_cols = [c for c in cfg["ft_candidates"] if c in group.columns]

    required = [fs_col, gds_col]
    if any(col not in group.columns for col in required):
        return None

    return group[required + ft_cols].copy()
