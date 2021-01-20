def getp(arr, start, end):

    pivot = arr[start]
    i = start + 1
    j = end

    while i<=j:
        if arr[i] <= pivot:
            i+=1
        elif arr[j] > pivot:
            j-=1
        else:
            arr[i], arr[j] = arr[j], arr[i]

    arr[start], arr[j] = arr[j], arr[start]

    return j


def qs(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1

    if start > end:
        return

    partition = getp(arr, start, end)

    qs(arr, start, partition-1)
    qs(arr, partition+1, end)




a = [1, 5, 10, 20, 1, -5, 100, 50, 23]
qs(a)
print(a)
