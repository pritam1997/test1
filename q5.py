s = input("enter string : ").split(",")
l=[]
for x in s:
	l.append(x)
l.sort()

for i in range(len(l)):
	if i==len(l)-1:
		print(x)
	else:
		print(x,end=",")

print("\n")