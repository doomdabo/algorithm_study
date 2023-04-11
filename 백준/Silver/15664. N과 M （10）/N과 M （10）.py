import sys

read = sys.stdin.readline
n, m = list(map(int, read().split()))

num = list(map(int, read().split())) #입력받은 수 저장

arr = [0 for _ in range(m)]
vis = [0 for _ in range(n)]

num.sort()
def choose(k,start):
  if (k == m):
    print(" ".join(map(str, arr)))
  else:
    temp = 0
    for i in range(start,n):
      if(vis[i]==0 and temp != num[i]):
        vis[i] = 1
        arr[k] = num[i]
        temp = num[i]
        choose(k + 1,i)
        vis[i] = 0


choose(0,0)
