N = int(input())
a = [list(map(int,input().split())) for _ in range(N)]

#방향별 모래 비율 위치가 어디로 변하는지 구하기
left = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1),
         (-1, -1, 0.1), (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)]
right = [(x,-y,z) for x,y,z in left]
down = [(-y,x,z) for x,y,z in left]
up = [(y,x,z) for x,y,z in left]
##########################################
answer = 0 #밖으로 나간 모래양
now = [N//2,N//2] #현재 x좌표 / y좌표
def recount(time, dx, dy, direction):
    global answer
    for _ in range(time):
        #현재 좌표 업데이트
        now[0] += dx
        now[1] += dy
        #회오리 끝난 경우
        if now[0]<0 or now[1] <0:
            break
        total = 0 #alpha 구하기 위한 변수
        for x,y,rate in direction:
            nx = x + now[0]
            ny = y + now[1]
            if rate == 0: #a인 경우
                sand = a[now[0]][now[1]] - total
            else: #비율대로 분배
                sand = int(a[now[0]][now[1]] * rate)
                total += sand
            if 0<=nx<N and 0<=ny<N:
                a[nx][ny] += sand
            else: #범위 밖에 있으면 ans 카운트
                answer += sand

for i in range(1,N+1):
    if i % 2 == 1: #홀수면 왼쪽, 아래쪽으로 순서대로 이동
        recount(i,0,-1,left) #왼쪽으로 이동
        recount(i,1,0,down) #아래로 이동
    elif i % 2 == 0: #짝수면 오른쪽, 위 순서대로 모래 이동
        recount(i,0,1,right) #오른쪽으로 이동
        recount(i,-1,0,up) #위쪽으로 이동
print(answer)