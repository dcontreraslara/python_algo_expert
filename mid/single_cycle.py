def hasSingleCycle(array):
    visited = [0 for x in array]

    i = 0

    while True:
        if visited[i] == 1:
            break
        visited[i] = 1
        i = (array[i] + i) % len(array)

    if i != 0:
        return False

    for i in visited:
        if i == 0:
            return False
    return True
