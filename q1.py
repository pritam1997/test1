def fun(a=2000,b=3200):
	s=""
	l=[]

	for n in range(a,b+1):
		if n%7==0 and n%5!=0:
			print(n,end=",")
	return ''
		
print(fun())