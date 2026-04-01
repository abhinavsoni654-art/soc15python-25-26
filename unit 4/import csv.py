import csv

row_count = 0

with open('data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
        row_count += 1

print(f"Number of rows in the CSV file: {row_count}")