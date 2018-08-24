a=int(input())
b=0
nm=a
for i in range(0,a+1):
	if(i%60==0 and i>=60):
		b+=1
		nm-=60
print(b,nm,end="")
