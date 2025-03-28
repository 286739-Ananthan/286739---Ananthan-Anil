# ***************************************************************************************************************************************************
#  *Author           : Ananthan.A - 286739
#  *File             : __init__.py
#  *Title            : Python String Operations Module Development
#  *Description      : python package
#  ****************************************************************************************************************************************************

# Import all functions from the main module
from strops import (
    getspan,
    reverseWords,
    removePunctuation,
    countWords,
    characterMap,
    makeTitle,
    normalizeSpaces,
    transform,
    getPermutations
)

# Package metadata
__version__ = "0.1"
__author__ = "Ananthan.A"
__email__ = "ananthan.a@ust.com"
__license__ = "MIT"

# Explicit exports for 'from strops import *'
__all__ = [
    'getspan',
    'reverseWords',
    'removePunctuation',
    'countWords',
    'characterMap',
    'makeTitle',
    'normalizeSpaces',
    'transform',
    'getPermutations'
]

# Compatibility initialization
if __name__ == "__main__":
    print(f"strops v{__version__} - String operations package")
