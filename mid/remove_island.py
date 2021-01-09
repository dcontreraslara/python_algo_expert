def removeIslands(matrix):
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            if matrix[i][j] == 1:
                is_island(matrix, i, j)

    return matrix


def to_append(m, i, j, s):
    if i == 0 or j == 0:
        return

    if i == len(m) - 1:
        return

    if j == len(m[0]) - 1:
        return

    if m[i][j] == 1:
        s.append((i, j))


def is_island(matrix, i, j):

    s = [(i,j)]

    is_island = True
    while len(s) > 0:
        curr_i, curr_j = s.pop()

        left = curr_j - 1
        right = curr_j + 1
        top = curr_i - 1
        bottom = curr_i + 1

        if matrix[curr_i][left] == 1 and left == 0: # is not island
            is_island = False

        if matrix[curr_i][right] == 1 and right == len(matrix[0]) -1: # is not island
            is_island = False

        if matrix[top][curr_j] == 1 and top == 0: # is not island
            is_island = False

        if matrix[bottom][curr_j] == 1 and bottom == len(matrix) - 1: # is not island
            is_island = False

        to_append(matrix, curr_i, left, s)
        to_append(matrix, curr_i, right, s)
        to_append(matrix, top, curr_j, s)
        to_append(matrix, bottom, curr_j, s)

        if matrix[curr_i][curr_j] == 1:
            matrix[curr_i][curr_j] = 2


    for i in matrix:
        for j in range(len(i)):
            if i[j] == 2:
                i[j] = 0 if is_island else 1

input = [
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 1],
            [0, 0, 1, 0, 1, 0],
            [1, 1, 0, 0, 1, 0],
            [1, 0, 1, 1, 0, 0],
            [1, 0, 0, 0, 0, 1],
        ]
m = removeIslands(input)

for x in m:
    print(x)