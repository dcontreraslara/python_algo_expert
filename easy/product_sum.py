# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.

def helper(array, mult):
    sum = 0
    for i in array:
        if isinstance(i, int):
            sum = sum + i
            continue
        else:
            sum = sum + helper(i, + mult+1)

    return sum * mult


def productSum(array):
    return helper(array, 1)



print(productSum([[[[[5]]]]]))
