#AgeClassifier
#6/13/17
#CTI-110 M3HW1- AgeClassifier
#MarquisMarshall
#

age = int(input("Enter a person's age: "))

if age <= 1:
    stage = "Infant"
elif age <= 13:
    stage = "Child"
elif age <= 20:
    stage = "Teenager"
elif age > 20:
    stage = "Adult"


print("This person is a:",stage)
