def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while low <= high:
        if array[high] > pivot:
            high = high - 1
        elif array[low] <= pivot:
            low = low + 1
        else:
            array[low], array[high] = array[high], array[low]

    array[start], array[high] = array[high], array[start]
    print(low, high)
    return high


def quickSort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1

    if start >= end:
        return array

    p = partition(array, start, end)
    quickSort(array, start, p - 1)
    quickSort(array, p + 1, end)
    return array



