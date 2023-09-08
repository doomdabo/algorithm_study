import sys
read = sys.stdin.readline

n,m = map(int,read().split())
tree = list(map(int,read().split()))

tree.sort()
st,end = 1,tree[-1]
result = 0
while st<end:
  mid = (st+end)//2
  sum = 0
  for i in tree:
    if i > mid:
      sum += i - mid
  if sum < m:
    end = mid
  else:
    result = mid
    st = mid + 1
print(result)