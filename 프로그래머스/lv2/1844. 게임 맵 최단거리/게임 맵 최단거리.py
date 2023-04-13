from collections import deque

dq = deque()
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dist = [[-1]*m for _ in range (n)]
    
    dist[0][0] = 0
    dq.append((0,0))
    while(dq):
        x,y = dq.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if(nx<0 or ny <0 or nx>=n or ny>=m): continue
            if(maps[nx][ny]==0 or dist[nx][ny] !=-1): continue
            dist[nx][ny] = dist[x][y]+1
            dq.append((nx,ny))
            
        
    
    if(dist[n-1][m-1]==-1 ): return -1 
    return dist[n-1][m-1]+1
