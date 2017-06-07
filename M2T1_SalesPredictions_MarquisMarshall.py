#Input,Processing and Output
#6/5/2017
#CTI-110 M2T1- Sales Prediction
#Marquis Marshall
#

# Get the projected total sales
projectedTotalSales = float( input('Please enter the proected amount '+ \
                                   ' of total sales:'))

# Calculate the profit as 23 percent of total sales.
profit = 0.23 * projectedTotalSales

# Display the profit
print( 'The profit is $' + format( profit , ',.2f'))
