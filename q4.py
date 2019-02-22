from math import sqrt as sq
c=50
h=30

d=input("Enter no. : ").split(",")
q=[]
for x in d:
	n=int(x)
	a=2*c*n
	b=a/h
	w=sq(b)
	q.append(int(w))

# for i in q:
	# print(i,end=",")

for x in range(len(q)):
	if x==len(q)-1:
		print(q[x])
	else:
		print(q[x],end=",")
print("\n")