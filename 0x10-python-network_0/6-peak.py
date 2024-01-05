#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers"""
def find_peak_alternative(list_of_integers):
    """Finds a peak in a list of unsorted integers"""
    if not list_of_integers:
        return None

    length = len(list_of_integers)
    if length <= 2:
        return max(list_of_integers)

    start, end = 0, length - 1
    while start <= end:
        middle = (start + end) // 2

        if (middle == 0 or list_of_integers[middle] >= list_of_integers[middle - 1]) and \
           (middle == length - 1 or list_of_integers[middle] >= list_of_integers[middle + 1]):
            return list_of_integers[middle]
        elif middle > 0 and list_of_integers[middle - 1] > list_of_integers[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return None
