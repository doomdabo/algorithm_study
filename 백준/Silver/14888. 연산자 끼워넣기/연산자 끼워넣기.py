import sys
from collections import deque
read = sys.stdin.readline
n = int(read())
arr = list(map(int, read().split()))
op = list(map(int, read().split())) #순서대로 +, -, x, //

maxi = -1e10 #젤 작은 수로 초기화 해두고 이거보다 큰거 나오면 새로 업데이트
mini = 1e10 #젤 큰 수로 초기화 해두고 이거보다 작은거 나오면 새로 업데이트
def dfs(depth, result, op):
  global mini, maxi
  if depth == n: #마지막 수까지 계산이 끝났다면?
    mini = min(mini, result)#minimum 업데이트
    maxi = max(maxi, result)#maximum 업데이트
  else: #아직 마지막 수가 아니라면
    if op[0] > 0: #+를 아직 쓸 수 있다면
      op[0] -= 1 #+를 한번 쓰고
      dfs(depth+1, result + arr[depth], op) #dfs한 다음
      op[0] += 1
    if op[1] > 0:
      op[1] -= 1
      dfs(depth+1, result - arr[depth], op)
      op[1] += 1
    if op[2] > 0:
      op[2] -= 1
      dfs(depth+1, result * arr[depth], op)
      op[2] += 1
    if op[3] > 0:
      op[3] -= 1
      dfs(depth+1, int(result / arr[depth]), op)
      op[3] += 1

dfs(1,arr[0], op)
print(int(maxi))
print(int(mini))
