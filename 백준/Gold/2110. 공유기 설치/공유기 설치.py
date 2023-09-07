import sys
read = sys.stdin.readline

n,c = map(int,read().split()) #n, c 입력 받기
h = [int(read()) for _ in range(n)] #집 위치 입력받기
h.sort() #이진 탐색 위해 sort

start, end = 1, h[n-1] - h[0] #최소거리 1, 최대거리 계산하기
result = 0
if c==2:
  print(h[n-1]-h[0])
else: 
  while start < end:  
    mid = (start+end)//2 #공유기 공평하게 설치할 수 있는 간격 구하기-> 처음엔 임의로 중간값
    #예시로, 1,2,4,8,9에 집이 있다고 하면, 최소거리 1, 최대거리 8임. 그래서 중간값 4
    #일단 첫번째 집에 설치를 해봄

    last_set = h[0] #1에설치가 됨. 
    cnt = 1 #몇개 설치할 수 있나 카운팅
    #그 다음 집부터 mid만큼의 간격을 두고 설치를 하면서 몇 개 설치 할 수 있나 체크
    for i in range(1,n):
      if last_set + mid <= h[i]: #마지막 설치한 집 + 설정한 mid값 <= 다음 집 위치
        cnt += 1 #카운팅 해주기
        last_set = h[i] #마지막 설치한 집을 업데이트 해줌

    if cnt >= c: #설치한 공유기 수가 설치해야할 수 이상이면 간격이 작다는 말.
      result = mid #일단 거리를 저장해 두고
      start = mid + 1#한번 더 넓게 설치해봄
    elif cnt < c: #공유기를 더설치해야하므로 더 좁게 설치해야함
      end = mid

  print(result)
      
