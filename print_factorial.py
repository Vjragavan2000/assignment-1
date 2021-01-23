a=int(input("Enter 'n' value:"))
ans=1
if a==0:
	print(ans)
else:
	for x in range(1,a+1,1):
		ans=ans*x
	print(ans)
	
