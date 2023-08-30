import sys
from collections import deque
read = sys.stdin.readline
############변수 입력 받기############
n,k = map(int, read().split())
board = [list(map(int,read().rstrip().split())) for _ in range(n)]
s,x,y = map(int, read().split())
####################################
dx = [-1,0,1,0]
dy = [0,-1,0,1]
data = []
for i in range(n):
  for j in range(n):
    if board[i][j] != 0:
      data.append((board[i][j],i,j))

data.sort()
dq = deque(data)

sec = 0
while dq:
  if sec == s:
    break
  for _ in range(len(dq)): #매번 새로 들어오는 칸의 수만큼 반복
    vir, xx, yy = dq.popleft()
    for dir in range(4):
      nx = xx + dx[dir]
      ny = yy + dy[dir]
      if nx<0 or ny<0 or nx>=n or ny>=n:
        continue
      if board[nx][ny] != 0:
        continue
      board[nx][ny] = vir
      dq.append((vir,nx,ny))
  sec+=1

print(board[x-1][y-1])


