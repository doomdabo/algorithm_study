import heapq

n,e = map(int,input().split())
board = [[] for i in range(n+1)]
for i in range(e):
  a,b,c = map(int,input().split())
  board[a].append([b,c])
  board[b].append([a,c])
v1,v2 = map(int,input().split())

def dij(start,end):
  dis = [1e9]*(n+1)
  q=[]
  dis[start] = 0
  heapq.heappush(q,[0,start])
  while q:
    d,now = heapq.heappop(q)
    if dis[now]<d:
      continue
    for edge,cost in board[now]:
      if dis[edge]>cost+d:
        dis[edge]=cost+d
        heapq.heappush(q,[dis[edge],edge])
  return dis[end]

stov1=dij(1,v1)
stov2=dij(1,v2)
v1tov2=dij(v1,v2)
v1ton=dij(v1,n)
v2ton=dij(v2,n)

r1=stov1+v1tov2+v2ton
r2=stov2+v1tov2+v1ton
# if v1tov2>=1e9:
#   print(-1)
# else:
ans=min(r1,r2)
if ans>=1e9:
  print(-1)
else:
  print(ans)
  
