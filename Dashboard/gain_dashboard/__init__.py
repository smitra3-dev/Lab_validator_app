#dashboard/gain/__init__.py
from Dashboard.gain_dashboard.layout_gain.layout_gain import create_layout_gain
from Dashboard.gain_dashboard.gain_dashboard_backend.filters import register_gain_filter_callbacks
from Dashboard.gain_dashboard.gain_dashboard_backend.plotting import register_gain_plot_callback


def build_gain_dashboard(app, df, meta):
    layout = create_layout_gain(meta)
    register_gain_filter_callbacks(app, df)
    register_gain_plot_callback(app, df)
    return layout


__all__ = ["build_gain_dashboard"]
