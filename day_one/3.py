dime = int(input("How many containers with less than 1 liter: "))
quarter = int(input("How many containers with more than 1 liter: "))

total = (dime * 0.1) + (quarter * 0.25)

print("Your total is "+ "{:.2f}".format(total) +" $")