import csv

# open file
with open('budget_data.csv', newline='') as F:
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

    average = TotalNet / monthCount

    with open('results.csv', 'wt') as csvfile:
        x = [
        "Financial Analysis", ('-' * 30),
        ('Total Month: ' + str(monthCount)),
        ('Total Revenue: $' + str(TotalNet)),
        ('Total Average: $' + str(int(average))),
        ("Greatest Increase in Profits: " + IncDate + " ($" + MaxIncrease + ")"),
        ("Greatest Decrease in Profits: " + DecDate + " ($" + MaxDecrease + ")")
        ]

        writer = csv.writer(csvfile)
        for row in x:
            print(row)
            writer.writerow([row])
