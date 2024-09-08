n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

head = False
hx, hy = 0, 0
ans = []
for i in range(n):
    for j in range(n):
        if not head and arr[i][j] == '*': #일단 머리를 찾자
            hx = i+2
            hy = j+1 #심장의 위치 찾음
            head = True
    if head:
        print(hx,hy)
        break
ck1 = False
ck2 = False
st, ed = 0, 0
for i in range(n): #팔길이 구하기
    if not ck1 and arr[hx-1][i] == '*':
        st = i+1
        ck1 = True
    elif ck1 and (arr[hx-1][i] == '_'):
        ed = i
        break
    elif ck1 and i == n-1 and arr[hx-1][i-1] == '*':
        ed = i+1
ans.append(hy-st)
ans.append(ed-hy)

#허리길이 구하기
waist = 0
for i in range(hx,n):
    if arr[i][hy-1] == '*':
        waist +=1
ans.append(waist)
#다리길이 구하기
left, right = 0,0
for i in range(hx+waist,n):
    if arr[i][hy-2] == '*':
        left += 1
    if arr[i][hy] == '*':
        right += 1
ans.append(left)
ans.append(right)
for i in range(5):
    print(ans[i],end=' ')

#머리 심장 허리 좌우팔 다리 - 빨간색이 심장 . 머리는 심장 바로 윗칸 1칸 크기로 있음.
#왼쪽 팔은 심장 바로 왼쪽 오른쪽 팔은 심장 바로 오른쪽. 허리는 심장 바로 아래쪽. 왼쪽다리 허리 아래

#심장위치, 팔, 다리, 허리 길이 구하기