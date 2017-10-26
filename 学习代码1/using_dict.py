#!/usr/bin/python
#Filename:using_dict.py

#'ab' is short for 'a'ddress 'b'ook

ab = {'Swaroop':'swaroopch@byteofpython.info',
      'Larry':'larry@wall.org',
      'Mastsumoto':'matz@ruby-lang.org',
      'Spammer':'spammer@hotmail.com'
     }

print "Swaroop's address is %s" % ab['Swaroop']

#Adding a key/value pair
ab['Guido'] = 'guido@python.org'

#Deleting a key/value pair
del ab['Spammer']

print '\n There are %d contacts in the address-book\n' % len(ab)

for name,address in ab.items():
    print 'Comtact %s at %s' % (name, address)

if 'Guido' in ab:  #OR ab.has_key('Guido')
    print "\n Guido's address is %s" % ab['Guido']

    
