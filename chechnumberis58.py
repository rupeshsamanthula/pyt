n,m=map(int,input().split())
lst=[int(x) for x in input().split()]
c=0
for i in range(0,n):
  if m==lst[i]:
    print("yes",end="")
    break
else:print("no",end="")
