import sys

read = sys.stdin.readline
n, m = list(map(int, read().split()))

num = list(map(int, read().split())) #입력받은 수 저장

arr = [0 for _ in range(m)]

num.sort()
def choose(k):
  if (k == m):
    print(" ".join(map(str, arr)))
  else:
    temp = 0
    for i in range(n):
      if(temp != num[i]):
        arr[k] = num[i]
        temp = num[i]
        choose(k + 1)



choose(0)
