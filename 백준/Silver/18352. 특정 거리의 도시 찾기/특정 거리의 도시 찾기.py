import sys
from collections import deque
read = sys.stdin.readline

n,m,k,x = map(int, read().split())
answer = []
board = [[] for _ in range(n+1)]
dist = [-1] * (n+1)

for _ in range(m):
  a,b = map(int, read().split())
  board[a].append(b)
dist[x] = 0 #x->x로 가는 최단 거리 0
dq = deque()
dq.append(x)

while(dq):
  cur = dq.popleft()
  for i in board[cur]:
    if dist[i] == -1: #방문한 적 없다면
      dq.append(i)
      dist[i] = dist[cur]+1
      if dist[i] == k:
        answer.append(i)
    
if len(answer) == 0:
  print(-1)
else:
  answer.sort()
  for i in answer:
    print(i)