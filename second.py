import sys

if len(sys.argv) != 4:
    raise SystemExit("usage: second.py principal rate time")

principal = float(sys.argv[1])
rate = float(sys.argv[2])
time = int(sys.argv[3])

interest = 0.0
loan_at_start = principal
loan_at_end = principal

with open("../Globant/BasicPython/loan_details.txt", "w") as out:
    for year in range(time):
        loan_at_start = loan_at_end
        interest = loan_at_end * (rate / 100)
        loan_at_end += interest
        print("{:>5d} {:>10.2f} {:>10.2f} {:>10.2f}".format(year, loan_at_start, interest, loan_at_end), file=out)

    print("If you borrowed at the bank ${:<10.2f}\nYou would have to pay ${:<10.2f}".format(principal, loan_at_end),
          file=out)
