n=int(input(""))
count=0
for i in range(2,n):
	if(n%i==0):
		count+=1
		break
if(count==0):
	print("yes",end="")
else:
	print("no",end="")
