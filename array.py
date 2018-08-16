m,n=input().split()
m=int(m)
n=int(n)
d=0
a=[int(x) for x in input().split()]
for i in range(0,n):
	d+=a[i]
print(d,end="")
