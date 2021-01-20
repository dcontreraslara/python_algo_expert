def arrayManipulation(n, queries):
    res = [0 for x in range(n+1)]
    for num in range(1,n+1):
        for i in queries:
            if i[0]<=num<=i[1]:
                res[num]+=i[2]
    return max(res)


arr= [ [1, 5, 3]
        ,[4, 8, 7]
        ,[6, 9, 1]]

print(arrayManipulation(10, arr))