from collections import deque
def devide(w):
    left = 0
    right = 0
    cnt = 0
    for i in w:
        cnt += 1
        if i == "(":
            left += 1
        elif i == ")":
            right += 1
        if left == right:
            return w[:cnt],w[cnt:]
    
def check(u): #올바른 괄호 문자열인지 체크
    #스택으로 구현
    dq = deque()
    for i in u:
        if i == '(':
            dq.append('(')
        else:
            if dq:
                dq.pop()
    if dq:
        return False
    else:
        return True
def solution(p):
    #1
    if not p:
        return ""
    #2
    u,v = devide(p)
    #3
    if check(u) == True:
        return u + solution(v)
    #4
    if check(u) == False:
        #4-1
        answer = "("
        #4-2
        answer += solution(v)
        #4-3
        answer += ")"
        #4-4
        u = u[1:len(u)-1]
        for i in u:
            if i == '(':
                answer += ')'
            else:
                answer += '('
        return answer