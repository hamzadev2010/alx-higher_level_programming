#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    """find the peak of the list
    """
    peak = None
    for ele in list_of_integers:
        if peak is None or peak < ele:
            peak = ele
    return peak
