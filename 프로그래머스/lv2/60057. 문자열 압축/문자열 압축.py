def solution(s):
    answer = []
    for i in range(1,len(s)+1):
        b = ""
        cnt = 1
        temp = s[:i] #첫번째
        for j in range(i, len(s)+i, i): #i부터 끝까지 i단위로 나눠서 탐색
            if temp==s[j:i+j]:#앞에랑 같은 경우
                cnt+=1
            else:
                if cnt!=1: #앞에서 중복이 있으면
                    b = b+str(cnt)+temp #원래 글자 + 개수 + 줄일 문자
                else:
                    b = b+temp #중복 없었으면 개수 없이 그냥 문자만 저장
                temp = s[j:j+i]
                cnt = 1
        answer.append(len(b))
        
    
    return min(answer)