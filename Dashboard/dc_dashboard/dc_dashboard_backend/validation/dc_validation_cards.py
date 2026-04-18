##dashboard/dc/validation/dc_validation_cards.py

from dash import html


def build_dc_validation_card(param, keys, lines, color):
    try:
        m, d, sx, sy, vd_val = keys
    except Exception:
        m = d = sx = sy = vd_val = "NA"

    return html.Div(
        children=[
            html.Div(f"Parameter : {param}", style={"fontWeight": "bold"}),
            html.Div(f"Macro : {m}"),
            html.Div(f"Device : {d}"),
            html.Div(f"SiteX : {sx}"),
            html.Div(f"SiteY : {sy}"),
            html.Div(f"Vd : {vd_val}"),
            *lines,
        ],
        style={
            "border": "1px solid #ccc",
            "borderRadius": "6px",
            "padding": "10px",
            "marginBottom": "10px",
            "backgroundColor": "#fafafa",
            "borderLeft": f"5px solid {color}",
            "fontSize": "12px",
            "lineHeight": "1.5",
        },
    )
