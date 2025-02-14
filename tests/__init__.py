# src/setlogging/__init__.py

from src.setlogging.logger import CustomFormatter, setup_logging, get_logger

__version__ = "0.3.5"
__author__ = "Jie Yan"
__email__ = "kiki3890528@gmail.com"

__all__ = [
    "CustomFormatter",
    "setup_logging",
    "get_logger",
]
