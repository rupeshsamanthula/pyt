n=input()
c=0
for i in range(0,len(n)):
	if(n[i]!="." and n[i].isalnum()==False):
		c+=1
print(c,end="")
		
