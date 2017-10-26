#!/usr/bin/python
#Filename: break.py

while True:
    s = raw_input("Enter someting:\n");
    if s=="quit":
        break;
    print "Length of the string is:",len(s);
else:
    print "else case";

print "Done"
