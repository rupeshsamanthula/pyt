ch=input("")
if((ch>='a' or ch<='z') and (ch>='A' or ch>='Z')):
	if(ch=='a',ch=='e',ch=='i',ch=='o',ch=='u',ch=='A',ch=='E',ch=='I',ch=='O',ch=='U'):
		print('vowel',end="")
		
	else:
		print('constant',end="")
else:
	print('notvalid',end="")
	
