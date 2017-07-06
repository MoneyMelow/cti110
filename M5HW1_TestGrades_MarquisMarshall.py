#TestAverage
#6/27/17
#CTI-110 M5HW1 - TestAverage and Grade
#MarquisMarshall
#


def main():
    score1, score2, score3, score4, score5 = scores()
    printTableOfResults( score1, score2, score3, score4, score5 )
    print('Your average is', calc_average(score1,score2,score3,score4,score5))
    


def scores():
    print("Enter 5 test scores: ")
    score1 = float(input('Enter Score1: '))
    score2 = float(input('Enter Score2: '))
    score3 = float(input('Enter Score3: '))
    score4 = float(input('Enter Score4: '))
    score5 = float(input('Enter Score5: '))

    return score1, score2, score3, score4, score5

    
    
def calc_average(score1,score2,score3,score4,score5):
    average = (score1 + score2 + score3 + score4 + score5) / 5
    return average

def determine_grade(userScore):
    if (userScore < 60):
        return "F"
    elif (userScore < 70):
        return "D"
    elif (userScore < 80):
        return "C"
    elif (userScore < 90):
        return "B"
    elif (userScore < 100):
        return "A"

def printTableOfResults( score1, score2, score3, score4, score5):
    print( "Score\t\tLetter Grade")
    print( str( score1) + "\t\t" + determine_grade( score1), \
           str( score2) + "\t\t" + determine_grade( score2), \
           str( score3) + "\t\t" + determine_grade( score3), \
           str( score4) + "\t\t" + determine_grade( score4), \
           str( score5) + "\t\t" + determine_grade( score5), sep = "\n")
    
           
    
    
main()
              
    
