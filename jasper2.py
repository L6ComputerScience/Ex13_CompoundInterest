A = 0
r = 0
t = 0
n = 0

while A <= 0:
    A = float(input("Please input the amount after compund interest: £"))
    if A <= 0:
        print("Invalid entry")

while r <= 0:
    r = float(input("Please input the rate of interest as a percentage: "))
    if r <= 0:
        print("Invalid entry")

while t <= 0:
    t = int(input("Please input the number of years the amount was invested for: "))
    if t <= 0:
        print("Invalid entry")

while n <= 0:
    n = int(input("Please input the number of times the investment was compounded per year: "))
    if n <= 0:
        print("Invalid entry")

P = A/((1 + ((r/100)/n))**(n*t))

print("£", round(P, 2), "was invested at", r, "% for", t, "years compunded", n, "times a year resulting in £", A)
