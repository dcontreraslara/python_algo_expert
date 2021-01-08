def firstDuplicateValue(array):

    if len(array) <= 1:
        return -1

    for i in range(len(array)):
        candidate = abs(array[i]) - 1

        print(i, candidate, array)
        if array[candidate] < 0:
            return abs(array[i])
        array[candidate] = -array[candidate]

    return -1



input = [2, 1, 5, 2, 3, 3, 4]
input = [1, 1, 2, 3, 3, 2, 2]
print(firstDuplicateValue(input))
print(firstDuplicateValue([2, 1, 5, 3, 3, 2, 4]))