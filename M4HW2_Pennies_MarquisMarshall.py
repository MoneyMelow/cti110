#Pennies4Pay
#6/20
#CTI-110- M4HW2- PenniesForPay
#MarquisMarshall
#

daysWorked = int(input("Please enter how many days you worked:"))
payPerDay = 0.01
totalNumberOfPennies = 0
                 

print("Day\tSalary\n----\t-------")
for currentDay in range( daysWorked):
                 penniesForDay = 2 ** currentDay
                 totalNumberOfPennies = totalNumberOfPennies + penniesForDay
                 print( currentDay + 1, "\t" , penniesForDay)


totalPay = totalNumberOfPennies * 0.01

print("\nTotal pay: $", totalPay + float(format( totalPay,",.2f")), sep ="")
                 
                 
