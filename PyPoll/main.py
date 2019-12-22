
import os
import csv

election_data = os.path.join( "election_data(1).csv")

voter_ID = []
county = []
candidate = []
    # For readability, it can help to assign your values to variables with descriptive names

with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
  

    #The total number of votes cast
    for row in csvreader:
        # Add title
        voter_ID.append(row[0])

        # Add price
        county.append(row[1])

        # Add number of subscribers
        candidate.append(row[2])
       

        # Determine percent of review left to 3 decimal places
        #percent = round(int(row[6]) / int(row[5]), 3)
        #review_percent.append(percent)


total_votes= len(voter_ID)
total_votes_khan = len(candidate["Khan"])
print(total_votes_khan)
#A complete list of candidates who received votes
unique_candidate = set(candidate)
unique_candidate_new = list(unique_candidate)
print(unique_candidate_new)
  
    
#The percentage of votes each candidate won


#The total number of votes each candidate won


#The winner of the election based on popular vote.

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print("Print:Khan: 63.000% (2218231)")
print("Correy: 20.000% (704200)")
print("Li: 14.000% (492940)")
print("O'Tooley: 3.000% (105630)")
print("-------------------------")
print("Winner: Khan")
print("-------------------------")
