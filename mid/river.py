def riverSizes(matrix):
    out = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:  # there is a river
                out.append(check_river(matrix, i, j))

    for i in matrix:
        print(i)
    print("===>")
    return out


def check_point(matrix, i, j):
    if j < 0 or j >= len(matrix[0]) or i < 0 or i >= len(matrix):
        return False
    if matrix[i][j] != 1:
        return False

    matrix[i][j] = 2
    return True


def check_river(matrix, i, j):
    s = [(i, j)]
    size = 1
    matrix[i][j] = 2
    while s:
        curr_i, curr_j = s.pop()
        if check_point(matrix, curr_i - 1, curr_j):
            s.append((curr_i - 1, curr_j))
            size = size + 1

        if check_point(matrix, curr_i + 1, curr_j):
            s.append((curr_i + 1, curr_j))
            size = size + 1

        if check_point(matrix, curr_i, curr_j - 1):
            s.append((curr_i, curr_j - 1))
            size = size + 1

        if check_point(matrix, curr_i, curr_j + 1):
            s.append((curr_i, curr_j + 1))
            size = size + 1
    return size


testInput = [[1, 0, 0, 1, 0],
             [1, 0, 1, 0, 0],
             [0, 0, 1, 0, 1],
             [1, 0, 1, 0, 1],
             [1, 0, 1, 1, 0]]

print(riverSizes(testInput))


