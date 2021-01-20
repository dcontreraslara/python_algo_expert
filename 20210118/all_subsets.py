def subsets(arr):

    if len(arr) == 0:
        return [[]]

    out = []
    for i in range(len(arr)):
        value = arr[i]
        gap = arr[:i] + arr[i+1:]

        for elem in subsets(gap):
            out.append(elem + [value])

    return out


print(subsets([1,2,3]))
print(subsets([]))
