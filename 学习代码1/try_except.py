#!/usr/bin/python
#Filename:try_except.py

import  sys

try:
    s = raw_input('Enter something-->')
except EOFEttor:
    print '\n Why did you do an EOF on me?'
    sys.exit() #exit the program
except:
    print '\n Some error/exception occurred.'
    #here .we are not exitong the program

print 'Done'

