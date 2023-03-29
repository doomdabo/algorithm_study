import sys
read = sys.stdin.readline
n = int(read())
t=[]
p=[]
dp = [0 for _ in range(n+1)]
for _ in range(n):
  a,b = map(int,read().split())
  t.append(a)
  p.append(b)

for i in range(n-1,-1,-1): #뒤에서부터 거꾸로 계산
  if t[i] + i > n: #상담에 필요한 일수가 퇴사일보다 크면 해당 상담은 진행할 수 없으므로 다음날 값을 그대로 가져 옴
    dp[i] = dp[i+1]
  else: #상담이 가능한 경우 
    dp[i] = max(dp[i+1],dp[t[i]+i]+p[i])
    #상담을 진행하지 않는 경우: dp[i+1]
    #상담을 진행하는 경우: dp[t[i]+i]+p[i] 
print(dp[0])