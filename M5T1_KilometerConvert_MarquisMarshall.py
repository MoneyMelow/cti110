#KiloConverter
#6/26/17
#CTI-110 M5T1_KilometerConverter
#MarquisMarshall
#


kmConversion = 0.6214

def main():
    kilometers = float(input('Enter a distance in kilometers: '))
    show_miles (kilometers)
    

def show_miles (km):
    miles = km * kmConversion
    print (km, 'kilometers is equal to', miles + float(format(miles,".2f")), 'miles.')


main()

    
