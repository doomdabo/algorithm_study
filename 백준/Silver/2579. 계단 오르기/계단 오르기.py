###https://stonejjun.tistory.com/24

n=int(input())
arr=[0]*301
for i in range(n):
  arr[i+1]=int(input())

dp=[0]*301 #dp[n]은 n칸 까지 올랐을 때 최댓값
dp[1]=arr[1]
dp[2]=arr[1]+arr[2]
dp[3]=max(arr[2]+arr[3],arr[1]+arr[3])
for i in range(4,n+1):
  dp[i]=max(dp[i-3]+arr[i-1]+arr[i],dp[i-2]+arr[i])

print(dp[n])