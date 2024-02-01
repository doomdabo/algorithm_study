from collections import deque
n,m = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]

dx=[-1,-1,-1,0,0,1,1,1]
dy=[-1,0,1,-1,1,-1,0,1]


def bfs(x,y):
  vis=[[-1]*m for _ in range(n)]
  q = deque()
  q.append((x,y))
  vis[x][y] = 0
  while q:
    curx,cury = q.popleft()
    for dir in range(8):
      nx = curx + dx[dir]
      ny = cury + dy[dir]
      if 0<=nx<n and 0<=ny<m:
        if vis[nx][ny]==-1:
          if board[nx][ny]==1:
            return vis[curx][cury]+1
          else:
            q.append((nx,ny))
            vis[nx][ny]=vis[curx][cury]+1
  
            
ans = [[-1]*m for _ in range(n)]
for i in range(n):
  for j in range(m):
    if board[i][j]!=1:
      ans[i][j] = bfs(i,j)
#print(ans)
cnt = -1
for i in range(n):
  for j in range(m):
    if ans[i][j]>cnt:
      cnt = ans[i][j]
print(cnt)