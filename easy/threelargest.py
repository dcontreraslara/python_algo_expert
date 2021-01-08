def findThreeLargestNumbers(array):
    import heapq
    a = [0,0,0]
    heapq._heapify_max(array)
    a[2] =  heapq.heappop(array)
    heapq._heapify_max(array)
    a[1] =  heapq.heappop(array)
    heapq._heapify_max(array)
    a[0] =  heapq.heappop(array)
    return a

