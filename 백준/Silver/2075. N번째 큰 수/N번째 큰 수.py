import heapq
n = int(input())
heap = []
for _ in range(n):
    arr = map(int, input().split()) #한줄씩 입력받음
    for i in arr:
       if len(heap) < n: #만약 힙에 자리 있으면 일단 push
           heapq.heappush(heap, i)
       else:
           #자리가 없으면 비교를 하자
            if heap[0] < i:
                heapq.heappop(heap)
                heapq.heappush(heap, i)
print(heap[0])
