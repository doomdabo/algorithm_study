n=int(input())

arr = [0]*10001
for i in range(1,n+1):
  arr[i]=int(input())
#OOOX의 경우: dp[i-1]
#OXOO의 경우: dp[i-3]+arr[i-1]+arr[i]
#OOXO의 경우: dp[i-2]+arr[i]

dp=[0]*10001
if n==1:
  print(arr[1])
elif n==2:
  print(arr[1]+arr[2])
else:
  dp[1]=arr[1]
  dp[2]=arr[1]+arr[2]
  for i in range(3,n+1):
    dp[i]=max(dp[i-1],dp[i-3]+arr[i-1]+arr[i],dp[i-2]+arr[i])
  
  print(max(dp))
  