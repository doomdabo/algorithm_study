from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for v in edge:
        graph[v[0]].append(v[1])
        graph[v[1]].append(v[0])
    vis = [-1 for _ in range(n+1)]
    dq=deque()
    dq.append(1)
    vis[1] = 0
    while(dq):
        cur = dq.popleft()
        for i in graph[cur]:
            if vis[i] == -1:
                vis[i]=vis[cur] + 1
                dq.append(i)
                        
    maxx = max(vis)
    for i in vis:
        if i==maxx:
            answer+=1
    return answer