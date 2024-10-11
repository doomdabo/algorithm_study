N, d, k, c = map(int,input().split())
arr = [int(input()) for _ in range(N)]
arr = arr*2
#print(arr)
ans = 0
sliding = arr[0:k]
for i in range(1,N+1):
    sliding = arr[i:i+k]
    sliding.append(c)
    sliding = set(sliding)
    ans = max(ans, len(sliding))
print(ans)