# Assign a variable for the file to load and the path.
import csv
import os

#Assign a variable to load a file from a path
file_to_load = os.path.join('Resources','election_results.csv')
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Intialize a total vote counter
total_votes=0

#Candidate Options
candidate_options=[]
candidate_votes={}

#Winning Candidate and winning count tracker
winning_candidate=""
winning_count=0
winning_percentage=0

# Open the elction results and read the file
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)
    #print header
    headers=next(file_reader)
    print(headers)
   # Print each row in the CSV file.
    for row in file_reader:
        total_votes+=1
        #Print the candidate name from each row
        candidate_name=row[2]

        #Add candidate name to list
        if (candidate_name) not in (candidate_options):
            candidate_options.append(candidate_name)
            #Begin tracking vote count
            candidate_votes[candidate_name]=0 
         #Add a vote to the candidat's count
        candidate_votes[candidate_name]+=1
#Determine percentage of votes
for candidate_name in candidate_votes:
    votes=candidate_votes[candidate_name]
    vote_percentage=float(votes)/float(total_votes)*100
    
    
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    #Determine winning vote count and candidate
    if(votes>winning_count) and (vote_percentage>winning_percentage):
        winning_count=votes
        winning_percentage=vote_percentage
        winning_candidate=candidate_name
winning_candidate_summary=(
    f"-----------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-----------------------------\n")
print(winning_candidate_summary)
print(candidate_votes)

#Print Candidate vote dictionary
#print(candidate_votes)

#Print the total votes
#print(total_votes)



# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

 