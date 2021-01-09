def powerset(array, i = None):
    if i is None:
        i = len(array) - 1
    if i < 0:
        return [[]]

    num = array[i]
    subsets = powerset(array , i-1)

    for i in range(len(subsets)):
        subsets.append(subsets[i] + [num])
    return subsets

def powerIter(array):

    subsets = [[]]

    for i in array:
        for j in range(len(subsets)):
            subsets.append(subsets[j]+[i])

    return subsets

print(powerset([1,2]))
print(powerIter([1,2]))