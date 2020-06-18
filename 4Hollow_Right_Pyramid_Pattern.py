i=input("enter a number:")
for j in range(i-1):
	for k in range(i-j-1):
		print ' ',
	print "*",
	if(j!=0):
		for l in range(2*j-1):
			print " ",
		print "*",
	print
for n in range(2*i-1):
	print "*",
	
