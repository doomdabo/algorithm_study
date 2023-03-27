import sys
from collections import deque

read = sys.stdin.readline
n, m = map(int, read().split())
graph = [list(map(int, read().split())) for _ in range(n)]
vis = [[False]* m for _ in range(n)]

#하우상좌
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cnt = 0
mx = 0

def bfs(x,y):
  queue = deque()
  queue.append((x, y))
  vis[i][j] = True
  area = 0
  while queue:
    x, y = queue.popleft()
    area = area + 1

    for dir in range(4):
      nx = x + dx[dir]
      ny = y + dy[dir]
      if 0 <= nx < n and 0 <= ny < m and not vis[nx][ny] and graph[nx][ny] == 1:
        queue.append((nx, ny))

        vis[nx][ny] = True
  return area
        
for i in range(n):
  for j in range(m):
    if graph[i][j] == 1 and not vis[i][j]:
      cnt = cnt + 1  #그림의 수 카운팅
      mx = max(mx, bfs(i, j))
      


print(cnt)
print(mx)
