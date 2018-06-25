import csv

# open file
# The dataset is composed of three columns:
# Voter ID, County, and Candidate


def PrintNWrite(Blah, fileName):
    print(Blah)
    print(Blah, file=fileName)



Candidates = []

with open('election_data2.csv', newline='') as E:
    reader = csv.reader(E, delimiter=',')
    next(E)
    TotalVotes = 0
    for x in reader:
        TotalVotes += 1
        if not Candidates:
            Candidates.append({'name': x[2], 'numVote': 1, 'percVote': 0})
        else:
            inList = False
            for a in Candidates:
                if a['name'] == x[2]:
                    a['numVote'] += 1
                    inList = True
            if not inList:
                Candidates.append({'name': x[2], 'numVote': 1, 'percVote': 0})
# The total number of votes cast
results = open('results.csv', 'wt')
print('Election Results', file=results)
print('-' * 30, file=results)
print("Total Votes: %s" % TotalVotes, file=results)
print('-' * 30, file=results)
# The percentage of votes each candidate won
# The total number of votes each candidate won
maxVote = 0
maxVoteName = ''
for a in Candidates:
    # "{0:.0%}".format(1./3)
    print('{name}: {perc:.3%} ({numvote})'.format(name=a['name'],
        perc=a['numVote'] / TotalVotes, numvote=a['numVote']),
        file=results)
    if a['numVote'] > maxVote:
        maxVote = a['numVote']
        maxVoteName = a['name']
# The winner of the election based on popular vote.
print('-' * 30, file=results)
print('Winner: {name}'.format(name=maxVoteName), file=results)
print('-' * 30, file=results)
results.close()
