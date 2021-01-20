def mergeSortedArrays(arrays):
    current_idx = [0 for _ in arrays]
    length = sum([len(x) for x in arrays])
    import sys
    output = []
    while len(output) < length:
        current_min = -1, sys.maxsize
        for i in range(len(arrays)):
            if current_idx[i] < len(arrays[i]) and arrays[i][current_idx[i]] < current_min[1]:
                current_min = i, arrays[i][current_idx[i]]

        current_idx[current_min[0]] += 1
        output.append(current_min[1])
    return output

