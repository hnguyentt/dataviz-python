"""
Utility functions related to load data, pre-processing data
By: Hoa Nguyen
Last update: May 07, 2020
"""


def txt2list(path):
    """
    Read txt file and parse to list
    :param path: <str> Path to txt file
    :return:
    """
    with open(path) as f:
        lines = f.read().splitlines()

    return lines
