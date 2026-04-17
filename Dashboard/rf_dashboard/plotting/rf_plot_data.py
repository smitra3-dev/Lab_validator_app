##plotting/rf_plot_data.py
def prepare_rf_plot_dataframe(filtered):
    pdf = filtered.collect().to_pandas()

    if pdf.empty:
        return None, "No data found"

    if "Fs" in pdf.columns:
        pdf = pdf[pdf["Fs"] > 0]

    if pdf.empty:
        return None, "No valid frequency data found"

    return pdf, None


def normalize_selected_params(params):
    if not params:
        return []

    if isinstance(params, str):
        return [params]

    return list(params)


def find_valid_rf_params(pdf, params):
    params = normalize_selected_params(params)
    return [p for p in params if p in pdf.columns]
