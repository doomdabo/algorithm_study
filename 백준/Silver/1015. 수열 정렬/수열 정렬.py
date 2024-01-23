n = int(input())
a = list(map(int,input().split()))

s_a= sorted(a)

ans = []
for i in a:
    ans.append(s_a.index(i)) # i가 s_a의 몇번째 인덱스인지 찾아서 ans에 저장
    s_a[s_a.index(i)]=-1 #해당 숫자 -1로 바꿔서 재탐색 가능하게!
for i in ans:
    print(i,end=' ')