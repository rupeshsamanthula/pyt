a,b=map(int,input().split())
c=[int(x) for x in input().split()]
for i in range(1,a+1):
  if(b==i):
    print(c[i-1],end="")
    
