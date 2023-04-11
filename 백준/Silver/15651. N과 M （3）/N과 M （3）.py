import sys
read = sys.stdin.readline
n,m = list(map(int,read().split()))

vis = [0 for _ in range(n+1)]
arr = [0 for _ in range(m)]
def choose(k):
  if(k==m):
    print(" ".join(map(str,arr))) #숫자 다 모아졌으면 출력

  else:
    for i in range(1,n+1):
      arr[k] = i
      choose(k+1)


choose(0)