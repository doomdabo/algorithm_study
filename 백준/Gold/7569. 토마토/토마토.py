from collections import deque
import sys
input = sys.stdin.readline
m,n,h = map(int,input().split())
arr = []
dx = [0,1,0,-1,0,0]
dy = [1,0,-1,0,0,0]
dz = [0,0,0,0,1,-1]
vis = [[[False]*m for _ in range(n)] for _ in range(h)]
for _ in range(h):
    temp = []
    for _ in range(n):
        temp.append(list(map(int,input().split())))
    arr.append(temp)
q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                q.append((i, j, k))
                vis[i][j][k] = True
while q:
    cx, cy, cz= q.popleft()
    for dir in range(6):
        nx = cx + dx[dir]
        ny = cy + dy[dir]
        nz = cz + dz[dir]
        if nx<0 or ny<0 or nz<0 or nx>=h or ny>=n or nz>=m:
            continue
        if vis[nx][ny][nz] == False and arr[nx][ny][nz] == 0:
            q.append((nx, ny, nz))
            arr[nx][ny][nz] = arr[cx][cy][cz] + 1
            vis[nx][ny][nz] = True

ans = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 0:
                print(-1)
                exit(0)
            ans = max(ans, arr[i][j][k])
print(ans-1)