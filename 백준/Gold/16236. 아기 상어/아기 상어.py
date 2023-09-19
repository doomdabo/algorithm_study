from collections import deque
dx = [-1,0,1,0]
dy = [0,-1,0,1]

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            x = i #상어의 x좌표
            y = j #상어의 y좌표
            board[i][j] = 0 #상어 0으로 만듦



def bfs(x,y,size):
    fish = []
    vis = [[-1]*N for _ in range(N)]
    q = deque()
    q.append((x,y)) #x,y부터 bfs 돌자
    vis[x][y] = 0 #처음 상어 위치는 거리 0
    while q:
        curx,cury = q.popleft()
        for dir in range(4):
            nx = curx + dx[dir]
            ny = cury + dy[dir]
            if nx<0 or nx>=N or ny<0 or ny>=N: #범위 벗어나는 경우
                continue
            if board[nx][ny] > size or vis[nx][ny] != -1: #사이즈가 더 큰경우나, 방문했던 경우
                continue
            vis[nx][ny] = vis[curx][cury] + 1
            q.append((nx,ny))
            if 0 < board[nx][ny] < size: #얘는 먹을 수 있는 물고기
                fish.append((vis[nx][ny], nx, ny)) #차례대로 거리, x좌표, y좌표
    return sorted(fish, key=lambda x:(x[0],x[1],x[2]))

size = 2 #상어 초기 사이즈는 2 -> 같은 수의 물고기 먹으면 크기 1 증가
answer = 0 #여기다가 몇초 지났나 확인할 것임
cnt = 0 #몇마리 먹었나 보는용
while True:
    #계속 반복하면서 초를 세줘야함
    #일단 BFS로 돌면서 먹을 수 있는 물고기를 (거리,x,y)좌표 순으로 저장함
    fish = bfs(x,y,size)
    #맨 앞에 있는 애를 먹어야함.
    #근데 만약 fish가 비어있다면 그만두고 끝내야겠지?
    if not fish:
        print(answer)
        break
    #맨앞에 있는 애를 먹을거야
    answer += fish[0][0] #맨앞에있는 애의 첫번쨰 원소에 거리가 들어있음.
    #그 거리만큼 초가 증가한다..

    #이제 먹은 위치로 이동해야함
    x = fish[0][1]
    y = fish[0][2]
    #보드에서 물고기 삭제해버려
    board[x][y] = 0
    #한마리 먹었다고 표시
    cnt += 1
    #근데 같은 수 만큼 물고기 먹으면 크기 1증가
    if size == cnt:
        cnt = 0
        size += 1




