temp = []
def func(arr,cnt,st):
    if cnt == 6:
        for j in temp:
            print(j,end = ' ')
        print()
    else:
        for i in range(st,len(arr)):
            if arr[i] not in temp:
                temp.append(arr[i])
                func(arr, cnt+1, i)
                temp.pop()


while True:
    arr = list(map(int,input().split()))
    if arr[0] == 0:
        break
    func(arr,0,1)
    print()



