import pandas as pd
import os

# Define the file path
file_path = r'C:\Users\leahm\python-challenge\PyBank\Resources\budget_data.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Clean and convert data types
df['Date'] = pd.to_datetime(df['Date'].str.strip(), format='%b-%y', errors='coerce')
df['Profit/Losses'] = pd.to_numeric(df['Profit/Losses'], errors='coerce')

# Drop rows with NaT in Date or NaN in Profit/Losses
df = df.dropna(subset=['Date', 'Profit/Losses'])

# Calculate required metrics
total_months = df['Date'].nunique()
net_total = df['Profit/Losses'].sum()
df['Change'] = df['Profit/Losses'].diff()

# Calculate average change
average_change = df['Change'].mean()

# Determine greatest increase and decrease
greatest_increase = df.loc[df['Change'].idxmax()]
greatest_decrease = df.loc[df['Change'].idxmin()]

# Format dates for output
greatest_increase_date = greatest_increase['Date'].strftime('%b-%y')
greatest_decrease_date = greatest_decrease['Date'].strftime('%b-%y')

# Prepare results
results = [
    "Financial Analysis",
    "-----------------------------",
    f"Total Months: {total_months}",
    f"Net Total Profit/Losses: ${int(net_total)}",
    f"Average Change in Profit/Losses: ${average_change:.2f}",
    f"Greatest Increase in Profits: {greatest_increase_date} (${int(greatest_increase['Change'])})",
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${int(greatest_decrease['Change'])})"
]

# Print results to the terminal
for line in results:
    print(line)

# Export results to a text file
output_path = r'C:\Users\leahm\python-challenge\PyBank\analysis\financial_analysis.txt'
with open(output_path, 'w') as f:
    for line in results:
        f.write(line + '\n')

