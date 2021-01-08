def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne = sorted(arrayOne)
    arrayTwo = sorted(arrayTwo)
    i = 0
    j = 0
    print(arrayOne, arrayTwo)
    import sys
    mm, candidate = sys.maxsize, sys.maxsize
    r1, r2 = -1, -1
    while i < len(arrayOne) and j < len(arrayTwo):
        f1,f2 = arrayOne[i] , arrayTwo[j]
        if arrayOne[i] < arrayTwo[j]:
            candidate = arrayTwo[j] - arrayOne[i]
            i = i + 1
        elif arrayOne[i] > arrayTwo[j]:
            candidate = arrayOne[i] - arrayTwo[j]
            j = j + 1
        else:
            return [arrayOne[i], arrayTwo[j]]

        if candidate < mm:
            mm = candidate
            r1, r2 = f1, f2

    return [r1, r2]



print(smallestDifference([-1, 5, 10, 20, 28, 3],[26, 134, 135, 15, 17]))



