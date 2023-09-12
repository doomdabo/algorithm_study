import sys
from collections import deque
read = sys.stdin.readline

n = int(read())
m = int(read())
friend = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,read().split())
    friend[a].append(b)
    friend[b].append(a)
vis = [0]*(n+1)

dq = deque()
vis[1] = 1
dq.append(1)
while dq:
    cur = dq.popleft()
    for i in friend[cur]:
        if vis[i] == 0: #방문한 적이 없으면
            vis[i] = vis[cur] + 1
            dq.append(i)

ans = 0
for i in range(2,n+1):
    if 2<=vis[i]<=3:
        ans+=1
print(ans)