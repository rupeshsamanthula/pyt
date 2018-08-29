a=input()
b=0
for i in range(0,len(a)):
	if(a[i].isnumeric()):
		b+=1
print(b,end="")
