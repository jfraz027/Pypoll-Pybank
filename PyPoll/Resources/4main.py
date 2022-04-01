# Import dependencies
import os
import csv

def fixPercent(num):
    num = "{:.3%}".format(num)
    return num

#import collections
#from collections import Counter

# Define PyPoll's variables
voters_candidates = []
votes_per_candidate = []
votes_percent =[]
votes_total = 0
winner_count = 0

# Path to collect data from the Resources folder
election_data_csv_path = os.path.join("PyPoll","Resources", "election_data.csv")

# Open and read csv
with open(election_data_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    # Read data 
    for row in csv_reader:
        votes_total = 1

    if row[2] not in voters_candidates:
        voters_candidates.append(row[2])
        votes_per_candidate.append(1)
    
    else:
        candidate = voters_candidates.index(row[2])
        votes_per_candidate[candidate] = 1
    # Sort the list by default ascending order
    #sorted_list = sorted(voters_candidates)
          
    # Arrange the sorted list 
    #arrange_list = sorted_list

    # candidate votes 
    #count_candidate = Counter (arrange_list) 
    #votes_per_candidate.append(count_candidate.most_common())

#def fixPercent(num):
    #num = "{:.3%}".format(num)
    #return num

    # % of candidate votes  
    #for item in votes_per_candidate:
       
        #first = format((item[0][1])*100/(sum(count_candidate.values())),".3f")
        #second = format((item[1][1])*100/(sum(count_candidate.values())),".3f")
        #third = format((item[2][1])*100/(sum(count_candidate.values())),".3f")
for i in range(len(votes_per_candidate)):
    votes_percent.append(votes_per_candidate[i] / votes_total)

# --- calculate the winner based on most votes ---
for i in range(len(votes_per_candidate)):

    # if the number of votes is greater than WinnerCount (initially zero)
    if votes_per_candidate[i] > winner_count:
        
        #update WinnerCount to the number of votes at index i
        winner_count = votes_per_candidate[i]

        #update Winner to the candidate name at index i
        winner = voters_candidates[i]

#--- create a text file with the analysis output ---
with open("outputfile.txt", 'w') as textfile:
    textfile.write(f"Election Results\n"
                   f"----------------------------\n"
                   f"Total Votes: {votes_total}\n"
                   f"----------------------------\n"
                   )

    # --- for loop to iteratively write each candidate's info ---
    for i in range(len(voters_candidates)):
        textfile.write(f"{voters_candidates[i]}: {fixPercent(votes_percent[i])} ({votes_per_candidate[i]})\n")

    textfile.write(f"----------------------------\n"
                   f"Winner: {winner}\n"
                   f"----------------------------\n"
                  )

# --- read the output file and print analysis to terminal ---
with open ("outputfile.txt", 'r') as analysis:
    contents = analysis.read()
    print(contents)








# Print Results
    #print(f"Election Results")
#print(f"-------------------------")
#print(f"Total Votes:  {sum(count_candidate.values())}")
#print(f"-------------------------")
#print(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})")
#print(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})")
#print(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})")
#print(f"-------------------------")
#print(f"Winner:  {votes_per_candidate[0][0][0]}")
#print(f"-------------------------")

# Export as text file 
#election_file = os.path.join("Output", "election_data.txt")
#with open("election_file.txt", "w") as f:

    #f.write(f"Election Results\n")
    #f.write(f"-------------------------\n")
    #f.write(f"Total Votes:  {sum(count_candidate.values())}\n")
    #f.write(f"-------------------------\n")
    #f.write(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})\n")
    #f.write(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})\n")
    #f.write(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})\n")
    #f.write(f"-------------------------\n")
    #f.write(f"Winner:  {votes_per_candidate[0][0][0]}\n")
    #f.write(f"-------------------------\n")    