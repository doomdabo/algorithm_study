#뒤집기
s = input()
st=''
cnt = [0,0]
for i in range(len(s)):
    if i==0:
        st = s[i]
        cnt[int(st)]+=1
    else:
        if s[i] == st:
            continue
        else:
          cnt[int(s[i])]+=1
          st = s[i]
print(min(cnt))



