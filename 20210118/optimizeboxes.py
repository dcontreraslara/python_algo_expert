
def optimize_sets(arr):

    low = len(arr)//2
    high = len(arr)-1
    RR = []
    while low<=high:
        mid = (low+high)//2
        L = arr[:mid+1]
        R = arr[mid+1:]
        if sum(R) > sum(L):
            low = mid+1
            RR = R
        else:
            high = mid-1

    return RR

print(optimize_sets([5,5,5,6,10]))






