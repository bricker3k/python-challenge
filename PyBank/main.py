
import os
import csv

budget_data = os.path.join( "budget_data.csv")

with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")
    i = str(budget_data[0])

    amount = []
    for row in csvreader:
        amount.append(int(row[1]))

        max_amount = -2196188
        min_amount = 1926172
        
        if amount > max_amount:
            max = i
            date_xamount = i
        if amount < min_amount:
            min = i 
            date_namount = i

    average_change = []
    for x in row:
        average_change.append(previous - x)
        previous = x
        average_change.pop(0)

    for i in range(0, len(lst)-1)
    average_change.append(lst[i]-lst)[i+1]
    
    
    


#The total number of months included in the dataset
total_months= len(amount)


#The net total amount of "Profit/Losses" over the entire period
total_amount= sum(amount)

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_amount:,}")
print(f"Average  Change: {average_change}") 
print(f"Greatest Increase in Profits:{date_xamount}({max_amount})")
print(f"Greatest Decrease in Profits: {date_namount}({min_amount})")

