import sys

read = sys.stdin.readline
n,m = list(map(int,read().split()))

#1~n까지 자연수 중 중복없이 m개를 고르는 수열
#고른 수열은 오름차순

vis=[0 for _ in range(n+1)]
arr=[0 for _ in range(m)]
def choose(k,start): #현재까지 k개의 숫자를 선택, 시작 숫자
  if(k == m):
    print(' '.join(map(str, arr)))

  else:
    for i in range(start,n):
      if(vis[i] == 0):
        vis[i] = 1
        arr[k] = i+1
        choose(k+1,i+1)
        vis[i] = 0
  
choose(0,0)
  