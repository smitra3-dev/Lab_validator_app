#dashboard/rf/__init__.py

from Dashboard.rf_dashboard.layout_rf.layout_rf import create_layout
from Dashboard.rf_dashboard.rf_dashboard_backend.filters import register_rf_filter_callbacks
from Dashboard.rf_dashboard.rf_dashboard_backend.plotting import register_rf_plot_callback
from Dashboard.rf_dashboard.rf_dashboard_backend.config.rf_params import get_rf_params


def build_rf_dashboard(app, df, meta):
    rf_params = get_rf_params()
    layout = create_layout(meta, rf_params)
    register_rf_filter_callbacks(app, df)
    register_rf_plot_callback(app, df)
    return layout


__all__ = ["build_rf_dashboard"]
