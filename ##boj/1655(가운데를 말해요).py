import sys
from heapq import heappush, heappop

In = sys.stdin.readline

N = int(In()[:-1])

max_heap = []
min_heap = []

middle = int(In()[:-1])

print(middle)

for _ in range(N - 1):
    k = int(In()[:-1])

    if k > middle:
        if len(max_heap) == len(min_heap):
            heappush(min_heap, k)
        else:
            heappush(max_heap, (-middle, middle))
            heappush(min_heap, k)
            middle = heappop(min_heap)
    elif k == middle:
        if len(max_heap) == len(min_heap):
            heappush(min_heap, k)
        else:
            heappush(max_heap, (-k, k))
    else:
        if len(max_heap) == len(min_heap):
            heappush(min_heap, middle)
            heappush(max_heap, (-k, k))
            middle = heappop(max_heap)[1]
        else:
            heappush(max_heap, (-k, k))

    print(middle)
