#!/usr/bin/python3
""" Function test """
find_peak = __import__('6-peak').find_peak

print(find_peak([1, 2, 4, 6, 3, 2, 3, 4]))
print(find_peak([4, 2, 1, 2, 3, 3, 2, 1]))
print(find_peak([2, 3, 3, 1, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 3, 2, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 3, 3, 3, 1, 2, 3, 1]))
