def sameBsts(arrayOne, arrayTwo):
    if len(arrayOne) != len(arrayTwo):
        return False

    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True

    if arrayOne[0] != arrayTwo[0]:
        return False

    l1 = smallest(arrayOne)
    l2 = smallest(arrayTwo)
    r1 = greatest(arrayOne)
    r2 = greatest(arrayTwo)

    return sameBsts(l1, l2) and sameBsts(r1, r2)


def smallest(a):
    s = []

    for i in range(1, len(a)):
        if a[i] < a[0]:
            s.append(a[i])
    return s


def greatest(a):
    s = []

    for i in range(1, len(a)):
        if a[i] >= a[0]:
            s.append(a[i])
    return s



