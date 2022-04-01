import os
import csv

# Set up Lists and Variables
date =[]
months =[]
profit = []
changes = []
count = 0
initial_profit = 0
total_profit = 0
total_change_profits = 0
average_net_change = 0

# Set path as csv file  
budget_path_csv = os.path.join("Pybank","Resources","budget_data.csv")

# Open and Read csv file 
with open(budget_path_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read header row
    cvsreader = next(csvfile)
    for row in csvreader:    
      month = row[0]
      
      # Store Variables 
      date.append(row[0])
      months.append(month)
      values =int(row[1])

      # Calculate profit 
      profit.append(values)
      total_profit = total_profit + int(row[1])

      # Determine monthly profit changes and averages
      count =len(months)
      final_profit = int(row[1])
      monthly_change_profits = final_profit - initial_profit
      
      # List changes 
      changes.append(monthly_change_profits)
      net_total = sum(profit) 
      total_change_profits = total_change_profits + monthly_change_profits
      initial_profit = final_profit
      net_total_months =len(months) - 1
      budget_change =[]  

    for i in range(len(profit) - 1):
      
      budget_change.append((profit[i + 1]) - (profit[i]))
      new_net_total = sum(budget_change)

    # Formulate average change in profits
    average_net_change = new_net_total/net_total_months
    
      # Find profit max/min change by date 
    greatest_increase_profits = max(changes)
    greatest_decrease_profits = min(changes)

    increase_date = date[changes.index(greatest_increase_profits)]
    decrease_date = date[changes.index(greatest_decrease_profits)]
      
    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change is: $" + str(round(average_net_change, 2)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
    print("----------------------------------------------------------")

# Open the file 
with open("Financial_analysis.txt", "w") as output_csv_file:

  output_csv_file.write("----------------------------------------------------------\n")
  output_csv_file.write("Financial Analysis"+ "\n")
  output_csv_file.write("----------------------------------------------------------\n\n")
  output_csv_file.write("Total Months: " + str(count) + "\n")
  output_csv_file.write("Total Profits: " + "$" + str(total_profit) +"\n")
  output_csv_file.write(f"Average Change: ${round(average_net_change,2)}\n")
  output_csv_file.write("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
  output_csv_file.write("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
  output_csv_file.write("----------------------------------------------------------\n")