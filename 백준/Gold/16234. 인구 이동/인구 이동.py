import sys
from collections import deque
dx = [-1,0,1,0]
dy = [0,-1,0,1]
#입력받기
read = sys.stdin.readline
n,L,R = map(int,read().rstrip().split())
board = [[0]*n for _ in range(n)]

#보드 입력받기
for i in range(n):
  temp = list(map(int,read().rstrip().split()))
  for j in range(n):
    board[i][j] = temp[j]
  
cnt = 0
check = 0
while True:
  vis = [[0]*n for _ in range(n)]
  for i in range(n): #보드 전체를 돌면서 완전탐색
    for j in range(n):
      union = []
      if vis[i][j] == 0: #방문한 적이 없다면
        #BFS 시작해보기
        dq = deque()
        dq.append((i,j)) #일단 첫 지점 큐에 넣기
        union.append((i,j))
        vis[i][j] = 1 #방문 표시하기
        while dq:
          x,y = dq.popleft()
          for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx<0 or ny<0 or nx>=n or ny>=n or vis[nx][ny]!=0: #범위내에 있고, 방문한 적 없다면
              continue
            if L<=abs(board[x][y] - board[nx][ny])<=R: #국경선을 열 수 있다면
              dq.append((nx,ny)) #큐에 넣기
              union.append((nx,ny))
              vis[nx][ny] = 1
      
      if len(union) > 1:
        sum = 0
        for xx,yy in union:
          sum += board[xx][yy]
        sum = sum // len(union) 
        for xx,yy in union:
          board[xx][yy] = sum
        check = 1
  if check == 0: 
    break    
  cnt+=1
  check = 0
print(cnt)   