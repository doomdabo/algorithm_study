import sys
read = sys.stdin.readline

n,c = map(int,read().split()) #n, c 입력 받기
h = [int(read()) for i in range(n)] #집 위치 입력받기
h.sort() #이진 탐색 위해 sort
start,end = 1, h[n-1] - h[0] #집 사이의 최소 거리, 최대 거리
result = 0
#집이 2개라면 무조건 처음 ~ 마지막 집 사이의 거리
if c == 2:
    print(h[n-1] - h[0])
else:
    while(start < end): #이진탐색 시작
        mid = (start + end)//2
        count = 1
        ts = h[0] #마지막으로 설치된 공유기의 위치
        for i in range(n):
            if h[i] - ts >= mid:
                count+=1
                ts = h[i]
        if count >= c:
            result = mid
            start = mid + 1
        elif count < c:
            end = mid
    print(result)