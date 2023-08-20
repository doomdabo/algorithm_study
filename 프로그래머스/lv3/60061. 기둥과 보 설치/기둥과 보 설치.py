def check(answer):
    for x,y,a in answer:
        if a == 0: #기둥의 경우
            #기둥이 바닥에 있거나/보한쪽끝부분위(2가지)/다른 기둥 위
            if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            return False #위 경우가 아니면 False 리턴함
        else: #보의 경우
            #한쪽 끝 부분이 기둥 위(2가지)/양쪽 끝 부분이 다른 보와 동시에 연결
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            return False
    return True
def solution(n, build_frame):
    answer = []
    for build in build_frame:
        x,y,a,b = build
        if b == 0: #삭제인 경우
            answer.remove([x,y,a])
            if(check(answer) == False): #삭제가 불가능한 경우
                answer.append([x,y,a]) #다시 설치해야함
        else: #설치하는 경우
            answer.append([x,y,a])
            if(check(answer) == False): #설치가 불가능한 경우
                answer.remove([x,y,a])
    answer.sort()
    return answer