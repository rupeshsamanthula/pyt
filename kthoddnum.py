a,b=map(int,input().split())
c=[int(x) for x in input().split()]
s=0
for i in range(0,a):
  if(c[i]%2)!=0:
    s+=1
  if(b==s):
    print(c[i],end="")
    break
