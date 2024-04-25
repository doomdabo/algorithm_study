s, c = map(int,input().split())
arr=[]
for _ in range(s):
    arr.append(int(input()))

#이진탐색..
st = 1
ed = max(arr)
mx = ed

while st<=ed:
    mid = (st+ed)//2
    cnt = 0 #지금까지 몇개가 저장됐나 확인
    for i in arr: #배열을 하나씩 돌면서 몇개나 들어갈 수 있나 확인하자
        pos = i // mid # 파가 440이고 mid가 116이라면 2가 저장
        cnt = cnt + pos # 몇개가 가능한지 저장
    if (cnt >= c): #만약 너무 많이 파가남아? 그럼 더 키워
        st = mid + 1
    elif cnt < c:
        ed = mid - 1
print(sum(arr)-c*ed)




