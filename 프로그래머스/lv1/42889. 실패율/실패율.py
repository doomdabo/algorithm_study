def solution(N, stages):
    answer = []
    for i in range(1,N+1):
        mo = 0 #분모 - 스테이지에 도달한 플레이어 수
        ja = 0 #분자 - 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수
        for stage in stages:
            if stage>=i: #스테이지에 도달한 플레이어 수
                mo += 1
                if stage == i :
                    ja += 1
        fail = 0
        if mo != 0:
            fail = ja/mo
        answer.append((fail,i))
    answer = sorted(answer,key = lambda x:(-x[0],x[1]))
    arr = []
    for i in answer:
        arr.append(i[1])
    return arr
        