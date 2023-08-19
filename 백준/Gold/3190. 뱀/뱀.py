import sys
from collections import deque
read = sys.stdin.readline

dx = [0,1,0,-1]#우,하,좌,상
dy = [1,0,-1,0]

n = int(read()) #보드의 크기
board = [[0]*(n+1) for _ in range(n+1)] #보드 초기화

k = int(read()) #사과의 개수
for _ in range(k): #사과 위치 입력 받기
  x,y = list(map(int,read().split()))
  board[x][y] = 4 #사과를 위치 시킴

l = int(read()) #뱀의 방향 변환 횟수
dirChange = dict()
for _ in range(l): #방향변환 정보 입력받기
  x,c = list(map(str, read().split()))
  dirChange[int(x)] = c
#뱀의 몸을 deque로 표현
snake = deque() #deque 생성
snake.append((1,1)) 

x,y = 1,1 #맨 처음칸 좌표 기록
board[1][1] = 1 #맨 처음칸인 1,1에 뱀 위치
second = 0 #초 기록 위함
dir = 0 #방향 관리 위한 변수

while True:
  second += 1
  nx,ny = x+dx[dir], y+dy[dir] #다음 이동 좌표 미리 계산. dir에 따라 상하좌우로 이동
  if nx<=0 or ny<=0 or nx>n or ny>n or (nx,ny) in snake: #벽에 닿거나 뱀 몸에 닿으면 while문 탈출 
    break
  if board[nx][ny]!=4: #사과가 없는 경우
    tx,ty = snake.popleft() #몸길이 줄여서 꼬리가 위치한 칸 비움
    board[tx][ty] = 0 #보드에 꼬리 위치한 칸 0으로 바꿔줌
  #사과 있는 경우, 없는경우 모두 몸길이 늘려서 머리를 다음칸에 위치시켜야함
  board[nx][ny] = 1 #뱀을 위치 시킴
  snake.append((nx,ny)) #큐 오른쪽에 해당 위치 추가(머리에 해당)
  x = nx 
  y = ny
  if second in dirChange: #해당 초에 이동이 포함된다면
    if dirChange[second] == 'L': #왼쪽 방향으로 이동하는 경우 상좌하우상좌하우 반복 (반시계방향)
      dir = (dir - 1) % 4 
    else: #오른쪽 방향으로 이동하는 경우 우하좌상 반복(시계방향)
      dir = (dir + 1) % 4
print(second)