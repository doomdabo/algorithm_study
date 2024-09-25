import sys
import heapq
input = sys.stdin.readline

v,e = map(int,input().split())
start = int(input()) #시작정점의 번호
graph = [[] for _ in range(v+1)] #간선을 기준으로 저장
INF = int(1e9)
dist = [INF]*(v+1) #최단거리 테이블

for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c)) #u번정점은 v와 연결되어있고 거리 w

hq = []
dist[start] = 0 #시작정점의 거리 0으로 초기화
heapq.heappush(hq,(0,start)) #(거리, 정점번호)로 값 계속 넣음
while hq: #큐에 원소 있으면 계속 진행
    cur_cost, cur_v = heapq.heappop(hq)
    if(dist[cur_v] < cur_cost): #만약 옛날에 저장된애임. 이미 더 싼 거리가 나와서 갱신 했는데 갱신되기 이전애라면 걍 볼필요 없이 팝만하면됨
        continue
    for nxt_v, nxt_cost in graph[cur_v]: #현재정점과 이어진 정점을 확인하자
        if dist[nxt_v] > nxt_cost + cur_cost: #다음 연결된 애의 거리를 확인하자.
            #다음 연결된 애 저장되어 있는 거리가 무언가 거쳐가는거보다 크면, 더 작은거로 갱신하자
            dist[nxt_v] = nxt_cost + dist[cur_v]
            heapq.heappush(hq,(dist[nxt_v],nxt_v))
#rint(dist)
for i in range(1,v+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])