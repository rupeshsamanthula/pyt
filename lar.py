a,b,c=int(input("")).split()
if(a>b and a>c):
    print("big value is:",a)
elif(b>c and b>a):
    print("big value is:",b)
else:
    print("big value is:",c)
