# Import files
import csv
import os

# Define percentage in decimals
def fixPercent(num):
     num = "{:.3%}".format(num)
     return num

# Define path to input files 
election_data_csv = os.path.join("PyPoll","Resources", "election_data.csv")

# Create Variables and lists 
total_votes = 0
winner_count = 0
election_candidates = []
vote_counts = []
percentage_votes = []

# Read the file 
with open(election_data_csv, 'r') as election_data:
    reader = csv.reader(election_data, delimiter=",")  
    headers = next(reader)

    # Loop through rows and data
    for row in reader:
        total_votes += 1
    
        # Retrieve vote counts
        if row[2] not in election_candidates:

        # Append candidate names and votes
            election_candidates.append(row[2])
            vote_counts.append(1)

        else:
            # Get candidate list 
            Candidates = election_candidates.index(row[2])
            vote_counts[Candidates] += 1
        
# Calculate candidate percentage of votes 
for i in range(len(vote_counts)):
    percentage_votes.append(vote_counts[i] / total_votes)

# Determine election winner by vote counts 
for i in range(len(vote_counts)):

    if vote_counts[i] > winner_count:
       winner_count = vote_counts[i]
       winner = election_candidates[i]

#Path for Election results Output
election_data_output = os.path.join("Analysis", "PyPoll_analysis.txt")

# Create text file 
with open("election_data_file.txt", 'w') as textfile:

    textfile.write(f"Election Results\n"
    f"----------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"----------------------------\n"
    )

    # --- for loop to iteratively write each candidate's info ---
    for i in range(len(election_candidates)):
        textfile.write(f"{election_candidates[i]}: {fixPercent(percentage_votes[i])} ({vote_counts[i]})\n")

    textfile.write(f"----------------------------\n"
    f"Winner: {winner}\n"
    f"----------------------------\n"
    )
# Read file 
    election_data_file = os.path.join("PyPoll", "Output", "election_data_output.txt")
    with open(election_data_file, 'r') as Analysis:
        Election_results = Analysis.read()
    print(Election_results)
