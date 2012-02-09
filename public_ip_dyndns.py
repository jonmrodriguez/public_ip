#! /usr/bin/python

"""
prints public ip address

(same result as googling(what is my ip))
"""


import my_xml # pure awesomeness! what a great lib
import subprocess # .call and .check_output


# Console LOG
def clog(*args):
    print args

text = subprocess.check_output(['wget', '-q', '-O', '-', 'checkip.dyndns.org'])

# parse xml
xml = my_xml.parse(text)

# custom-crafted by jon on Jan 7, 2012
# the dir() function is a great way to find the names in an object
#  or with no args, the global names
sentence = xml.html.body.value

# the last token is the ip itself
tokens = sentence.split(' ')
ip = tokens[-1]

print ip

