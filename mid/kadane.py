def kadanesAlgorithm(array):
    import sys
    current_max = -sys.maxsize
    current_sum = 0

    for i in array:
        partial_sum = current_sum + i
        if i > partial_sum:
            current_sum = i
        else:
            current_sum = partial_sum
        current_max = max(current_max, current_sum)
        # print(partial_sum, current_sum, current_max)

    return max(current_max, current_sum)



print(kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))