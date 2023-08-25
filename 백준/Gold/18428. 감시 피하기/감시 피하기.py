import sys
from collections import deque
read = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
#수 입력 받기
n = int(read())
board = [list(map(str,read().rstrip().split())) for _ in range(n)]
vis = [[0]*n for _ in range(n)]
check = 0
#입력 받은 정보 저장 - 선생님 위치 저장
teacher = []
for i in range(n):
  for j in range(n):
    if board[i][j] == 'T':
      teacher.append((i,j))

def bfs(): #선생님이 학생을 잡을 수 있나 없나 확인.
  global n
  for x,y in teacher: #선생님마다 확인
    for dir in range(4):
      nx,ny = x,y
      while 0<=nx<n and 0<=ny<n:
        if board[nx][ny] == 'O': #감시가능
          break
        if board[nx][ny] == 'S': #학생 발견        
          return False
        nx += dx[dir]
        ny += dy[dir]
  return True    

        
def backtracking(cnt):
  global n, check
  if cnt == 3:
    #3개의 장애물 설치를 완료한 경우
    if bfs(): #bfs를 통해 선생님이 학생 감시 가능한지 확인
      #감시 가능하면
      check = 1
      return 
  else:
    for i in range(n):
      for j in range(n):
        if board[i][j] == 'X':
          board[i][j] = 'O'
          backtracking(cnt + 1)
          board[i][j] = 'X'
backtracking(0)
if check == 1:
  print("YES")
else:
  print("NO")