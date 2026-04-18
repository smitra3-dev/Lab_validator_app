##dashboard/dc/plotting/dc_plot_data.py
def prepare_dc_plot_dataframe(filtered):
    pdf = filtered.collect().to_pandas()

    if pdf.empty:
        return None, "No data found"

    if "Vg" in pdf.columns:
        pdf["Vg"] = pdf["Vg"].astype(float)

    pdf = pdf.dropna(subset=["Vg"])

    if pdf.empty:
        return None, "No valid Vg data found"

    return pdf, None


def normalize_selected_params(params):
    if not params:
        return []

    if isinstance(params, str):
        return [params]

    return list(params)


def find_valid_dc_params(pdf, params):
    params = normalize_selected_params(params)
    return [p for p in params if p in pdf.columns]

