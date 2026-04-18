import webbrowser
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from data_finder.dataset_detector import (
    detect_gain_folders,
    detect_rf_folder,
    detect_dc_folder,
)
from data_finder.parquet_loader import (
    load_gain_parquet_folders,
    load_parquet_folder,
)

from Dashboard.gain_dashboard import build_gain_dashboard
from Dashboard.rf_dashboard import build_rf_dashboard
from Dashboard.dc_dashboard import build_dc_dashboard


# ==========================================================
# DASHBOARD FACTORIES
# ==========================================================
def create_gain_dashboard(app):
    gain_folders = detect_gain_folders()
    df, meta = load_gain_parquet_folders(gain_folders)

    if df is None or meta is None:
        return html.Div("No parquet files found in *_GAIN folders.")

    return build_gain_dashboard(app, df, meta)


def create_rf_dashboard(app):
    rf_folder = detect_rf_folder()
    df, meta = load_parquet_folder(rf_folder)

    if df is None or meta is None:
        return html.Div("No RF dataset found.")

    return build_rf_dashboard(app, df, meta)


def create_dc_dashboard(app):
    dc_folder = detect_dc_folder()
    df, meta = load_parquet_folder(dc_folder)

    if df is None or meta is None:
        return html.Div("No DC dataset found.")

    return build_dc_dashboard(app, df, meta)


# ==========================================================
# CREATE APP
# ==========================================================
def create_app():
    app = Dash(__name__, suppress_callback_exceptions=True)

    gain_layout = create_gain_dashboard(app)
    rf_layout = create_rf_dashboard(app)
    dc_layout = create_dc_dashboard(app)

    app.layout = html.Div(
        className="app-shell",
        children=[
            html.H1("Unified Dashboard", className="app-title"),
            dcc.Tabs(
                id="tabs",
                value="gain",
                children=[
                    dcc.Tab(label="Current Dashboard", value="gain"),
                    dcc.Tab(label="Frequency Dashboard", value="rf"),
                    dcc.Tab(label="Bias Dashboard", value="dc"),
                ],
            ),
            html.Div(id="tabs-content"),
        ],
    )

    @app.callback(
        Output("tabs-content", "children"),
        Input("tabs", "value"),
    )
    def render_content(tab):
        if tab == "gain":
            return gain_layout
        if tab == "rf":
            return rf_layout
        if tab == "dc":
            return dc_layout
        return html.Div("Select a dashboard.")

    return app


# ==========================================================
# RUN SERVER
# ==========================================================
if __name__ == "__main__":
    app = create_app()
    url = "http://127.0.0.1:8050/"
    webbrowser.open(url)
    app.run(debug=False, host="127.0.0.1", port=8050)
