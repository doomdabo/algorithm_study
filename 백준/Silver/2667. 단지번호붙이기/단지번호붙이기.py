from collections import deque
'''
1 - 집이 있는곳
0 - 집이 없는곳
연결된 집의 모임인 단지를 정하고 단지에 번호를 붙이려 함
연결되었다? 어떤 집이 좌우 혹은 아래위로 다른집이 있는 경우. 대각선 ㄴㄴ

단지 수 출력/ 각 단지에 속하는 집의 수 오름차순으로 정렬하여 출력
'''

n = int(input())
arr = []
for i in range(n):
    arr.append(input())

dx = [0,-1,0,1]
dy = [1,0,-1,0]
vis = [[False]*n for _ in range(n)]
cnt = 0
ans = []
for i in range(n):
    for j in range(n):
        if vis[i][j] or arr[i][j]=='0':
            continue
        q = deque()
        cnt += 1
        q.append((i,j))
        vis[i][j] = True
        t = 1
        while q:
            curx, cury = q.popleft()
            for dir in range(4):
                nx = curx + dx[dir]
                ny = cury + dy[dir]
                if nx<0 or ny<0 or nx>=n or ny>=n:
                    continue
                if vis[nx][ny]:
                    continue
                if arr[nx][ny] == '0':
                    continue
                vis[nx][ny]=True
                q.append((nx,ny))
                t += 1
        ans.append(t)
print(cnt)
ans.sort()
for i in ans:
    print(i)
