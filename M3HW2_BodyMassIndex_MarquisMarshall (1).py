#BMIndex
#6/14/17
#CTI-110 M3HW2- Body Mass Index
#MarquisMarshall
#

weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))

bMI = weight * 703/height**2

if bMI < 18.5:
    print("A person with a BMI of " + format(bMI,".2f") + " is Underweight")
    bodyWeight = "Underweight"

elif bMI >= 18.5 and bMI <= 25:
    print("A person with a BMI of " + format(bMI,".2f") + " is Optimal Body Weight")
    bodyWeight = "Optimal Body Weight"

elif bMI > 25:
    print("A person with a BMI of " + format(bMI,".2f") + " is Overweight")
    bodyWeight = "Overweight"
    


print("Your Body Mass Index is:",format(bMI,'.2f'))
