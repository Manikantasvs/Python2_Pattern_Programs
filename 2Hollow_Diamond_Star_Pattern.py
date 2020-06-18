i=input("enter a number:")
for j in range(i):
	for k in range(i-j-1):
		print ' ',
	print "*",
	if(j!=0):
		for l in range(2*j-1):
			print " ",
		print "*",
	print
for m in range(i-1):
	for n in range(m+1):
		print " ",
	print "*",
	for o in range(2*(i-2-m)-1):
		print " ",
	if(2*(i-2-m)-1>0):
		print "*",
	print
