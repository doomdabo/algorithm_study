import sys
from collections import deque

read = sys.stdin.readline
n, k = map(int, input().split())
belt = deque(list(map(int, read().split())))
robot = deque([0] * n)
ans = 0
while (1):
  ans += 1  #단계+1
  belt.rotate(1)  #1단계: 벨트가 한 칸 회전
  robot.rotate(1)  #2단계: 로봇과 함께 한 칸 회전
  robot[-1] = 0  # 내리는 위치에 도달한 경우, 즉시 내림
  for i in range(n - 2, -1, -1):  #맨 뒤에서 두번째, 즉 먼저 올라간 로봇부터 한칸 갈 수 있다면 이동
    if (robot[i] == 1 and belt[i + 1] >= 1 and robot[i + 1] == 0):
      #해당 칸에 로봇이 있고, 이동하려는 칸 내구도 1이상, 로봇 없으면 이동
      robot[i + 1] = 1
      robot[i] = 0
      belt[i + 1] -= 1
  robot[-1] = 0  #로봇이 있으면 0으로 바꿔줌
  if belt[0] >= 1 and robot[0] == 0:  #0번째 벨트에 내구도 있고, 로봇이 없으면
    robot[0] = 1  #로봇 올리고
    belt[i] -= 1 #내구도 1빼기
  if belt.count(0) >= k:
    break
print(ans)