from math import *

print "please enter the principal amount: "
PV = float(raw_input())
print "please enter the time period in years: "
T = float(raw_input())
print "please specify the annual interest rate in percentage: "
r = float(raw_input())

t = 0

while True:
    print("type 1 for discrete compounding or 2 for continous compounding:")
    mode = raw_input()
    if mode == '1':
        FV = PV * (1 + r/100)**(T-t)
        print "The accumulated value after", T, "years is", FV
        break
    elif mode == '2':
        FV = PV * exp(r/100*(T-t))
        print "The accumulated value after", T, "years is", FV
        break
    else:
        print 'error, type 1 or 2'
        continue
