n,k = map(int,input().split())
str = input()

ans = 0
check = [False] * n
for i in range(n):
    if str[i] == 'P': #사람이 오면
        for j in range(i-k,i+k+1):
            if j>=0 and j<n:
                if not check[j] and str[j]=='H':
                    check[j] = True
                    ans += 1
                    break
print(ans)
