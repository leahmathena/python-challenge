import os
import csv

# Define the file path for the CSV file
csv_path = os.path.join("PyBank", "Resources", "budget_data.csv")
analysis_path = os.path.join("PyBank", "Analysis", "PyBank_analysis.txt")

# Set variables
total_months = 0
net_total = 0
previous_profit = None
total_change = 0
greatest_increase = ('', float('-inf'))
greatest_decrease = ('', float('inf'))


with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader) 

    for row in csvreader:
        date, profit_loss = row
        profit_loss = int(profit_loss)
        
        total_months += 1
        net_total += profit_loss

        if previous_profit is not None:
            change = profit_loss - previous_profit
            total_change += change

            if change > greatest_increase[1]:
                greatest_increase = (date, change)
            if change < greatest_decrease[1]:
                greatest_decrease = (date, change)

        previous_profit = profit_loss

# Calculate average change
average_change = total_change / (total_months - 1) if total_months > 1 else 0

# Print the results
results = [
    "Financial Analysis",
    "----------------------------",
    f"Total Months: {total_months}",
    f"Total: ${net_total}",
    f"Average Change: ${average_change:.2f}",
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})",
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})"
]
for line in results:
    print(line)

with open(analysis_path, 'w') as file:
    for line in results:
        file.write(line + '\n')
