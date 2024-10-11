from collections import defaultdict
import sys
input = sys.stdin.readline
N, d, k, c = map(int,input().split())
arr = [int(input()) for _ in range(N)]
arr = arr*2
dic = defaultdict(int)
ans = 0
left = 0
right = k
dic[c] += 1 #보너스는 걍 먹기
for i in range(k): #처음에 k개 먹기
    dic[arr[i]] += 1
while right < len(arr):
    ans = max(len(dic),ans)
    #왼쪽 초밥 제거
    dic[arr[left]]-=1
    if dic[arr[left]]==0: #만약에 더이상 그스시없으면 그냥 지워
        del dic[arr[left]]
    left += 1
    dic[arr[right]]+=1
    right += 1
print(ans)

