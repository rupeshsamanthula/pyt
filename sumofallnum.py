a=int(input())
c=0
b=[int(x) for x in input().split()]
for i in range(0,a):
  c=c+b[i]
print(c,end="")
