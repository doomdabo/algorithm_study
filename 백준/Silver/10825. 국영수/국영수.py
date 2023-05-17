import sys

read = sys.stdin.readline
n = int(read())
arr = []
for i in range(n):
  temp = read().strip().split()
  arr.append((temp[0],int(temp[1]),int(temp[2]),int(temp[3])))

arr.sort(key = lambda x:(-x[1],x[2],-x[3],x[0]))

for i in arr:
  print(i[0])
