a=input("enter name-")
b=input("Designation-")
c=int()
d=input("enter name of month-")
e=input("Did overtime(y/n)-")
if (e=='y'):
	i=int(input("enter no of days-"))
else:
	print("next")
if (d=='january' or 'march' or 'may' or 'july'or 'august' or 'october' or 'december'):
	c=31
elif (d=='april' or 'june' or 'september' or 'november'):
	c=30
else:
	c=29
if (e=='n' and b=='manager'):
	f=c*2000
	print("Salary",f)
elif (e=='y' and b=='manager'):
	k=(c+i/2)*2000
	print("Overtime salary---",(i/2)*2000)
	print(" Total Salary---",k)	
elif (e=='n' and b=='team leader'):
	g=c*1800
	print("total salary",g)
elif (e=='y' and b=='team leader'):
	l=(c+i/2)*1800
	print("Overtime salary",(i/2)*1800)
	print("Total Salary",l)
elif (e=='y' and b=='team member'):
	m=(c+i/2)*1500
	print("Overtime salary",(i/2)*1500)
	print("Total salary",m)	
else:
	h=c*1500
	print(" Total salary",h)



			