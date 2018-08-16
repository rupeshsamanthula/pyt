a,b=input().split()
a=int(a)
b=int(b)
for i in range(a+1,b):
	if((i%2!=0) and (i<=10000)):
		print(i,end=" ")
