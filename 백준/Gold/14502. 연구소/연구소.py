import sys
import copy
from collections import deque
from itertools import combinations

read = sys.stdin.readline
n,m = map(int,read().split())

dx = [-1,0,1,0]
dy = [0,1,0,-1]


#정보 입력 받기 - 얘는 항상 본 상태 유지해야함. 
arr = [list(map(int,read().strip().split())) for _ in range(n)]
#0 나오면 저장할 배열 선언
blank = []
#다 돌면서 0 나오면 배열에 담기
for i in range(n):
  for j in range(m):
    if arr[i][j] == 0:
      blank.append([i,j])
#print(blank)
ans = 0
#3개의 조합 만들기
for combi in combinations(blank,3):
  arr_temp = copy.deepcopy(arr)#그래서 복사해서 사용
  #방문한 위치 저장 위해 맵 0으로 초기화
  vis = [[0]*m for _ in range(n)]
  #0몇개인지 계산
  count = 0 
  for combi_cnt in range(3):
    #빈칸 3개를 선택해서 1로 만들기
    arr_temp[combi[combi_cnt][0]][combi[combi_cnt][1]] = 1
  #전체 arr_temp를 돌면서 2가 나오면 바이러스 전파 시키기

  for i in range(n):
    for j in range(m):
      if(arr_temp[i][j]==2):#바이러스를 의미하는 2가 나오면
        dq = deque()
        dq.append((i,j))
        vis[i][j]=1
        while dq: #탐색 시작
          x,y = dq.popleft()
          for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx<0 or ny<0 or nx>=n or ny>=m: 
              continue
            if vis[nx][ny]==1 or arr_temp[nx][ny]==1 or arr_temp[nx][ny]==2: 
              continue
            arr_temp[nx][ny] = 2#0이 나온 경우 2로 바이러스 전파 
            vis[nx][ny]=1
            dq.append((nx,ny))
  #bfs끝, 0 갯수 세기
  for i in range(n):
    for j in range(m):
        if arr_temp[i][j]==0:
          count +=1
  ans = max(count , ans)          
          
            
print(ans)