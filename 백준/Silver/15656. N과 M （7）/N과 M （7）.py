import sys

read = sys.stdin.readline
n, m = list(map(int, read().split()))

num = list(map(int, read().split()))
arr = [0 for _ in range(m)]
num.sort()


def choose(k):
  if (k == m):
    print(" ".join(map(str, arr)))

  else:
    for i in range(n):
      arr[k] = num[i]
      choose(k + 1)


choose(0)
