n,k = map(int,input().split())
ans=[]
sieve=[True]*(n+1) #모두 소수라 가정
for i in range(2,n+1):
  if sieve[i]==True:
    ans.append(i)
    for j in range(i+i,n+1,i):
      if sieve[j]==True:
        sieve[j]=False #배수는 소수가 아님
        ans.append(j)

print(ans[k-1])