n=int(input())
a=[int(x) for x in input().split()]
a.sort()
for i in range(0,n):
	if i<n-1:
		k=" "
	else:k=''
	print(a[i],end=" ")
