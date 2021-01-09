def maxSubsetSumNoAdjacent(array):
    if len(array) < 1:
        return 0

    if len(array) == 1:
        return array[0]

    using_first = array[0] + maxSubsetSumNoAdjacent(array[2:])
    not_using_first = maxSubsetSumNoAdjacent(array[1:])

    return max(using_first, not_using_first)