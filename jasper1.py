# please comment your code

P = 0
r = 0
t = 0
n = 0

while P <= 0:
    P = float(input("Please input the starting amount: £"))
    if P <= 0:
        print("Invalid entry")

while r <= 0:
    r = float(input("Please input the rate of interest as a percentage: "))
    if r <= 0:
        print("Invalid entry")

while t <= 0:
    t = int(input("Please input the number of years the amount is invested for: "))
    if t <= 0:
        print("Invalid entry")

while n <= 0:
    n = int(input("Please input the number of times the investment is compounded per year: "))
    if n <= 0:
        print("Invalid entry")

A = P *((1 + ((r/100)/n))**(n*t))

print("£", P, "invested at", r, "% for", t, "years compunded", n, "times a year is £", round(A, 2))
