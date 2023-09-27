dx = [-1,1,0,0] #위 아래 왼 오
dy = [0,0,-1,1]
#변수 입력 받기
n,m,k = map(int,input().split()) #n은 보드,m은 상어수,k번 이동후 냄새 사라짐
#격자 입력 받기: 0은 빈칸, 0이 아닌 수 x: x번 상어가 들어있는 칸
board = [list(map(int,input().split())) for _ in range(n)]
#상어 방향
s_dir = list(map(int,input().split()))
shark = [[] for _ in range(m)]
#상어의방향 우선순위
priority = [[] for _ in range(m)]
for i in range(m): #상어별로
    for j in range(4): #4번씩
        priority[i].append(list(map(int,input().split()))) #1번 위/2번 아래/3번 왼/4번 오
for i in range(n):
    for j in range(n):
        if board[i][j] != 0: #상어번호:x좌표,y좌표,상어방향
            shark[board[i][j]-1] = [i,j,s_dir[board[i][j]-1]-1]
        board[i][j]=[0,0] #격자값 초기화

second = 0
def smell(board,shark):
    #냄새 남기기
    for i in range(len(shark)):
        if shark[i]:
            x,y,dir = shark[i]
            board[x][y] = [k,i] #상어 번호,시간 저장
    return board
def move(shark):
    #이동하기
    left_shark = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(len(shark)):
        if shark[i]:
            x,y,dir = shark[i]
            no_smell = [] #냄새 없는경우
            my_smell = [] #비어있는 경우
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny][0] == 0: #냄새 없으면
                        no_smell.append((nx,ny,d))
                    elif board[nx][ny][1] == i: #내냄새있으면
                        my_smell.append((nx,ny,d))
            new_d = dir #상어 다음 방향 정하기
            if not no_smell:#옆에 냄새없는거 없다?
                no_smell = my_smell #빈자리 없으면 최종 후보는 내 냄새 남은곳
            if len(no_smell)>=2: #후보 여러개?
                for r in priority[i][dir]:
                    check = 0
                    for a,b,c in no_smell:
                        if c == r-1:
                            new_d = r-1
                            check = 1
                            break
                    if check==1:
                        break
            else: #후보군 하나
                new_d = no_smell[0][2]

            shark[i] = [x+dx[new_d],y+dy[new_d],new_d] #상어 정보 업뎃
            left_shark[x+dx[new_d]][y+dy[new_d]].append(i)
    for i in range(n):
        for j in range(n):
            if len(left_shark)>1:
                left_shark[i][j].sort()
                idx = 0
                for ls in left_shark[i][j]:
                    if idx != 0:
                        shark[ls] = []
                    idx+=1
    cnt = 0
    for i in range(m):
        if shark[i] != []:
            cnt+=1
    return shark,cnt

def next(board):
    for i in range(n):
        for j in range(n):
            if board[i][j][0]>0:
                board[i][j][0]-=1
    return board
while True:
    second += 1
    if second>1000:
        second = -1
        break
    #1번상어만 있으면 탈출
    board = smell(board,shark)
    shark,live = move(shark)
    board = next(board)
    if live==1:
        break

print(second)

