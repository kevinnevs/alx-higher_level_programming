#!/usr/bin/python3

"""
function that finds a peak in a list of unsorted integers
"""
def find_peak(list_of_integers):
    """
    first or last element is peak element
    """
    n = len(list_of_integers)
    arr = list_of_integers
    if not arr:
        return None
    if (n==1):
        return arr[0]
    if (arr[0] >= arr[1]):
        return arr[0]
    if (arr[n-1] >= arr[n-2]):
        return arr[n-1]
    """
    check for every other element
    """
    for i in range (1, n-1):
        """
        check if the neighbour are smaller
        """
        if (arr[i] >= arr[i-1] and arr[i] >= arr[i+1]):
            return i
