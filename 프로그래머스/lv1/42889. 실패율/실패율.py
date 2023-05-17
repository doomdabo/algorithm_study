def solution(N, stages):
    answer = []
    arr = []
    k = len(stages) #전체 사람의 수

    for i in range(1,N+1): #N개의 스테이지에 대해 조사
        fail = 0
        for j in range(len(stages)): 
            if i == stages[j]:
                fail+=1
        if fail != 0:
            fail_percent = fail/k
            arr.append((i,fail_percent))
        else:
            arr.append((i,0))
        k-= fail #실패 유저들을 빼서, 스테이지에 도달한 플레이어 수를 업데이트 해줌
            
    arr=sorted(arr,key = lambda x:-x[1])
    for i in arr:
        answer.append(i[0])
    return answer

