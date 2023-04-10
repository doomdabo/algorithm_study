import sys

read = sys.stdin.readline
s = int(read())
ans = 0
for i in range(1,4294967295):
  ans+=i
  if ans>s:
    print(i-1)
    break

