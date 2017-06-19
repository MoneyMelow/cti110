#BugCollector
#6/15/17
#CTI-110 M4T1 - BugCollector
#MarquisMarshall
#

total = 0

for day in range(1, 6):
    print("Enter the bugs collected on day:",day)
    bugs = int(input())
    total += bugs

print("You collected a total of", total, "bugs this week.")
    
