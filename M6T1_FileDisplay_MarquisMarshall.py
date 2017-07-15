#FileDisplay
#7/5
#CTI-110 M6T1 - FileDisplay
#MarquisMarshall
#

myfile = open('numbers.txt', 'r')


for line in myfile:
    number = int(line)
    print(number)

myfile.close()
              
