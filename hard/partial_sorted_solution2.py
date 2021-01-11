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

    min_found = array[found_idx]
    max_found = array[found_idx-1]
    start_idx, end_idx, i = found_idx, found_idx, found_idx

    print(start_idx, end_idx)
    while i < len(array):
        while start_idx > 0 and min_found < array[start_idx-1]:
            start_idx = start_idx - 1

        if max_found > array[i]: # unsorted
            end_idx = i
        else:
            max_found = array[i]

        if min_found > array[i]: # unsorted
            min_found = array[i]
            continue
        i = i + 1

    return [start_idx, end_idx]









# print(subarraySort([2,1]))
# print(subarraySort([1,2]))
# print(subarraySort([1,2,3,5,3,7,3,10,6,11]))
# print(subarraySort([3,2,1]))
# print(subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 7, 7, 16, 18, 19]))
print(subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))
# print(subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 13, 14, 16, 18, 19]))
# print(subarraySort([4, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 11, 57]))