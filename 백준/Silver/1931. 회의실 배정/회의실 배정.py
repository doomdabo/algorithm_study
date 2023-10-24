n = int(input())
arr = []
ans = 0
for i in range(n):
    a,b = map(int,input().split())
    arr.append((a,b))
#끝나는 시간 기준으로 정렬
arr= sorted(arr, key=lambda x:(x[1],x[0]))
st = 0
end = 0
for i in arr:
    if i[0]>=end:
        end = i[1]
        ans+=1
print(ans)
