def getTotalX(a, b):
    # Write your code here
    a = sorted(a, reverse=True)
    results = [0] * len(b)
    for i in range(len(b)):
        j = 0

        while j < len(a) and b[i] % a[j] == 0:
            j += 1

        if j == len(a):
            results[i] += 1
    return sum(results)


print(getTotalX([2],[20, 30, 12]))