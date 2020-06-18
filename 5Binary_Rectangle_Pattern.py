i=input("enter a number:")
for j in range(i):
	if(j==0 or j==i-1):
		for k in range(9):
			print 0,
	if(j>0 and j<i-1):
		print 0,
		for l in range(7):
			print 1,
		print 0,
	print
