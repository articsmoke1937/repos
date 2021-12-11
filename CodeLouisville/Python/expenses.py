""" expenses = [10.50, 8, 5, 15, 20 , 5, 3]
total = 0
for x in expenses:
    total= total + x
print("You spent $", total, " on lunch this week.", sep='')

expenses = [10.50, 8, 5, 15, 20 , 5, 3]
total = sum(expenses)
print("You spent $", total, " on lunch this week.", sep='')  """

total = 0 
expenses = []
numofExpense = int(input("Enter the number of expenses: "))

for i in range (numofExpense):
    expenses.append(float(input("Enter an expense: ")))

    total = sum(expenses)
    print("You spent $", total, sep='')