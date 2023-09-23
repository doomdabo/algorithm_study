from collections import deque

n = int(input())
n2 = n * n
arr = []
board = [[0]*n for _ in range(n)]
for _ in range(n2):
    a,b,c,d,e = map(int,input().split())
    arr.append([a,[b,c,d,e]])

dx = [1,0,-1,0]
dy = [0,1,0,-1]

for num in range(n2):
    #입력 받은 순서대로 하나씩 체크
    #가장 먼저 첫번째 거 테스트
    candidate = []

    r = arr[num][1] #여기에 좋아하는 친구들 담겨있음
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                like = 0
                empty = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx>=n or ny>=n or nx<0 or ny<0:
                        continue
                    if board[nx][ny] == 0:
                        empty+=1
                    if board[nx][ny] in r:
                        like += 1
                candidate.append((like,empty,i,j))
    candidate = sorted(candidate, key=lambda x:(-x[0],-x[1],x[2],x[3]))
    board[candidate[0][2]][candidate[0][3]] = arr[num][0]
#만족도 계산
ans = 0
for i in range(n):
    for j in range(n):
        cnt =0
        for d in range(4):
            nx = i+dx[d]
            ny = j+dy[d]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            for k in range(n2):
                if arr[k][0] == board[i][j]:
                    if board[nx][ny] in arr[k][1]:
                        cnt+=1
        if cnt!=0:
            ans += 10**(cnt-1)
print(ans)

