def kangaroo(x1, v1, x2, v2):
    if x2 < x1:
        return kangaroo(x2, v2, x1, v1)

    if v2 >= v1:
        return "NO"

    if (x1 - x2) % (v2 - v1):
        return "YES"

    return "NO"




print(kangaroo(0,3,4,2))
print(kangaroo(21,6,47,3))