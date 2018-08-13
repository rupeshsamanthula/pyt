n=int(input(""))
a=n
count=0
for i in range(1,n):
	if(n>0):
		
		n=n//10
		count+=1	
print(count,end="")
