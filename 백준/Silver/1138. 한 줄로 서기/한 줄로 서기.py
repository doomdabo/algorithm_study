n = int(input())
ori = list(map(int,input().split()))

vis =[False]*n
ans = [0]*n
for i in range(n):
  cnt = 0 #몇번 앞으로 갔는지 체크
  j = 0
  while True:
    if vis[j] == False:
      if cnt==ori[i]:
        vis[j] = True
        break
      cnt+=1
      
    j+=1
  ans[j] = i+1

#print(ans)
for i in ans:
  print(i,end=' ')