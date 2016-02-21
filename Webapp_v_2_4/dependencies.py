#!/usr/bin/env python

# Setting up the environment

import subprocess
import sys

#List commands to execute here.

SOLRPY = "sudo pip install -U solrpy"
FLASK = "sudo pip install -U flask"


#order commands in sequence
cmds = [SOLRPY, FLASK]

#Iterates over list, running statements for each item in the list
count=0
for cmd in cmds:
    count+=1
    print "Running Command Number %s" % count
    subprocess.call(cmd, shell=True)