# __init__.py
from .module import greet
from .utils import add

__version__ = '1.0.0'
__doc__ = 'Это пакет, который содержит...'
__author__ = 'John'
__all__ = ['greet', 'add']  # для импорта со *
