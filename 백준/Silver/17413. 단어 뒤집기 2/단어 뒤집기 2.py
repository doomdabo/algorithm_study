s = input()
ans = ""
ck=0
temp = ""
temp2=""
for i in range(len(s)):
    if s[i] == '>':
        ck=0
        ans+=s[i]
        continue
    if ck == 1:
        ans += s[i]
        continue
    if s[i]=='<':
        if temp:
            for j in temp:
                temp2 = j + temp2
            ans += temp2
            temp = ""
            temp2 = ""
        ck=1
        ans+=s[i]
        continue
    if s[i]==' ':
        for j in temp:
            temp2=j+temp2
        ans+=temp2+" "
        temp=""
        temp2=""
        continue
    else:
        temp+=s[i]
if temp:
    for j in temp:
        temp2 = j + temp2
    ans += temp2
print(ans)