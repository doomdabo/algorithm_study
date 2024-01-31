
n = int(input())
r = []
ans = [0]*n
for i in range(n):
  s = input()
  r.append(s)
#print(r)

for i in range(n):
  for j in range(n):
    if r[i][j] == 'Y':
      ans[i] += 1
    elif i!=j:
      for k in range(n):
        if r[i][k] == 'Y' and r[j][k] == 'Y':
          ans[i] += 1
          break
print(max(ans))