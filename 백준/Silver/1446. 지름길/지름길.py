#지름길
n, d = map(int, input().split())
arr = []
for i in range(n):
    a = list(map(int, input().split()))
    arr.append(a)
'''
1. 최단거리 테이블 생성 -> [i for i in range(D+1)] = [0, 1, 2, 3, ... , D]
2. 한 칸 전 위치의 테이블 값+1이 현재 테이블 값보다 작다면 현재 테이블 값을 한 칸 전 위치의 테이블 값+1로 바꾼다. 
3. 현재 위치에 지름길이 있다면 지름길로 건너간 곳의 원래 테이블 값과 지름길로 건너가기 전의 
테이블 값+지름길의 거리 중 더 작은 값으로 건너간 곳의 값을 바꾼다. 
'''
dis = [i for i in range(d+1)]
for i in range(d+1):
    if i > 0:
        dis[i] = min(dis[i], dis[i - 1] + 1)
    for s,e,di in arr:
        if i==s and e<=d and dis[i]+di<dis[e]:
            dis[e] = dis[i]+di

print(dis[d])