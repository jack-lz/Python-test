#!/usr/bin/python
#Filename:mymodule.py

def sayhi():
    print "Hi,this is mymodule speaking."


    if __name__ == "__main__":
        print "this program is being run by itself"
    else:
        print "this program is being imported from another module"
        print "__name__ is", __name__

version = "0.1"

   
