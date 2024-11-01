n, new_score, p = map(int,input().split())
if n>0:
    rank = list(map(int,input().split()))
    #n이 0이상일때만
    if len(rank) == p and rank[-1]>=new_score: #이미 꽉차있는데 점수 낮으면 그냥 -1 출력
        print(-1)
        exit(0)
    rank.append(new_score)
    rank = sorted(rank)
    rank.reverse()
    if len(rank)>p: #추가했는데 길이가 더 길어? 그럼 잘라야해
        rank = rank[:p]
    print(rank.index(new_score)+1)



else:
    print(1)
