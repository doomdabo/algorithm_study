import sys

read = sys.stdin.readline
n,m = list(map(int,read().split()))

#1~n까지 자연수 중 중복없이 m개를 고르는 수열

#1~n까지 자연수 담은 배열 만들기
vis=[0 for _ in range(n+1)]
arr=[0 for _ in range(n+1)]
def choose(k): #현재까지 k개의 숫자를 선택
  if(k == m):
    for i in range(m):
      print(str(arr[i])+" ",end="")
    print()
  else:
    for i in range(n):
      if(vis[i] == 0):
        vis[i] = 1
        arr[k] = i+1
        choose(k+1)
        vis[i] = 0
  
choose(0)
  