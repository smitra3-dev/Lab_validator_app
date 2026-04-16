# Freq region splitter 
def split_by_fnqs(df, fnqs):
    """
    Split dataframe into LF and HF using dynamic fnqs boundary.
    """
    lf = df[df["__fs__"] <= fnqs].copy()
    hf = df[df["__fs__"] > fnqs].copy()
    return lf, hf


def split_by_absolute_limits(df, lf_fs_abs_max, hf_fs_abs_min):
    """
    Split dataframe into LF and HF using absolute configured limits.
    """
    lf = df[df["__fs__"] <= lf_fs_abs_max].copy()
    hf = df[df["__fs__"] >= hf_fs_abs_min].copy()
    return lf, hf
