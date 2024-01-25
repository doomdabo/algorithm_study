#11053 가장 긴 증가하는 부분 수열
n = int(input())
a = list(map(int,input().split()))
dp=[1]*n
for i in range(n):
  for j in range(i):
    if a[i]>a[j] and dp[i]<dp[j]+1:
      dp[i] = dp[j]+1
print(max(dp))