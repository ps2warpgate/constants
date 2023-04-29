"""Common files used across ps2warpgate projects."""

from .logformatter import CustomFormatter
from .isdocker import is_docker

__all__ = [
    'CustomFormatter',
    'is_docker'
]

__author__ = 'wupasscat'
__version__ = '1.0.0'
