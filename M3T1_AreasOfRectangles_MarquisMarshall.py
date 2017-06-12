#AreaofRectangle
#6/12/17
#CTI-110 M3T1- Areas of Rectan
#MarquisMarshall
#

length1 = int( input("What's the length of rectangle 1?" ))
width1 = int( input ("What's the width of rectangle 1?"))

length2 = int( input("What's the length of rectangle 2?"))
width2 = int( input("What's the width of rectangle 2?"))

area1 = length1 * width1
area2 = length2 * width2

if area1 > area2:
    print( "Rectangle 1 has the greater area!")
elif area2 > area1:
    print("Rectangle 2 has the greater area!")
else:
    print("Both rectangles have the same area.")
    
    


              
