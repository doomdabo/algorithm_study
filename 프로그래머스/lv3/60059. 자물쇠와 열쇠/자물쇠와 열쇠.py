def rotation90(m, key): #90도 회전하는 함수
    newkey = [[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            newkey[i][j] = key[m-j-1][i]
    return newkey

def check(n, extend_lock):
    for i in range(n,n*2):
        for j in range(n,n*2):
            if extend_lock[i][j] != 1:
                return False
    return True
            
def put(i,j,m,newkey,extend_lock):
    for p in range(m):
        for q in range(m):
            extend_lock[i+p][j+q] += newkey[p][q]
def reset(i,j,m,newkey,extend_lock):
    for p in range(m):
        for q in range(m):
            extend_lock[i+p][j+q] -= newkey[p][q]
            
def solution(key, lock):
    m = len(key) #key의 길이 m 구하기 
    n = len(lock) #lock의 길이 n 구하기
    
    #lock을 3배 확장하고 가운데에 자물쇠 배치#
    extend_lock = [[0]*(n*3) for _ in range(n*3)] #확장 
    #자물쇠 배치
    for i in range(n):
        for j in range(n):
            extend_lock[i+n][j+n] = lock[i][j]
    newkey = rotation90(m,key)                  
    for _ in range(4): #4번 회전
        for i in range(1,n*2):
            for j in range(1,n*2):
                put(i,j,m,newkey,extend_lock)
                if check(n,extend_lock):
                    return True
                reset(i,j,m,newkey,extend_lock)
        newkey = rotation90(m,newkey)        
        
    return False

    
