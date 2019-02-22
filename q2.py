n = int(input("Enter no. : "))
l=[]
for i in range(1,n+1):
	l.append(i)

d=dict((i,i*i) for i in l)
print(d)