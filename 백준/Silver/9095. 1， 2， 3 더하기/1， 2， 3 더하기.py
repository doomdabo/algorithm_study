import sys
read = sys.stdin.readline

#1,2,3더하기

t = int(read())

arr = [0 for _ in range(12)]
arr[1] = 1
arr[2] = 2
arr[3] = 4
for i in range(4, 12):
    arr[i] = arr[i-1] + arr[i-2] + arr[i-3]
for _ in range(t):
    n = int(read())
    print(arr[n])

    