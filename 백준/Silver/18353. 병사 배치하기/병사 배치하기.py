import sys
read = sys.stdin.readline
n = int(read())
arr = list(map(int, read().split()))
dp = [1] * n

for i in range(1,n):
  for j in range(i): #0~i-1번째 원소들 탐색
    #만약 내림차순이라면(i번째 원소보다 큰 값들 중 가장 큰 dp값 찾기)
    if arr[j]>arr[i]: 
      dp[i] = max(dp[i], dp[j]+1) 

print(n-max(dp))
