def arrayOfProducts(array):
    if len(array) == 1:
        return array

    aux = 1
    for i in range(len(array)):
        curr = aux
        aux = array[i] * aux
        for j in range(i + 1, len(array)):
            curr = curr * array[j]

        array[i] = curr

    return array

print(arrayOfProducts([5, 1, 4, 2]))