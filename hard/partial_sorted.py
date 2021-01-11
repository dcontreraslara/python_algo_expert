import sys
def subarraySort(array):

    previous = array[0]
    found_idx = -1

    for i in range(1, len(array)):
        if previous <= array[i]:
            previous = array[i]
            continue

        found_idx = i
        break

    if found_idx == - 1:
        return [found_idx, found_idx]

    i = found_idx
    start_idx, end_idx, last_max = found_idx, found_idx, array[i-1]

    while i < len(array):
        pivot = array[start_idx]
        while start_idx > 0 and pivot < array[start_idx-1]:
            start_idx = start_idx - 1

        previous = array[i]
        while i < len(array):
            if array[i] > last_max and previous <= array[i]:
                last_max = max(array[i], last_max)
                previous = array[i]
                i = i + 1
                continue

            end_idx = i
            candidate_start = i
            while start_idx > 0 and array[candidate_start] < array[start_idx-1]:
                start_idx = start_idx - 1

            # start_idx = min(candidate_start, start_idx)

            i = i + 1
        break

    return [start_idx, end_idx]









print(subarraySort([2,1]))
# print(subarraySort([1,2]))
# print(subarraySort([1,2,3,5,3,7,3,10,6,11]))
# print(subarraySort([3,2,1]))
# print(subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 7, 7, 16, 18, 19]))
print(subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))
# print(subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 13, 14, 16, 18, 19]))
# print(subarraySort([4, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 11, 57]))