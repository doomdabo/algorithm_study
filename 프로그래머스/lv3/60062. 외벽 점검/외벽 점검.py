from itertools import permutations

def solution(n, weak, dist):
    #원형 -> 선형으로 바꾸는 과정에서 길이를 2배로 늘림. 시계, 반시계 방향으로 탐색하기 위해서 이 방법이 좋음
    #[1,5,6,10] -> [1,5,6,10,13,17,18,22]
    #10에서 시계 방향으로 1에 가려면 13(12+1)으로 이동하면 됨
    #10에서 반시계 방향으로 1에 가려면 1로 이동하면 됨
    weak2 = weak + [w+n for w in weak]
    friends_combi = list(permutations(dist,len(dist))) #dist에서 순서를 고려하여 len(dist)개 만큼 뽑는 모든 경우의 수를 friends_combi에 저장
    answer = len(dist) + 1 #투입할 친구의 최솟값을 찾아야 하므로 (현재 총 친구 수+1)를 정답으로 정해둠
    for start in range(len(weak)): #weak갯수만큼 반복
        for friends in friends_combi: #친구 목록 다 돌면서 확인
            f_cnt = 1 #투입된 친구 수 카운팅 위한 변수. 새로운 순열 시작할때마다 새로 리셋해줘야함
            pos = weak[start] + friends[f_cnt-1] #friend의 첫 친구가 점검 가능한 위치 확인: 현재 취약 위치좌표 + 이동할 수 있는 거리
            #시작점 부터 모든 취약 지점 전부 확인
            for i in range(start,start+len(weak)): 
                if pos<weak2[i]: #친구가 점검가능한 위치보다 취약점이 멀리 있다면
                    f_cnt+=1 #다른 친구를 투입
                    if f_cnt>len(dist): #친구 수보다 카운트가 많으면 전부 돌수있는 방법이 없으므로 다음으로 넘어감
                        break
                    pos = weak2[i] + friends[f_cnt-1] #현재 취약지점에서 다음 친구가 갈 수 있는 거리를 계산해 pos를 업데이트
            answer = min(answer, f_cnt)
            
    
    if answer > len(dist):
        answer = -1
    return answer