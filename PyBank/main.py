import csv

# open file
with open('budget_data.csv', 'rb') as F:
    reader = csv.reader(F, delimiter=',')
    for x in reader:
        print(x)
        print(x[0])
        print(x[0], x[1], x[2])
# The total number of months included in the dataset
# The total net amount of "Profit/Losses" over the entire period
# The average change in "Profit/Losses" between months over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period
