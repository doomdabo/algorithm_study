
#11722 가장 긴 감소하는 부분 수열
n= int(input())
a= list(map(int,input().split()))
dp=[1]*n
min=0
for i in range(n):
  for j in range(i):
    if a[i]<a[j]:
      dp[i]=max(dp[j]+1,dp[i])

print(max(dp))