a=int(input())
c=0
for i in range(0,a):
	c+=a%10
	a=a//10
print(c,end="")
	
