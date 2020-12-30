import sys
import csv

if len(sys.argv) != 2:
    raise SystemExit("usage: third.py filename")

account = None
total = 0.0
total_items = 0
filename = sys.argv[1]

with open(filename, "r") as f:
    rows = csv.reader(f)
    header = next(f)
    for i, row in enumerate(rows):
        row[2] = int(row[2])
        row[6] = float(row[6])

        if account is None:
            account = row[1]
        total_items += row[2]
        total += row[2] * row[6]

print("Account Name: {}".format(account))
print("Total Items: {:<5d}".format(total_items))
print("Total: {:<10.2f}".format(total))
print("Number of lines processed: {:<5d}".format(i+1))
