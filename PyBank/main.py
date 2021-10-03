import os
import csv

#Collect data from csv path__
csvpath = os.path.join('Resources','budget_data.csv')


# file to hold output of the data
outputfile = os.path.join("budgetData.txt")

# Calulate the amount of "Profit/Losses" over the entire period
TotalMonths = 0 #initialize total Months to 0
TotalProfit = 0 #initialize total Profit to 0
PreviousProfit = 0 # initialize previous profit to 0
Profit = ["", 0] #hold the month and the greatest profit
Loss = ["", 0] #hold the month and the greatest loss
months=[] #initialize months 


#variable to hold changes
MonthlyChanges = []
#monthlyChanges[TotalProfit] # initialize list of monthly changes

#read the csv file
with open(csvpath) as csvfile:
    #create csv reader
    csv_reader = csv.reader(csvfile,delimiter=",")
    print(csv_reader)

    #put in code to read the header
    csv_header = next(csv_reader)
    print(f"csv header:{csv_header}")


    #establish previous profit  
    #PreviousProfit = firstRow   

    for row in csv_reader:
        
        
        #increment the count of total months  
        TotalMonths += 1 #same as totalMonths + 1

        #add on the number of profit
            #profit in index 1
        TotalProfit += float(row[1])

    
         #calculate netchange
        if TotalMonths == 1:
            netchange = 0 
        else: 
            netchange =float(row[1])- PreviousProfit 
        
        #add the first month a change occured
        months.append (row[0])   
        
        #add on to the list of monthly changes
        MonthlyChanges.append(netchange)

        #update previous profit
        PreviousProfit = float(row[1])

#Calculate average profit per month
averageChangePerMonth = sum(MonthlyChanges) / (len(MonthlyChanges) -1)

#output for Total Months
output =(f"Total Months = {TotalMonths}\n" f"average change per month {averageChangePerMonth}" )

GreatestIncrease =[months[1], MonthlyChanges[0]] #hold the great increase
GreatestLoss = [months[0], MonthlyChanges[0]] #hold the greatest decrease

#use this loop to calucalte the index of the greatest and lease month change 
for m in range(len(MonthlyChanges)):
    #calculate the greatest increase and decrease
    if (MonthlyChanges[m] > GreatestIncrease[1]):
        # if the value is greater than the greatest increase, that value becomes the newest increase
        GreatestIncrease[1] = MonthlyChanges[m]
        #update the month
        GreatestIncrease[0] = months[m]

    if (MonthlyChanges[m] < GreatestLoss[1]):
        # if the value is less than the greatest loss, that value becomes the newest loss
        GreatestLoss[1] = MonthlyChanges[m]
        #update the month
        GreatestLoss[0] = months[m]
    print(m)
    
#start generating the output
output = (
    f"n\ budget data \n"
    f"\-------------------- \n"
    f"\tTotal Months ={TotalMonths} \n"
    f"\tTotal Profit =${TotalProfit:,.2f} \n"
    f"\tAverage Change per month =${averageChangePerMonth:,.2f} \n"
    f"\tGreatest increase = {GreatestIncrease[0]} Amount ${GreatestIncrease[1]:,.2f} \n"
    f"\tGreatest decrease = {GreatestLoss[0]} Amount ${GreatestLoss[1]:,.2f} \n"
    )

#print the ouput to terminal
print(output) 



# export output variable to text file


outputfile = os.path.join('.Analysis')
with open(outputfile, "w") as textfile:
    textfile.write(output)









