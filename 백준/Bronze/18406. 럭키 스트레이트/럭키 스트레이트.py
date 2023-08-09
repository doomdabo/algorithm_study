import sys

read = sys.stdin.readline

N = read().rstrip()

strlen = int(len(N))

sum1 = 0
sum2 = 0
for i in range(strlen // 2):
  sum1 += int(N[i])
for i in range(strlen // 2, strlen):
  sum2 += int(N[i])
if sum1 == sum2:
  print("LUCKY")
else:
  print("READY")
