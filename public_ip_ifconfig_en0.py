#! /usr/bin/python

"""
prints public ip address

(parses results of ifconfig.
 should give same result as what's seen in system preferences)
"""

import subprocess # .call and .check_output

text = subprocess.check_output(['ifconfig', 'en0'])

# splits on all whitespace. pretty nifty
tokens = text.split()

for i in range(0, len(tokens)):
    
    if tokens[i] == 'inet':
    
        # the token after inet is the public ip
        print tokens[i+1]

