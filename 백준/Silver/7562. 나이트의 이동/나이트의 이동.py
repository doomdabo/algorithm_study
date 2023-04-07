import sys
from collections import deque
read = sys.stdin.readline
T = int(read())
dx = [2,1,-1,-2,-2,-1,1,2]
dy = [-1,-2,-2,-1,1,2,2,1]
def bfs(board,s1,s2):
  queue = deque()
  queue.append((s1,s2))
  board[s1][s2] = 0
  while queue:
    x,y = queue.popleft()
    for i in range(8):
      nx = x+dx[i]
      ny = y+dy[i]
      if(0<=nx<l and 0<=ny<l and board[nx][ny]==-1):
        queue.append((nx,ny))
        board[nx][ny]=board[x][y]+1
for _ in range(T):
  l = int(read())#한변의길이
  s1,s2 = map(int,read().split())#start
  d1,d2 = map(int,read().split())#destination
  
  board =[[-1 for j in range(l)] for i in range(l)]
  bfs(board,s1,s2)
  print(board[d1][d2])