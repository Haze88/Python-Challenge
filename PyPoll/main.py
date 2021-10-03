import csv
import os


#Read the  voting data
csvpath = os.path.join('Resources','election_data.csv')

#output file location for the analysis
inputfile = os.path.join('Resources','election_data.csv')

#Variables
candidatevotes = {} #variable holds the total number of candidates
TotalVotes = 0 #variable that hold the total number of votes
candidate = [] # variable for each candiate 
WinningCount = 0 #variable hold the winning count
Winner = "" #variable for winner


#read the csv file
with open(inputfile) as csvfile: 
    #create csv reader
    csv_reader= csv.reader(csvfile)

    #read the header
    header =next(csv_reader)
    

    #rows will be lists
        #index 0 is the candidate name
        #index 1 is for total candidates
        #index 2 is for total number of votes each candidate won
       
    #For each row
    for Row in csv_reader:
            #add on total votes
        TotalVotes += 1 # same as TotalVotes - TotalVotes + 1 

        #check to see if the name is in the list of candidates 
        if Row[2] not in candidatevotes:
                #if the candidate is not on the list, add candidate to the list
            candidate.append(Row[2])

                #Add the total to the dictonary as well
                # {"key: value"}
                #start the count at the 1 for the votes.
            candidatevotes[Row[2]] = 1 
        else:
                # the candidate is in the list of votes
                #add a vote to that total count
            candidatevotes[Row[2]] += 1



    voteoutput =""

    for candidate in candidatevotes:
    #get the vote count and percentage of the votes
        Votes = candidatevotes.get(candidate)
        votePct = float(Votes) / float(TotalVotes) * 100.00
        voteoutput += f"{candidate}: {votePct:.2f} %\n"
    
    #compare the votes to winning count
    if Votes > WinningCount: 
        WinningCount = Votes

        #Update winner
        Winner = candidate
    
#Winner Outcome 
Winneroutcome = f"Winner:{Winner}\n"

    
#create an output variable to hold the output
output =( 
    f"\nelection_Data\n"
    f"\n------------------\n"
    f"Total Votes: {TotalVotes:,}\n"
    f"------------------------------\n"
    f"{voteoutput}\n"
    f"------------------------------\n"
    f"{Winner}"
    )
print(output)

 #create output for ekection results\
outputfile = os.path.join("VoteCount.txt")
with open(outputfile, "w") as textfile:
    textfile.write(output)

    