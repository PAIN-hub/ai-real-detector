"""
AI Real Detector
----------------
A lightweight package to detect whether an image is AI-generated or real.
Includes model-based prediction and metadata analysis.

Usage:
    from ai_real_detector import predict, analyze_metadata
"""

from .predictor import predict
from .metadata import analyze_metadata
from .model_loader import get_model

__all__ = ["predict", "analyze_metadata", "get_model"]

__version__ = "0.1.0"