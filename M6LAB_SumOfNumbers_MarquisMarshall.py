#SumOfNumbers
#CTI-110 -SumOfNumbers- M6LAB
#7/6/17
#MarquisMarshall
#


def main():
    numbersFile = open("numbers.txt", "r")

    total = 0
    


    for line in  numbersFile:
        total = total + int(line)


    print("The numbers in the file sum up to", total)

    numbersFile.close()

main()

    
        
