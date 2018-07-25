#!/usr/bin/python
#Filename: If.py

number = 23 
guess = int(raw_input('Enter an integer:'))
if guess == number:
    print 'Congratulations, you guesses it.'
    print "(but you do not win any peizes!)"
elif guess > number:
    print 'NO,it is a little higher than that'
else:
    print "No,it is a little lower than that"

print "Done"
