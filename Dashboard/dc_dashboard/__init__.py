#dashboard/dc/__init__.py

from Dashboard.dc_dashboard.layout_dc.layout_dc import create_layout_dc
from Dashboard.dc_dashboard.dc_dashboard_backend.filters import register_dc_filter_callbacks
from Dashboard.dc_dashboard.dc_dashboard_backend.plotting import register_dc_plot_callback


def build_dc_dashboard(app, df, meta):
    layout = create_layout_dc(meta)
    register_dc_filter_callbacks(app, df)
    register_dc_plot_callback(app, df)
    return layout


__all__ = ["build_dc_dashboard"]
