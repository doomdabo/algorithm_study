#1541 잃어버린 괄호
str = input()
numlist = []
ck=0
temp=""
for i in str:
  if i.isdigit(): 
    temp+=i 
  else:
    numlist.append(int(temp))
    temp = ""
    numlist.append(i)
numlist.append(int(temp))
#print(numlist)

while '+' in numlist:
  idx = 0
  for i in numlist: 
    if i=='+':
      t = numlist[idx-1]+numlist[idx+1]
      numlist[idx]=t
      del numlist[idx+1]
      del numlist[idx-1]
    idx+=1

#AAprint(numlist)
idx = 0
ans = 0
for i in numlist:
  if idx ==0 :
    ans = i
  else:
    if i != '-':
      ans-=i
  idx+=1
print(ans)