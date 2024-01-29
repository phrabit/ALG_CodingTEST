import sys
import heapq as hq
input = sys.stdin.readline

heap = []
n = int(input())
for _ in range(n):
    num = int(input())
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-hq.heappop(heap))
    else:
        hq.heappush(heap, -num)