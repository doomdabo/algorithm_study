import sys

read = sys.stdin.readline
n, m = list(map(int, read().split()))
num = list(map(int,read().split()))
arr = [0 for _ in range(m)]
vis = [0 for _ in range(n)]
num.sort()
def choose(k):
  if (k == m):
    print(" ".join(map(str, arr)))  #숫자 다 모아졌으면 출력
      
  else:
    for i in range(n):
      if(vis[i]==0):
        vis[i] = 1
        arr[k] = num[i]
        choose(k + 1)
        vis[i] = 0

choose(0)
