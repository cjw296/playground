"""
This is  module.
"""
from sys import version_info


def version_happiness():
    """
    This is version happiness...
    """
    if version_info.major == 2:
        return ':-('
    else:
        return ':-)'
