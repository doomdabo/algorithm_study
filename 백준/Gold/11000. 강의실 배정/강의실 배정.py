#강의실 배정
#si ~ ti (n개의 수업) -> 최소 강의실 사용, 모든 수업 가능하게
import sys
import heapq
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    a,b = map(int, input().split())
    arr.append((a,b))
arr =sorted(arr, key = lambda x:x[0])

temp = [0]
pq = []
heapq.heappush(pq,arr[0][1])
for i in range(1,n):
    if arr[i][0]>=pq[0]:
        heapq.heappop(pq)
    heapq.heappush(pq,arr[i][1])
    #시초코드
# for a in arr:
#     ck =0
#     for t in range(len(temp)):
#         if temp[t]<=a[0]:
#             temp[t] = a[1]
#             ck=1
#             break
#     if ck==0:
#         temp.append(a[1])
print(len(pq))