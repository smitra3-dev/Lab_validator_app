#__init__
from .trend_detector import detect_trend
from .trend_predictor import predict_trend

__all__ = [
    "detect_trend",
    "predict_trend",
]
