a,b = map(int,input().split())

sieve = [True]*(b+1)
for i in range(2,b+1):
  if sieve[i]==True:
    for j in range(i+i,b+1,i):
      sieve[j] = False

prime=[i for i in range(2,b+1) if sieve[i]==True]
#print(prime)
ans=[]

# for i in range(a,b+1):
#   cnt=0
#   k = i
#   while True:
#     if k in prime:
#       cnt+=1
#       break
#     for j in prime:
#       if k%j==0: #나눠 떨어지면
#         k = k//j
#         cnt+=1
#         break
#   #print(i,cnt)
#   ans.append(cnt)
dp=[0]*(b+1)
for i in range(2,b+1):
  for j in prime:
    if i%j==0:
      dp[i]=dp[i//j]+1
      break
#print(dp)
#print(ans)
realans=0
for i in range(a,b+1):
  if dp[i] in prime:
    realans+=1
print(realans)
  