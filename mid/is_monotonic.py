def isMonotonic(array):
    import sys

    if len(array) <= 1:
        return True

    fval = array[0]
    j = 1
    while j < len(array) - 1 and array[j] == array[0]:
        j = j + 1

    is_decreasing = array[j] < fval
    fval = array[j]
    for i in range(j + 1, len(array)):
        if is_decreasing and array[i] <= fval:
            fval = array[i]
        elif is_decreasing is False and array[i] >= fval:
            fval = array[i]
        else:
            return False

    return True


