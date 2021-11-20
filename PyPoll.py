# The date we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Import the datetime class from the datetime module.
# import datetime as dt
# # Use the now() attribute on the datetime class to get the present time.
# now = dt.datetime.now()
# # Print the present time
# print("THe time right now is ", now)

# # Assign a variable for the file to load and the path
# file_to_load = "Resources\election_results.csv"

# # Open the election results and read the file
# election_data = open(file_to_load, "r")

# # To do: perform analysis
# print(election_data)

# # Close the file
# election_data.close()

# # Create a filename variable to a direct or indirect path to the file
# file_to_save = "analysis\election_analysis.txt"

# # Use the open statement to open the file as a text file
# outfile = open(file_to_save, "w")

# # Write some data to the file
# #outfile.write("hello world")
# # Write three counties to the file
# #outfile.write("Arapahoe, ")
# #utfile.write("Denver, ")
# #outfile.write("Jefferson")
# #outfile.write("Arapahoe, Denver, Jefferson")

# outfile.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

# # Close the file
# outfile.close()

#Add our dependencies
import csv
import os

#Assign a variable to load a file form a path
file_to_load = os.path.join("Resources","election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("Analysis","election_analysis.txt")

# Initalize a total voter counter
total_votes = 0

# Candidate Options
candidate_options =[]

# Declare the empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:

    # To do: read and analysis the data here
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Print the header row
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
        # Add to the totoal vote count
        total_votes += 1

        # Print the candidate name for each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            #Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
           
        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#Save the results to our text file
with open(file_to_save, "w") as txt_file:

    #Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"--------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------\n")
    print(election_results, end="")
    #Save the final vote count to the text file
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        #Retrieve vote count and percentage    
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        #Print each candidate, their voter count, and percentage to the cerminal
        candidate_results = (f"{candidate_name}: received {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        #Save the candidate results to our text file
        txt_file.write(candidate_results)
                    
        # Determine winning vote count and candidate
        # Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percent =
        # vote_percentage.
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
                            
    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n")
    print(winning_candidate_summary)
    #Save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)
    #Print the total vote dictionary
    #print(candidate_votes)


