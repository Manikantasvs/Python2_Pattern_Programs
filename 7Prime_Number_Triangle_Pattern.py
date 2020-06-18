i=input("enter a number:")
m=2
for j in range(i):
	c=0
	while(c<j+1):
		n,k=0,1
		while(k<=m):
			if(m%k==0):
				n+=1
			k+=1
		if(n==2):
			print m,
			c+=1
		m+=1
	print
