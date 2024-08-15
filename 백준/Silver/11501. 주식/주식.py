T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int,input().split()))

    total_plus = 0
    maxx = 0
    for i in range(n-1,-1,-1): #맨 뒤에부터 접근
        #maxx값보다 크면 maxx를 갱신
        if maxx<arr[i]:
            maxx = arr[i]
        else:
            #maxx보다 작은경우 사야지~
            total_plus += maxx - arr[i]


    print(total_plus)