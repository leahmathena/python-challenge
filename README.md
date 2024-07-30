# python-challenge
This repository contains the solution for the Python Challenge assignment, which includes two tasks: PyBank and PyPoll. The objective was to use Python for data analysis and generate reports based on financial and election data.

## PyBank

### Description

The PyBank challenge involved analyzing a financial dataset to determine various financial metrics. The dataset, `budget_data.csv`, contains two columns: "Date" and "Profit/Losses".

### Tasks Completed

1. **Total Months**: Calculated the total number of months included in the dataset.
2. **Net Total**: Computed the net total amount of "Profit/Losses" over the entire period.
3. **Average Change**: Calculated the average change in "Profit/Losses" over the entire period.
4. **Greatest Increase**: Identified the greatest increase in profits, including the date and amount.
5. **Greatest Decrease**: Identified the greatest decrease in profits, including the date and amount.

### Results

The analysis was executed using the script in `PyBank/main.py` and results were stored in `PyBank/Analysis/financial_analysis.txt`. The output is as follows:

### *Financial Analysis*

Total Months: 86

Total: $22,564,198

Average Change: $-8,311.11

Greatest Increase in Profits: Aug-16 ($1,862,002)

Greatest Decrease in Profits: Feb-14 ($-1,825,558)



## PyPoll

### Description

The PyPoll challenge required analyzing election data to determine voting metrics. The dataset, `election_data.csv`, includes "Voter ID", "County", and "Candidate".

### Tasks Completed

1. **Total Votes**: Calculated the total number of votes cast.
2. **Candidates List**: Created a complete list of candidates who received votes.
3. **Percentage of Votes**: Calculated the percentage of votes each candidate won.
4. **Total Votes per Candidate**: Computed the total number of votes each candidate won.
5. **Election Winner**: Determined the winner of the election based on the popular vote.

### Results

The analysis was executed using the script in `PyPoll/main.py` and results were stored in `PyPoll/Analysis/election_results.txt`. The output is as follows:

### *Election Results*

Total Votes: 369,711

Charles Casper Stockham: 23.049% (85,213)

Diana DeGette: 73.812% (272,892)

Raymon Anthony Doane: 3.139% (11,606)

Winner: Diana DeGette


## Final Notes

- Both scripts print their results to the terminal.
- Analysis results are saved in text files within the `Analysis` folders for each challenge.
- The code has been tested and verified to produce correct results based on the provided datasets.

