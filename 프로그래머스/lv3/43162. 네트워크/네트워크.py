from collections import deque


def solution(n, computers):
    answer = 0
    vis = [False]*n
    for i in range(n): #컴퓨터 개수만큼 순회
        if(vis[i] == False): #i번째 방문 안했으면
            answer+=1
            dq = deque()
            dq.append(i) #큐에 넣고 
            vis[i] = True #방문 표시
            while(dq):
                v = dq.popleft()
                for j in range (n):
                    if(vis[j]==False and computers[v][j]==1):
                        dq.append(j)
                        vis[j] = True
    return answer
