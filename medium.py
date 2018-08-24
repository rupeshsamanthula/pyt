n=int(input())
a=[int(x) for x in input().split()]
a.sort()
print(a)
if 1<=n<=10000:
	k=int((n+1)/2)
if(n%2==0):
	print(a[k-1],a[k])
else:
	print(a[k-1])
