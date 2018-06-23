import csv

# open file
with open('budget_data.csv', newline = '') as F:
    reader = csv.reader(F, delimiter=',')
    monthCount = 0
    TotalNet = 0
    MaxIncrease = 0
    MaxDecrease = 100000000
    next(F)
    for x in reader:
        x[1] = int(x[1])
        monthCount = monthCount + 1
        TotalNet = TotalNet + x[1]
        if x[1] > MaxIncrease:
            MaxIncrease = x[1]
            IncDate = x[0]
        if x[1] < MaxDecrease:
            MaxDecrease = x[1]
            DecDate = x[0]
    MaxIncrease = str(MaxIncrease)
    MaxDecrease = str(MaxDecrease)
    print("Financial Analysis")
    print('-' * 30)
    # The total number of months included in the dataset
    print('Total Month: ' + str(monthCount))
    # The total net amount of "Profit/Losses" over the entire period
    print('Total Revenue: $' + str(TotalNet))
    # The average change in "Profit/Losses" between months over the entire period
    average = TotalNet / monthCount
    print('Total Average: $' + str(int(average)))
    # The greatest increase in profits (date and amount) over the entire period
    print("Greatest Increase in Profits: " + IncDate + " ($" + MaxIncrease + ")")
    # The greatest decrease in losses (date and amount) over the entire period
    print("Greatest Decrease in Profits: " + DecDate + " ($" + MaxDecrease + ")")
