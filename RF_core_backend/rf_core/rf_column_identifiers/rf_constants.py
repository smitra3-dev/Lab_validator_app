RF_REQUIRED_BASE_COLS = [
    "technology", "wafer", "macro", "device",
    "siteX", "siteY", "Vd", "Vg", "Id", "Ig", "Fs"
]

RF_REQUIRED_SPARAM_COLS = [
    "S11R", "S11I", "S12R", "S12I",
    "S21R", "S21I", "S22R", "S22I"
]

RF_NUMERIC_BASE_COLS = ["Vd", "Vg", "Fs", "Id", "Ig"]

RF_SINGAPORE_RENAME_MAP = {
    "vd`": "Vd",
    "vg`": "Vg",
    "Fs`": "Fs",
    "id": "Id",
    "ig": "Ig",
}

RF_USA_FALLBACK_RENAME_MAP = {
    "Fs`": "Fs",
    "vg`": "Vg",
    "vd`": "Vd",
    "id": "Id",
    "ig": "Ig",
}

RF_Z0 = 50.0
RF_TINY = 1e-30
