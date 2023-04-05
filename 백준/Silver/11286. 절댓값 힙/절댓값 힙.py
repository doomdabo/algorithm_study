import sys
import heapq
read = sys.stdin.readline
n = int(read())
hq=[]
for _ in range (n):
  x = int(read())
  if(x != 0): #x가 0이 아닌 경우
    heapq.heappush(hq,(abs(x),x)) #절대값,원래값 저장
  else: #x가 0인경우
    if hq: #비어있지 않은 경우
      print(heapq.heappop(hq)[1])#힙에서 값 뽑아서 출력
    else:
      print(0)