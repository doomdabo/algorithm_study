n = int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
arr = sorted(arr,key = lambda x:-x)
ans = 0
k = 0

for i in range(len(arr)):
    k+=1
    temp = arr[i]*(i+1)
    if ans<temp:
        ans=temp
print(ans)


