import sys
def minOperations(arr, threshold, d):
    # Write your code here
    vector = []
    MAX_VAL = 10000
    for i in range(MAX_VAL):
        vector.append([])

    n = len(arr)
    for i in range(n):
        count = 0

        vector[arr[i]] = vector[arr[i]] + [0]

        while arr[i] > 0:
            arr[i] = arr[i] // d
            count += 1
            vector[arr[i]] += [count]

    response = float('inf')

    for i in range(MAX_VAL):

        if len(vector[i]) >=threshold:
            m = 0
            vector[i].sort()

        for j in range(len(vector[i])):
            m = m+vector[i][j]

        response = min(response, m)

    return response


print(minOperations([64,30,25,33],2,2))