def ps(array):
    if len(array) == 0:
        return [[]]

    current = ps(array[:-1])
    for i in range(len(current)):
        current.append(current[i] + [array[len(array)-1]])

    return current

print(ps([1,2]))