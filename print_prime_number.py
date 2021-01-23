a=int(input('Enter the 1st number:'))
b=int(input('Enter the 2nd number:'))
for x in range(a,b+1,1):
	count=0
	for y in range(1,x+1,1):
		if x%y==0:
			count=count+1
	if count==2:
		print(x,end=' ')
print('')
