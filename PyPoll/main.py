import os
import csv

# Define the file path for the CSV file
csv_path = os.path.join("PyPoll", "Resources", "election_data.csv")

# Set variables
total_votes = 0
candidate_votes = {}

# Open the CSV file and read its content
with open(csv_path, 'r') as file:
    reader = csv.reader(file)
    header = next(reader) 

    for row in reader:
        total_votes += 1
        candidate = row[2] 
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate the percentage of votes and determine the winner
results = []
winner = ""
max_votes = 0

for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {percentage:.3f}% ({votes})")
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for result in results:
    print(result)
print("-------------------------")
print(f"Winner: {winner}")

