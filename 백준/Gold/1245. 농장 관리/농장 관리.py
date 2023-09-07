import sys
from collections import deque
read = sys.stdin.readline

n,m = map(int,read().split())
board = [list(map(int,read().split())) for _ in range(n)]

dx = [0,-1,-1,-1,0,1,1,1]
dy = [1,1,0,-1,-1,-1,0,1]

vis = [[0]*m for _ in range(n)]
def check_top(i,j):
  check = 0 #젤 높을지 안높을지 체크할 변수
  dq = deque()
  dq.append((i,j))
  vis[i][j] = 1
  while(dq):
    x,y = dq.popleft()
    for dir in range(8):
      nx = x + dx[dir]
      ny = y + dy[dir]
      if nx<0 or ny<0 or nx>=n or ny>=m:
        continue
      if board[x][y]<board[nx][ny]:
        check = 1
      if vis[nx][ny] == 0 and board[x][y]==board[nx][ny]:
        vis[nx][ny] = 1
        dq.append((nx,ny))
        
  return check      

ans = 0
for i in range(n):
  for j in range(m):
    if not vis[i][j]:
      #방문한 적이 없다면 제일 높은 건지 확인해 줘야함
      if check_top(i,j) == 0:
        #print(i,j)
        ans += 1
print(ans)