# your code goes here
n=int(input(""))
sum=0
a=n
while(n>0):
	rem=n%10
	sum+=rem**3
	n=n//10
if(a==sum):
	print("yes")
else:
        print("no")
