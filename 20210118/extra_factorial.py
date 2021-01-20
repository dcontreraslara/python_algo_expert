def extraLongFactorials(n):
    num = 1
    for i in range(2,n+1):
        num = num * i
    return num


print(extraLongFactorials(45))

print([1,2,3][:])