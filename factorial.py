a=int(input("enter any number :"))
print a
fact=1
if(a<0):
	print "no factorail for negitive"
elif(a==0):
	print "factorial = 1"
else:
	while(a>0):
		fact = fact * a
		a = a-1
	print "factorial :", fact
