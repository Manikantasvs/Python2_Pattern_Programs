i=input("enter a number:")
for j in range(i):
	if(j==0 or j==i-1):
		for k in range(9):
			print '*',
	if(j>0 and j<i-1):
		print '*',
		for l in range(7):
			print ' ',
		print '*',
	print
