a=int(input())
b=0
for i in range(0,a):
	if(i%60==0 and i>=60):
		b+=1
print(b,a)
