"""
Models module for Golden Mile Properties AI Platform.
"""

from src.models.train import PropertyModelTrainer
from src.models.inference import PropertyPricePredictor

__all__ = ['PropertyModelTrainer', 'PropertyPricePredictor']
