def moveElementToEnd(array, toMove):
    j = len(array) - 1
    i = 0

    while i < j:
        while i < j and array[j] == toMove:
            j = j - 1
        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]
            j = j - 1

        i = i + 1

    return array

