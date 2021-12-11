# get the loan details

moneyowed = float(input("How much money do you owe, in dollars\n"))
apr = float(input("What is the annual percentage rate\n"))
payment = float(input("What would you monthly payment be, in dollars\n"))
months = int(input("How many months do you want to see results for?\n"))

# Divide apr by 100 to make it a percent, then divide by 12 to make it monthly

monthly_rate = apr/100/12
paid = 0
totalinterest = 0

for x in range (months):
    #Add in interest
    interest_paid = moneyowed * monthly_rate
    moneyowed = moneyowed + interest_paid

    if (moneyowed - payment < 0):
        print("The last payment is", moneyowed)
        print("You paid off the loan in", x+1, "months")
        break
    # Make payment
    moneyowed = moneyowed - payment

    #track paid amount
    paid = paid + payment + interest_paid

    totalinterest = totalinterest + interest_paid

#Print the results after this month
print("Paid", payment, "each month with interest for a total of ", paid, ". The total interest was", totalinterest, ".\n", end=' ')
if (moneyowed - payment < 0):
    print("I owe nothing")
elif (moneyowed-payment > 0):
    print("Now I owe", moneyowed)
