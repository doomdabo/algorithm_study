
st = input()

a_num = st.count('a') #a 카운트
st = st+st
arr = st[0:a_num] #a의 갯수만큼 슬라이딩 윈도우 만들기
minn = arr.count('b')
for i in range(1,len(st)-a_num+1):
    arr = st[i:i+a_num]
    minn = min(minn, arr.count('b'))
print(minn)