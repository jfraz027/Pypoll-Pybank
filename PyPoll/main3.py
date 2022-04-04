## --- import packages to read/write CSV files and create dynamic paths to the I/O files ---
import csv
import os

# -- define function to fix percentage format to 3 decimal points ---
def fixPercent(num):
     num = "{:.3%}".format(num)
     return num

# --- define relative path for the input and output files ---
election_data_csv = os.path.join("PyPoll","Resources", "election_data.csv")
election_data_output = os.path.join("Analysis", "PyPoll_analysis.txt")

# --- create empty lists and variables for storing values and calculations from data ---
election_candidates = []
vote_counts = []
percentage_votes = []
total_votes = 0
winner_count = 0

# --- read the CSV file ---
with open(election_data_csv, 'r') as election_data:
    reader = csv.reader(election_data, delimiter=",")

    # --- store header rows into a Headers list ---
    Headers = next(reader)

    # --- for loop to go through each row in the CSV file and count the total number of votes ---

    for row in reader:
        total_votes += 1
    
        # Get count for votes
        if row[2] not in election_candidates:

            #append the name to UniqueCandidates and a value of 1 to VoteCounts list
            election_candidates.append(row[2])
            vote_counts.append(1)

        # if row[2] (candidate name) is in the UniqueCandidates list
        else:

            # get the index of the candidate from the UniqueCandidates list in order to increase the vote count by 1
            Candidates = election_candidates.index(row[2])
            vote_counts[Candidates] += 1
        

# --- calculate percentage of votes for each candidate ---
for i in range(len(vote_counts)):
    percentage_votes.append(vote_counts[i] / total_votes)

# --- calculate the winner based on most votes ---
for i in range(len(vote_counts)):

    # if the number of votes is greater than WinnerCount (initially zero)
    if vote_counts[i] > winner_count:
        
        #update WinnerCount to the number of votes at index i
        winner_count = vote_counts[i]

        #update Winner to the candidate name at index i
        Winner = election_candidates[i]

#--- create a text file with the analysis output ---
election_data_file = os.path.join("PyPoll", "Output", "election_data_output.txt")
with open(election_data_file, 'w') as textfile:
    textfile.write(f"Election Results\n"
                   f"----------------------------\n"
                   f"Total Votes: {total_votes}\n"
                   f"----------------------------\n"
                   )

    # --- for loop to iteratively write each candidate's info ---
    for i in range(len(election_candidates)):
       textfile.write(f"{election_candidates[i]}: {fixPercent(percentage_votes[i])} ({vote_counts[i]})\n")
        
    textfile.write(f"----------------------------\n"
    f"Winner: {Winner}\n"
    f"----------------------------\n"   
    )
# --- read the output file and print analysis to terminal ---
    with open(election_data_file, 'r') as analysis:
        contents = analysis.read()
        print(contents)
