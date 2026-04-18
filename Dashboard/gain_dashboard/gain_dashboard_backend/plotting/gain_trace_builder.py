#dashboard/gain/plotting/gain_trace_builder.py

import plotly.graph_objects as go


def add_gain_curve_trace(fig, group, param, keys):
    try:
        m, d, sx, sy, vd_val = keys
    except Exception:
        m = d = sx = sy = vd_val = "NA"

    label = f"{param} | {m} | {d} | ({sx},{sy}) | Vd={vd_val}"

    fig.add_trace(
        go.Scatter(
            x=group["Id"].values,
            y=group[param].values,
            mode="lines+markers",
            name=label,
            line=dict(width=2.2),
            marker=dict(size=5),
            hovertemplate=(
                f"<b>{param}</b><br>"
                f"Macro: {m}<br>"
                f"Device: {d}<br>"
                f"Site: ({sx},{sy})<br>"
                f"Vd: {vd_val}<br>"
                "Id: %{x:.4e}<br>"
                "Value: %{y:.4e}<extra></extra>"
            ),
        )
    )
