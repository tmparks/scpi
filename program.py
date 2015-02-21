#!/usr/bin/python
# Copyright 2014-2015 Thomas M. Parks <tmparks@yahoo.com>

import connect

commands = 'keithley.txt'   # Name of file with commands

# Load commands from file and send to Keithley device
s = connect.connect()
s.send('system:clear\n')		# Clear error queue
with open(commands, 'rb') as f :
    for line in f :
        if line[0] == '\n' : continue	# Empty line
        if line[0] == '%'  : continue	# Comment
        s.send(line)
        print line,
        s.send('system:error?\n')		# Print error queue
        print s.recv(4096),
s.close()
