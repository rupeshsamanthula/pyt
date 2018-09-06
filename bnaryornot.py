l=input()
c=0
for i in range(0,len(l)):
  if l[i]=='0' or l[i]=='1':
    c+=1
if c==len(l):
  print("yes")
else:print("no")
