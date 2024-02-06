from itertools import permutations
n = int(input())
a = list(map(int,input().split()))
ans = -1
for i in permutations(a,n):
  sum = 0
  for j in range(n-1):
    sum+=abs(i[j]-i[j+1])
  ans = max(sum,ans)
print(ans)