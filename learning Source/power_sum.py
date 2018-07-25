#!/usr/bin/python
#Filename: power_sum.py

def powersum(power,*args):
    '''Return the sum of each argument raised to specified power'''
    total = 0
    for i in args:
        total += pow(i,power)  #i^power
    return total

Resultone = powersum(2,3,4)
print  'resultone is ',Resultone


Resulttwo = powersum(2,10)
print 'resulttwo is ',Resulttwo




