def waterArea(heights):
    left = [0 for x in heights]
    right = [0 for x in heights]

    for i in range(1, len(heights)):
        left[i] = max(heights[i - 1], left[i - 1])

    i = len(heights) - 2

    while i >=0:
        right[i] = max(heights[i+1], right[i+1])
        i = i - 1

    sum = 0
    for i in range(len(heights)):
        min_height = min(left[i], right[i])

        if min_height - heights[i] > 0:
            sum = sum + min_height - heights[i]

    return sum



print(waterArea([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]))