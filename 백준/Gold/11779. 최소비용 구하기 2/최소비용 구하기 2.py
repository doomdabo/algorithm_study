import heapq
#입력받기
n = int(input())
m = int(input())
INF = int(1e9)
graph = [[] for _ in range(n+1)]
dist = [INF]*(n+1)
ways = [0] * (n+1)
for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

st,end = map(int,input().split())
###입력 끝
def dijkstra(st):
    q =[]
    dist[st] = 0 #시작지점의 비용은 0으로 설정
    heapq.heappush(q,(0,st)) #비용, 현재 위치
    while q:
        cost, cur = heapq.heappop(q)
        if dist[cur] < cost:
            continue
        for nxt_node,nxt_cost in graph[cur]:
            newcost = nxt_cost + cost
            if newcost<dist[nxt_node]:
                dist[nxt_node]=newcost
                heapq.heappush(q,(newcost,nxt_node))
                ways[nxt_node] = cur #경로 저장-다음번인덱스 요소에 이전거 저장
dijkstra(st)
print(dist[end])
path = []
path.append(end)
now = end
while now != st:
    now = ways[now]
    path.append(now)
path.reverse()
print(len(path))
for i in path:
    print(str(i)+" ",end="")
