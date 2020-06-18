i=input("enter a number:")
for j in range(i):
	for k in range(j+1):
		if(j%2==0 and k%2==0):
			print 1,
		elif(j%2==0 and k%2!=0):
			print 0,
		if(j%2!=0 and k%2==0):
			print 0,
		elif(j%2!=0 and k%2!=0):
			print 1,
	print
