def divide(p):
    left = 0
    right = 0
    for i in range(len(p)):
        if p[i] == '(':
            left+=1
        else:
            right+=1
        if right==left: #좌괄호, 우괄호 수가 같으면
            return p[:i+1], p[i+1:]
            
def correct(u):
    stack = []
    for p in u:
        if p =='(':#좌괄호의 경우
            stack.append(p)
        else:#우괄호의 경우
            if not stack:#스택이 비어있는 경우 짝지을 좌괄호가 없으므로 올바른 괄호 문자열이 아님
                return False
            #짝지을 좌괄호가 있으면 
            stack.pop()
    return True
            
        
def solution(p):
    #1단계
    if not p: #p가 빈 문자열인 경우
        return ""
    #2단계
    u,v = divide(p)
    #3단계
    if correct(u)==True:
        #3-1단계
        return u+solution(v)
    #4단계
    if correct(u)==False:
        #4-1단계
        answer = "("
        #4-2단계
        answer += solution(v)
        #4-3단계
        answer += ")"
        #4-4단계
        u = u[1:len(u)-1]#첫번째, 마지막 문자 제거
        for p in u:
            if p =='(':
                answer += ')'
            else:
                answer += '('
        #4-5단계
        return answer

