def longestPeak(array):
    candidate = 0
    current = 0
    new_peak = False
    for i in range(1, len(array) - 1):
        # new candidate
        if array[i - 1] < array[i] > array[i + 1]:
            candidate = 1
            new_peak = True

        j = i - 1
        while j>=0 and new_peak:
            if array[j+1] > array[j]:
                candidate = candidate + 1
            else:
                break
            j = j - 1

        j = i + 1
        while j < len(array) and new_peak:
            if array[j - 1] > array[j]:
                candidate = candidate + 1
            else:
                break
            j = j + 1

        new_peak = False
        current = max(current, candidate)

    return current



# print(longestPeak([1, 3, 2]))
print(longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))