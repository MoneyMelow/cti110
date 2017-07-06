#Feet2Inches
#6/26/17
#CTI-110 M5T2_Feet2Inches
#MarquisMarshall
#


INCHES_PER_FOOT = 12

def main():
    feet = int(input("Enter a number of feet: "))

    print(feet, "feet is equal to", feet_to_inches(feet), "inches.")
    


def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

main()
