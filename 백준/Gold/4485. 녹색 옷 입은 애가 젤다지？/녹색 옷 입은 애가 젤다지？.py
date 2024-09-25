import sys
import heapq
input = sys.stdin.readline

problem = 1 #문제 번호

dx = [0,1,0,-1]
dy = [1,0,-1,0]
INF = int(1e9)

while True:
    n = int(input())
    if n == 0:
        break
    arr = [list(map(int,input().split())) for _ in range(n)]

    #일단 매번 새로 생성해줘야지
    dist = [[INF] * n for _ in range(n)] #그냥 N*N짜리 거리판을 만든다
    dist[0][0] = arr[0][0]
    q = []
    heapq.heappush(q,(arr[0][0],(0,0)))
    while q:
        cur_cost, cur_pos = heapq.heappop(q)
        if dist[cur_pos[0]][cur_pos[1]] != cur_cost:
            continue
        for dir in range(4):
            nx = cur_pos[0] + dx[dir]
            ny = cur_pos[1] + dy[dir]
            if nx<0 or nx >= n or ny < 0 or ny >= n:
                continue
            if dist[nx][ny] > cur_cost + arr[nx][ny]:
                dist[nx][ny] = cur_cost + arr[nx][ny]
                heapq.heappush(q,(dist[nx][ny],(nx,ny)))
    print("Problem "+ str(problem) + ": " + str(dist[n-1][n-1]))
    problem += 1