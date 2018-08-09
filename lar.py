a,b,c=input("").split()
a=int(a)
b=int(b)
c=int(c)
if(a>b and a>c):
    print("big value is:",a)
elif(b>c and b>a):
    print("big value is:",b)
else:
    print("big value is:",c)
