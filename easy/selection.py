def selectionSort(array):
    import sys
    for i in range(len(array)):
        midx = i

        for j in range(i + 1, len(array)):
            if array[midx] > array[j]:
                midx = j

        array[i], array[midx] = array[midx], array[i]

    return array
