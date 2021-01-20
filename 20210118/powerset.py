def ps(arr):

    if len(arr) == 0:
        return [[]]

    current = ps(arr[1:])

    for i in range(len(current)):
        current.append(current[i] + [arr[0]])

    return current


print(ps([1,2,3]))