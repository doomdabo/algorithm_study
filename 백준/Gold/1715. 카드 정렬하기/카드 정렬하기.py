import sys
from queue import PriorityQueue
read = sys.stdin.readline
n = int(read())
pq = PriorityQueue()
#수 입력받기
for _ in range(n):
    num = int(read())
    pq.put(num)

ans = 0

while pq.qsize()>=2:
    n1 = pq.get()
    n2 = pq.get()
    newnum = n1 + n2
    pq.put(newnum)
    ans += newnum

print(ans)