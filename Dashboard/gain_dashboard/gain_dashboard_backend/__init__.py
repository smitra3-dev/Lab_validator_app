#dashboard/gain/__init__.py

from .filters import register_gain_filter_callbacks
from .plotting import register_gain_plot_callback

__all__ = [
    "register_gain_filter_callbacks",
    "register_gain_plot_callback",
]
