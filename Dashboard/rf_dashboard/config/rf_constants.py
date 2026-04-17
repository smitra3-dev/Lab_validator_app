##config/rf_constants.py
RF_GROUP_COLS = ["macro", "device", "siteX", "siteY", "Vd", "Vg"]

RF_SPARAM_PARAMS = {
    "S11_dB", "S12_dB", "S21_dB", "S22_dB",
}

RF_H21_PARAMS = {"h21_dB"}

RF_CAP_PARAMS = {"Cgs", "Cgd", "Cgg"}

RF_FTFMAX_PARAMS = {"Ft_mean", "Ft", "Fmax", "Fmax_mean"}

RF_GENERIC_EXCLUDE_PARAMS = RF_FTFMAX_PARAMS
