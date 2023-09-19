import heapq
import sys
read = sys.stdin.readline
INF = int(1e9)
v, e = map(int,read().split())
graph = [[] for _ in range(v+1)] #연결이 어디어디 되어있나 확인
k = int(read())
#입력받기
for _ in range(e):
    a,b,c = map(int,read().split())
    graph[a].append((b,c))

dist = [INF] * (v+1)

def dijkstra(start):
    dist[start] = 0 #시작점은 0으로 초기화
    q = []
    heapq.heappush(q,(0,start)) #처음 거리: 0, 시작위치: start
    while q:
        #큐 비어있지 않으면 가장 짧은거 불러오기
        cost, cur = heapq.heappop(q)
        #이게 전에 처리 된건지(이미 더 짧은게 있나 확인)
        if dist[cur] < cost: #큐에서 방금 나온게 더 큰거면 그거 무시하는것
            continue
        for i in graph[cur]:
            #현재위치에서 연결된 모든 점을 살필거다
            #일단 거리 계산을 하자
            newcost = cost + i[1]
            #만약 지금까지 온 거리보다 짧은게 나왔으면
            if newcost<dist[i[0]]:
                dist[i[0]] = newcost #새로 구한 값으로 갱신해줌
                heapq.heappush(q,(newcost,i[0]))


dijkstra(k)
for i in range(1,v+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])