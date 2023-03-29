import sys

read = sys.stdin.readline
n = int(read())
cnt = 0
for i in range(6670000):
  if '666' in str(i):
    cnt+=1

  if n == cnt:
    print(i)
    break
  