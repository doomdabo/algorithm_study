import sys
input = sys.stdin.readline
n,m = map(int,input().split())

arr = {}
for i in range(n):
    word = input().rstrip()
    if len(word)<m:
        continue

    else:
        if word in arr:
            arr[word] += 1
        else:
            arr[word] = 1
arr = sorted(arr.items(), key = lambda x: (-x[1],-len(x[0]),x[0]))
for i in arr:
    print(i[0])

