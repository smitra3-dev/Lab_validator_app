import os
import re


def generate_output_folders(input_file):
    base = os.path.basename(input_file)
    name, _ = os.path.splitext(base)

    match = re.search(r"(part\d+)", name, re.IGNORECASE)

    if match:
        part = match.group(1)
        prefix = name.replace(f"_{part}", "")
    else:
        part = "full"
        prefix = name

    rf_folder = f"{prefix}_{part}_RF"
    gain_folder = f"{prefix}_{part}_GAIN"
    dc_folder = f"{prefix}_{part}_DC"

    return rf_folder, gain_folder, dc_folder
