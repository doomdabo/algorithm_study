from collections import deque
m,n,k = map(int,input().split())
#m*n 사이즈의 board 만들자
arr = [[0]*n for _ in range(m)]
for _ in range(k):
    # k번 입력 받음
    # 직사각형 왼쪽아래 꼭짓점 x,y좌표
    # 오른쪽 위 꼭짓점 x,y좌표
    x,y,xx,yy = map(int,input().split())
    #시작점 구하기
    stx = m - 1 - y
    sty = x
    edx = m - yy
    edy = xx - 1
    for i in range(edx,stx+1):
        for j in range(sty,edy+1):
            arr[i][j] = 1
#이제 보드 완성 - BFS 시작해야지..
dx = [0,1,0,-1]
dy = [1,0,-1,0]
vis = [[False]*n for _ in range(m)]
cnt = 0
dimension = []
for i in range(m):
    for j in range(n):
        #만약 arr[i][j]가 1이거나 이미 간 곳 방문할 필요가 없음
        if arr[i][j] == 1 or vis[i][j]:
            continue
        #비어있거나 방문 안했으면 일단 방문표시, 큐에 넣기
        cnt+=1
        q = deque()
        q.append((i,j))
        vis[i][j] = True
        dimen = 1
        while q:
            curx, cury = q.popleft()
            for dir in range(4):
                nx = curx + dx[dir]
                ny = cury + dy[dir]
                if nx<0 or ny<0 or nx>=m or ny>=n:
                    continue

                if vis[nx][ny] or arr[nx][ny] == 1:
                    continue
                vis[nx][ny] = True
                dimen += 1
                q.append((nx,ny))
        dimension.append(dimen)
print(cnt)
dimension.sort()
for i in dimension:
    print(i,'',end='')


