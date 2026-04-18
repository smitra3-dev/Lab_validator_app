#data/dataset_detector.py
import os
import glob


def _detect_latest_folder_by_suffix(suffix):
    base_path = os.getcwd()
    folders = [
        f for f in glob.glob(os.path.join(base_path, "**", f"*_{suffix}"), recursive=True)
        if os.path.isdir(f)
    ]
    folders.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    return folders


def detect_gain_folders():
    return _detect_latest_folder_by_suffix("GAIN")


def detect_rf_folder():
    folders = _detect_latest_folder_by_suffix("RF")
    return folders[0] if folders else None


def detect_dc_folder():
    folders = _detect_latest_folder_by_suffix("DC")
    return folders[0] if folders else None
