import sys

read = sys.stdin.readline
n, m = list(map(int, read().split()))

arr = [0 for _ in range(m)]


def choose(k,start):
  if (k == m):
    print(" ".join(map(str, arr)))  #숫자 다 모아졌으면 출력
      
  else:
    for i in range(start,n+1):
      arr[k] = i
      choose(k + 1,i)

choose(0,1)
