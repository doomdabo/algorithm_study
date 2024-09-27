N,M = map(int,input().split())
arr = list(map(int,input().split()))

#여기서 주의: m이 최대 300,000,000
#시간 제한은 0.5초임 -> n^2의 해결법은 안됨. -> 투포인터
#i번째수부터 j번째 수의 합이 m이 되는 경우의 수 구하기 -> 누적합


#일단 누적합을 구하는게 필요
acc = [0]
s = 0
for i in range(N):
    s += arr[i]
    acc.append(s)

st, end = 0,0
ans = 0
#누적합을 기준으로 계산
while st <= end and end<=N:
    summ = acc[end]-acc[st]
    if summ == M:
        ans += 1
        st += 1
    elif summ < M:
        end += 1
    elif summ > M:
        st += 1
print(ans)