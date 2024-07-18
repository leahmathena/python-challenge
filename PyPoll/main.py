import pandas as pd

# Define the file path
file_path = r'C:\Users\leahm\python-challenge\PyPoll\Resources\election_data.csv'

try:
    # Read the CSV file
    df = pd.read_csv(file_path).rename(columns=lambda x: x.strip())
    
    # Check for necessary columns
    if all(col in df.columns for col in ['Ballot ID', 'Candidate']):
        # Total number of votes cast
        total_votes = len(df)

        # Total votes per candidate
        vote_counts = df['Candidate'].value_counts()

        # Calculate percentage of votes per candidate
        vote_percentages = (vote_counts / total_votes) * 100

        # Determine the winner
        winner = vote_counts.idxmax()

        # Prepare results
        results = [
            "Election Results",
            "-------------------------",
            f"Total Votes: {total_votes}",
            "-------------------------"
        ]

        for candidate, count in vote_counts.items():
            results.append(f"{candidate}: {vote_percentages[candidate]:.3f}% ({count})")
        
        results.append("-------------------------")
        results.append(f"Winner: {winner}")
        results.append("-------------------------")

        # Print results to the terminal
        for line in results:
            print(line)

        # Export results to a text file
        output_path = r'C:\Users\leahm\python-challenge\PyPoll\analysis\election_results.txt'
        with open(output_path, 'w') as f:
            for line in results:
                f.write(line + "\n")

    else:
        print("Error: Required columns are missing from the dataset.")

except FileNotFoundError:
    print(f"Error: The file was not found at {file_path}. Please check the path.")
except Exception as e:
    print(f"An error occurred during processing: {e}")