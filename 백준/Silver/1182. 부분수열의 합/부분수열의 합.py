
#배열입력받기
n, s = map(int, input().split())
arr = list(map(int,input().split()))
cnt = 0
ans = []
def backtracking(start):
    global cnt
    if sum(ans) == s and len(ans)>0:
        cnt+=1

    for i in range(start, n):
        #지금 원소를 추가하는거
        ans.append(arr[i])
        backtracking(i+1)
        #빼버린다
        ans.pop()

backtracking(0)
print(cnt)