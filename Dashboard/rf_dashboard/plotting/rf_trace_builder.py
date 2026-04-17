##plotting/rf_trace_builder.py
import plotly.graph_objects as go


def build_rf_curve_label(param, keys):
    try:
        macro_k, device_k, siteX_k, siteY_k, vd_k, vg_k = keys
    except Exception:
        macro_k = device_k = siteX_k = siteY_k = vd_k = vg_k = "NA"

    return f"{param} | {macro_k} | {device_k} | ({siteX_k},{siteY_k}) | Vd={vd_k}, Vg={vg_k}"


def add_rf_curve_trace(fig, group, param, keys):
    label = build_rf_curve_label(param, keys)

    try:
        macro_k, device_k, siteX_k, siteY_k, vd_k, vg_k = keys
    except Exception:
        macro_k = device_k = siteX_k = siteY_k = vd_k = vg_k = "NA"

    fig.add_trace(go.Scatter(
        x=group["Fs"].values,
        y=group[param].values,
        mode="lines+markers",
        name=label,
        line=dict(width=2.2),
        marker=dict(size=5),
        hovertemplate=(
            f"<b>{param}</b><br>"
            f"Macro: {macro_k}<br>"
            f"Device: {device_k}<br>"
            f"Site: ({siteX_k},{siteY_k})<br>"
            f"Vd: {vd_k}<br>"
            f"Vg: {vg_k}<br>"
            "Fs: %{x:.4g}<br>"
            "Value: %{y:.4e}<extra></extra>"
        ),
    ))
