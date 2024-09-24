import heapq
import sys
n = int(input())
arr = []
for _ in range(n):
    a = int(sys.stdin.readline())
    if a==0:
        if len(arr)==0:
            print(0)
        else:
            print(heapq.heappop(arr))

    else:
        heapq.heappush(arr, a)