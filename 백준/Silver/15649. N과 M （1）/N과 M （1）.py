n,m = map(int,input().split())

#1부터 n까지 자연수 중에서 중복 없이 m개를 고른 수열

arr = [i+1 for i in range(n)]
temp = []
vis = [False] * (n+1)
cnt = 0
def func(cnt):
    if cnt == m:
        for i in temp:
            print(i,end=' ')
        print()

    else:
        for i in arr:
            if not vis[i]:
                temp.append(i)
                vis[i] = True
                func(cnt+1)
                temp.pop()
                vis[i] = False


func(0)