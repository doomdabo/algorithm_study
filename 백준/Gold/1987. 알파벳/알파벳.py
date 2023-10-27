n,m = map(int,input().split())
arr = [list(map(str,input())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0
vis = set()
def bt(x,y,count):
    global ans
    ans = max(ans,count)
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m and not arr[nx][ny] in vis:
            vis.add(arr[nx][ny])
            bt(nx,ny,count+1)
            vis.remove(arr[nx][ny])
vis.add(arr[0][0])
bt(0,0,1)
print(ans)


