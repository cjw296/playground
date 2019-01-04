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
    elif version_info.minor <=6:
        return ':-|'
    else:
        return ':-)'
