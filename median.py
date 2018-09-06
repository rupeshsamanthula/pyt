a=int(input())
b=[int(x) for x in input().split()]
while(len(b)>a):
  n=int(input())
  b.append(n)
c=0
e=0
for i in b:
  c=c+i
  e+=1
d=c//e
print(d)
