import sys

#amount = float(sys.argv[1])
#rate = float(sys.argv[2])
#periodInYears = float(sys.argv[3])

amount = float(raw_input("Loan amount: "))
rate = float(raw_input("Rate: "))
periodInYears = float(raw_input("Period in years: "))

fname = "%s-%s-%s.txt" % (amount, rate, periodInYears)
f = open(fname, "a")
f.write("Loan amount: %s \n" % format(amount, ','))
f.write("Rate: %s \n" % format(rate, ','))
f.write("Period in years: %s \n" % format(periodInYears, ','))
f.write("\n")

installment = amount / (periodInYears * 12)
f.write("Installment = %s" % format(installment, ','))
f.write("\n\n")

total = 0
current = amount
while current >= 0:
	f.write("Remaining amount = %s\t|\t" % format(current, ','))
 	monthlyInterest = ((current / 100) * rate) / 12
	f.write("Monthly interest = %s\t|\t" % format(monthlyInterest, ','))
	monthlyPayment =  installment + monthlyInterest
	f.write("Monthly payment = %s" % format(monthlyPayment, ','))
	f.write("\n")

	total += monthlyPayment
	current -= installment

f.write("\n")	
f.write("Total = %s\n" % format(total, ','))
extra = total - amount
f.write("Extra = %s\n" % format(extra, ','))
