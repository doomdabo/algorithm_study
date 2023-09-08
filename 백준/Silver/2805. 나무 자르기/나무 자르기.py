import sys
read = sys.stdin.readline

n,m = map(int,read().split())
tree = list(map(int,read().split()))

tree.sort()
st,end = 1,tree[-1]
result = 0
while st<=end:
  mid = (st+end)//2
  sum = 0
  for i in tree: # for i in range(len(tree)): 이렇게 하면 python통과 못함..
    if i > mid:
      sum += i - mid
  if sum < m:
    end = mid -1
  else:
    result = mid
    st = mid + 1
print(result)