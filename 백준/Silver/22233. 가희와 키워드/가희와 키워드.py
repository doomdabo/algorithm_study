import sys
input = sys.stdin.readline
n,m = map(int,input().split())
dict = {}

for _ in range(n):
    dict[input().rstrip()] = 1
cnt = n
for _ in range(m):
    blog = list(map(str,input().rstrip().split(',')))

    for a in blog:
        if a in dict:
            cnt-=1
            del(dict[a])
    print(cnt)
