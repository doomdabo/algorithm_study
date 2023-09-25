# 4*4 크기의 공간
# 한 칸에는 물고기 한마리 존재
# 물고기 번호는 1~16 서로 다 다름. 방향은 상하좌우, 대각선 8가지
# 상어가 물고기 먹음 -> (0,0)에서 시작. (0,0)에 있던 물고기 먹고 방향 물고기 방향으로 전환
####### 이후 물고기 이동 시작 ###########
# 번호 작은 물고기부터 이동. 한칸 이동.
# 이동 가능한 칸: 빈칸, 다른 물고기 있는칸.
# 이동 불가 칸: 상어 있거나 공간 경계 넘는 칸
# 방향이 이동할 수 있는 칸을 향할때 까지 방향 45도 반시계 회전
# 이동할 수 있는 칸 없으면 이동X
# 그 외 경우 그 칸으로 이동. 물고기가 다른 물고기 있는 칸으로 이동할 때는 서로 위치 바굼
###### 물고기 이동 끝나면 상어 이동#################
# 상어는 방향에 있는 칸으로 이동 가능, 여러개의 칸 한번에 이동 가능
# 상어가 물고기 있는 칸으로 이동했으면 그 칸의 물고기 먹고 그 방향 가짐.
# 이동하는 중 지나가는 칸의 물고기 먹지 않음. 물고기 없으면 이동 불가.
# 이동할 수 있는 칸 없으면 상어 집으로 감..
# 상어 이동 후 다시 물고기 이동
#이 과정 계속 반복 ->상어가 먹을 수 있는 물고기 번호의 합 최댓값?
import copy

#방향 정보 저장 위쪽 방향부터 45도 방향 반시계 방향
d = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
#입력받기 -> 물고기 정보
board1 = [[] for _ in range(4)]
for i in range(4):
    arr = list(map(int,input().split()))
    k=0
    for j in range(4):
        board1[i].append([arr[k],arr[k+1] -1])
        k += 2
#현재 상어의 위치, 방향 (s_dir) 저장할 변수 필요
max_score = 0
def dfs(sx,sy,score,board):
    global max_score
    score += board[sx][sy][0] #냅다 물고기 먹기
    board[sx][sy][0] = -1 #상어가 물고기를 먹고 없어짐
    max_score = max(max_score,score) #최대 점수 구하기
    #물고기 움직임
    for f in range(1,17): #1번 물고기부터 16번 물고기까지 이동
        fx , fy = -1, -1
        for x in range(4): #4*4판을 돌면서 f번째 물고기를 찾음
            for y in range(4):
                if board[x][y][0] == f: #i번째 물고기를 찾았으면?
                    fx,fy = x,y #위치를 저장해둠
                    break
        #다 찾았는데 물고기가 없어..?
        if fx==-1 and fy==-1:
            continue #다음 물고기로 넘어가
        #물고기가 있으면 방향을 판단하고 위치를 바꿔야지
        dir = board[fx][fy][1] #처음 방향

        while True:
            nx = fx + d[dir][0]
            ny = fy + d[dir][1]
            #이동할 수 있을 때까지 방향을 돌려
            #이동할 수 없음: 상어 있거나 공간 넘는거
            if (0<=nx<4 and 0<=ny<4) and not (nx==sx and ny==sy):
                break #이동할 수 있으면 이동하러 가자
            else: #이동 못하면 방향을 바꾸자
                dir = (dir+1)%8
        # for i in range(8):
        #     nd = (dir + i) % 8
        #     nx = fx + d[nd][0]
        #     ny = fy + d[nd][1]
        #     if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == sx and ny == sy):
        #         continue
        #     board[fx][fy][1] = nd
        #     board[fx][fy], board[nx][ny] = board[nx][ny], board[fx][fy]
        #     break
        #이제 방향을 선정했으니 방향 값 바꿔주고
        board[fx][fy][1] = dir
        #해당 위치에 있는 물고기랑 위치를 바꾸자
        board[nx][ny],board[fx][fy] = board[fx][fy],board[nx][ny]
        #물고기 위치 1번 바꾸는 것 까지 코드 짬

        #물고기가 모두 이동! 이제 상어 이동할 차례
        #############################
        #print(board)
    s_dir = board[sx][sy][1]  # 상어의 방향
    # for _ in range(3):
    #     nx = sx + d[s_dir][0]
    #     ny = sy + d[s_dir][1]
    #     if (0<=nx<4 and 0<=ny<4) and board[nx][ny][0]>0:
    #         dfs(nx,ny,score,copy.deepcopy(board))
    for i in range(1, 5):
        nx = sx + d[s_dir][0]*i
        ny = sy + d[s_dir][1]*i
        if (0<= nx < 4 and 0<= ny < 4) and board[nx][ny][0] > 0:
            dfs(nx, ny, score, copy.deepcopy(board))
dfs(0,0,0,board1)
print(max_score)
