def spiralTraverse(array):
    # Write your code here.
    top = 0
    bottom = len(array) - 1
    left = 0
    right = len(array[0]) - 1

    dir = 0
    res = []
    while top <= bottom and left <= right:

        if dir == 0:
            for j in range(left, right + 1):
                res.append(array[top][j])
            top = top + 1
        elif dir == 1:
            for j in range(top, bottom + 1):
                res.append(array[j][right])
            right = right - 1
        elif dir == 2:
            for j in reversed(range(left, right + 1)):
                res.append(array[bottom][j])
            bottom = bottom - 1
        elif dir == 3:
            for j in reversed(range(top, bottom + 1)):
                res.append(array[j][left])
            left = left + 1

        dir = (dir + 1) % 4
    return res


print(spiralTraverse([[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]))
