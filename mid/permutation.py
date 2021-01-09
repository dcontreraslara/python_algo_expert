def getPermutations(array):
    if len(array) == 0:
        return []

    if len(array) == 1:
        return [array]

    out = []
    for i in range(len(array)):
        num = array[i]
        other = array[:i] + array[i + 1:]

        for elem in getPermutations(other):
            out.append([num] + elem)

    return out


print(getPermutations([1,2,3]))