##validation/rf_validation_cards.py
from dash import html


def build_validation_card(param, keys, lines, color):
    try:
        macro_v, device_v, siteX_v, siteY_v, vd_v, vg_v = keys
    except Exception:
        macro_v = device_v = siteX_v = siteY_v = vd_v = vg_v = "NA"

    header = [
        html.Div(f"Parameter : {param}", style={"fontWeight": "bold"}),
        html.Div(f"Macro : {macro_v}"),
        html.Div(f"Device : {device_v}"),
        html.Div(f"SiteX : {siteX_v}"),
        html.Div(f"SiteY : {siteY_v}"),
        html.Div(f"Vd : {vd_v}"),
        html.Div(f"Vg : {vg_v}"),
    ]

    return html.Div(
        children=header + lines,
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
