import os
import csv

# Variables
months = []
p = []
average_net_change = 0
total_months = 0
net_change = []
date = []

# Load csv file
csvpath = os.path.join("Pybank",'Resources', 'budget_data.csv')

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    reader = csv.reader(csvfile)
    next(reader, None)
# Add values to lists
    for row in reader:
        month = row[0]
        months.append(month)
        values = int(row[1])
        p.append(values)

total_months = len(months)
net_total = sum(p)
net_total_months = len(months) - 1
difference_budget_data = []

for i in range(len(p) - 1):
    difference_budget_data.append(float(p[i + 1]) - float(p[i]))
    new_net_total = sum(difference_budget_data)

# Find the sum of profits/losses
average_net_change = new_net_total/net_total_months

# Find the greatest increase/decrease (date and amount) over the entire period
greatest_increase_profits = max(months)
greatest_decrease_profits = min(months)

increase_date = p[months.index(greatest_increase_profits)]
decrease_date = p[months.index(greatest_decrease_profits)]

#min_p = p[p.index(min(p))] - p[p.index(min(p))-1]
#max_p = p[p.index(max(p))] - p[p.index(max(p))-1]

# Print out results to console
print("Financial Analysis")
print("--------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${round(average_net_change,2)}")
print(f"Greatest Increase in Profits: " + str(greatest_increase_profits) + " ($" + str(increase_date) + ")")
print(f"Greatest Decrease in Profits: " + str(greatest_decrease_profits) + " ($" + str(decrease_date)+ ")")
print("----------------------------------------------------------")




#print(f'Greatest Increase in Profits: {months[p.index(max(p))]} (${max_p})')
#print(f"Greatest Descrease in Profits: {months[p.index(min(p))]} (${min_p})")

# Create a text file with the results
#output_file = 'Analysis/financial_analysis.txt'
#with open(output_file, "w", newline="") as datafile:
   # csvwriter = csv.writer(datafile)
    #csvwriter.writerow(["Financial Analysis"])
    #csvwriter.writerow(["--------------------"])
    #csvwriter.writerow([f"Total Months: {total_months}"])
    #csvwriter.writerow([f"Total: ${net_total}"])
    #csvwriter.writerow([f"Average Change: ${round(average_net_change,2)}"])
    #csvwriter.writerow([f'Greatest Increase in Profits: {months[p.index(max(p))]} (${max_p})'])
    #csvwriter.writerow([f"Greatest Decrease in Profits: {months[p.index(min(p))]} (${min_p})"])