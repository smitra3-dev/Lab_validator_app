def build_gm_frequency_subset(group, cfg):

    "Temporary df for gm freq check"
    
    fs_col = cfg["fs_col"]
    gm_col = cfg["gm_col"]
    ft_cols = [c for c in cfg["ft_candidates"] if c in group.columns]

    required = [fs_col, gm_col]
    if any(col not in group.columns for col in required):
        return None

    return group[required + ft_cols].copy()
