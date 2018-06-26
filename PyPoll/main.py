import csv

# open file
# The dataset is composed of three columns:
# Voter ID, County, and Candidate
Candidates = []

with open('election_data.csv', newline='') as E:
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

# print('Election Results')

with open('results.csv', 'w') as csvfile:
    x = ['Election Results', '-' * 30, 
    ("Total Votes: %s" % TotalVotes), ('-' * 30)]

    maxVote = 0
    maxVoteName = ''
    for a in Candidates:
        x.append(('{name}: {perc:.3%} ({numvote})'.format(name=a['name'],
            perc=a['numVote'] / TotalVotes, numvote=a['numVote'])))
        if a['numVote'] > maxVote:
            maxVote = a['numVote']
            maxVoteName = a['name']

        # The winner of the election based on popular vote.
    x.append('-' * 30)
    x.append('Winner: {name}'.format(name=maxVoteName))
    x.append('-' * 30)

    writer = csv.writer(csvfile)
    for row in x:
        print(row)
        writer.writerows(row)
