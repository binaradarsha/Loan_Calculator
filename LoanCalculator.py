import sys

#amount = float(sys.argv[1])
#rate = float(sys.argv[2])
#periodInYears = float(sys.argv[3])

amount = float(raw_input("Loan amount: "))
rate = float(raw_input("Rate: "))
periodInYears = float(raw_input("Period in years: "))

installment = amount / (periodInYears * 12)
print("Installment = %s" % format(installment, ','))
print

total = 0
current = amount
while current >= 0:
	print("Current = %s" % format(current, ','))
 	monthlyInterest = ((current / 100) * rate) / 12
	print("Monthly interest = %s" % format(monthlyInterest, ','))
	monthlyPayment =  installment + monthlyInterest
	print("Monthly payment = %s" % format(monthlyPayment, ','))
	print

	total += monthlyPayment
	current -= installment
	
print("Total = %s" % format(total, ','))
extra = total - amount
print("Extra = %s" % format(extra, ','))
