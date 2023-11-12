N,L,R,X = map(int,input().split())
arr = list(map(int,input().split()))

from itertools import combinations
ans = 0
for i in range(2,N+1):
    for j in combinations(arr,i):
        if L<=sum(j)<=R:
            if max(j)-min(j)>=X:
                ans+=1
print(ans)

