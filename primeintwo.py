n,k=input().split()
n=int(n)
k=int(k)
count=0
for i in range(n,k):
	temp=i
	b=0
	#for j in range(0,i):
	while(temp!=0):
		a=temp%10
		b+=a**3
		temp=temp//10
	if(i==b):
		count+=1
		if(count==1):
			k=''
		else:
			k=" "
		print(end=k)
		print(i,end="")
