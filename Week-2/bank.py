#write a program that calculates 16%
#ranging between 100k - 150k
#19% tax income is between 150k - 300k
#30% tax income is above 300k 
#5% if income is less 100k

#print gross income and net income
income = input ("Enter your net income")

#Formulae gross_income = net income + taxes

net_income = int(input("Enter your Net income "))

#above 300k
if(net_income >= 300000):
	gross_income = net_income + ((30/100)*net_income)
	print("Since Your Net income is {} your Gross income is {}".format(net_income, int(gross_income)))

#150k to less than 300k
elif(net_income >= 150000) & (net_income < 300000):
	gross_income = net_income + ((19/100)*net_income)
	print("Since Your Net income is {} your Gross income is {}".format(net_income, int(gross_income)))

#100k to less than 150k
elif(net_income >= 100000) & (net_income < 150000):
	gross_income = net_income + ((16/100)*net_income)
	print("Since Your Net income is {} your Gross income is {}".format(net_income, int(gross_income)))

#from 1 to less than 100k
elif(net_income >= 1) & (net_income < 100000):
	gross_income = net_income + ((5/100)*net_income)
	print("Since Your Net income is {} your Gross income is {}".format(net_income, int(gross_income)))

else:
	print("Invalid argument!")

