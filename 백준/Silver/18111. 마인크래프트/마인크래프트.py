import sys
read = sys.stdin.readline
n,m,b = map(int,read().split()) #b는 가진 블록의 수
arr = [list(map(int,read().split())) for _ in range(n)]

ans = sys.maxsize
idx = 0
for height in range(257): #최소 높이~ 최대 높이까지 탐색
  use,remove = 0,0 #use는 가지고있는 블록 사용(1초), remove는 블록 제거(2초)
  for i in range(n):
    for j in range(m):
      if(arr[i][j]>height): #만약 해당 칸이 현재 높이보다 크다면 제거
        remove+=arr[i][j]-height #현재 높이에서 해당칸의 높이를 뺀 값을 remove에 더한다
      else: #해당 칸이 현재 높이보다 작거나 같다면 쌓기
        use+=height-arr[i][j] #높이 차 만큼 use에 더해줌
  #블록 뺀 것과 원래 있던 블록의 합이 더 커야지 층 만들 수 있음
  if use<=remove+b:   #사용한 블록<=제거한거 + 인벤토리에 있는블록
    if use+remove*2 <=ans: 
      ans = use+remove*2
      idx=height

print(ans,idx)