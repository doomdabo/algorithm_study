import sys

read = sys.stdin.readline
n, m = list(map(int, read().split()))

num = list(map(int, read().split()))
arr = [0 for _ in range(m)]
num.sort()


def choose(k,start):
  if (k == m):
    print(" ".join(map(str, arr)))

  else:
    for i in range(start,n):
      arr[k] = num[i]
      choose(k + 1,i)


choose(0,0)
