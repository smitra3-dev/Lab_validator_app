#dashboard/gain/plotting/gain_plot_data.py

def prepare_gain_plot_dataframe(filtered):
    pdf = filtered.collect().to_pandas()

    if pdf.empty:
        return None, "No data found"

    if "Id" in pdf.columns:
        pdf["Id"] = pdf["Id"].astype(float)

    pdf = pdf.dropna(subset=["Id"])

    if pdf.empty:
        return None, "No valid Id data found"

    return pdf, None


def normalize_selected_params(params):
    if not params:
        return []
    if isinstance(params, str):
        return [params]
    return list(params)


def find_valid_gain_params(pdf, params):
    params = normalize_selected_params(params)
    return [p for p in params if p in pdf.columns]
