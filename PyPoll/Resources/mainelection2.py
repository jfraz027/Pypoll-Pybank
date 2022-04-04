# Import dependencies
import os
import csv

#import collections
from collections import Counter

# Define PyPoll's variables
voters_candidates = []
votes_per_candidate = []
#percent_vote =[]
#totalvotes = 0

# Path to collect data from the Resources folder
election_data_csv_path = os.path.join("PyPoll","Resources", "election_data.csv")

# Open and read csv
with open(election_data_csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    # Read data 
    for row in csv_reader:
        #totalvotes += 1
        voters_candidates.append(row[2])

    # Sort the list by default ascending order
        sorted_list = sorted(voters_candidates)
          
    # Arrange the sorted list 
    arrange_list = sorted_list

    # candidate votes 
    count_candidate = Counter (arrange_list) 
    votes_per_candidate.append(count_candidate.most_common())

    # % of candidate votes  
    for item in votes_per_candidate:
       
     first = format((item[0][1])*100/(sum(count_candidate.values())),".3f")
    second = format((item[1][1])*100/(sum(count_candidate.values())),".3f")
    third = format((item[2][1])*100/(sum(count_candidate.values())),".3f")

#voter_output = f"{voters_candidates}: {percent_vote:.3f}% ({totalvotes})\n"
#print(voter_output, end="")



for i in range(len(votes_per_candidate)):
    #percent_vote.append(votes_per_candidate[i] / totalvotes)

    if row[2] not in voters_candidates:
        voters_candidates.append(row[2])
        votes_per_candidate.append(1)
    
else:
        candidate = voters_candidates.index(row[2])
        #votes_per_candidate[candidate] += 1

# Print Results
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes:  {sum(count_candidate.values())}")
print(f"-------------------------")
print(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})")
print(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})")
print(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})")
print(f"-------------------------")
print(f"Winner:  {votes_per_candidate[0][0][0]}")
print(f"-------------------------")

# Export as text file 
election_file = os.path.join("Output", "election_data.txt")
with open("election_file.txt", "w") as f:

    f.write(f"Election Results\n")
    f.write(f"-------------------------\n")
    f.write(f"Total Votes:  {sum(count_candidate.values())}\n")
    f.write(f"-------------------------\n")
    f.write(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})\n")
    f.write(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})\n")
    f.write(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})\n")
    #f.write(f"{votes_per_candidate}: {third}% ({votes_per_candidate})")
    f.write(f"-------------------------\n")
    f.write(f"Winner:  {votes_per_candidate[0][0][0]}\n")
    f.write(f"-------------------------\n")    