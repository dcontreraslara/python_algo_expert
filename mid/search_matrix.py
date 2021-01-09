def get_index(matrix, index):
    position = index % len(matrix[0])
    row = index // len(matrix[0])

    return row, position


def searchInSortedMatrix(matrix, target):
    i = 0
    j = len(matrix[0]) - 1

    while i < len(matrix) and j >= 0:
        if target < matrix[i][j]:
            j = j - 1
            continue

        if target > matrix[i][j]:
            i = i + 1
            continue

        if target == matrix[i][j]:
            return [i, j]
    return [-1, -1]







