import sys
from itertools import combinations
read = sys.stdin.readline
n,m = list(map(int,read().split()))

arr = [list(map(int,read().split())) for _ in range(n)]
result = 999999
house=[]
chicken=[]
for i in range(n):
  for j in range(n):
    if arr[i][j] == 1:
      house.append([i,j])
    elif arr[i][j]==2:
      chicken.append([i,j])
for i in combinations(chicken,m): #치킨집 중 m개 고르기
  city_len = 0 #도시 치킨 거리
  for j in house:#m개 고른 치킨집이랑 집이랑 짬뽕시키기
    house_len = 999 #각 집의 치킨 거리
    for k in range(m): #각 치킨집마다 거리 계산 해야함 
      #고른 m개 중 k번째거
      house_len = min(house_len,abs(j[0]-i[k][0])+abs(j[1]-i[k][1]))
    city_len +=house_len
  result = min(result, city_len)

print(result)
    
      