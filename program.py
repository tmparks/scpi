#!/usr/bin/env python3
# Copyright 2014-2019 Thomas M. Parks <tmparks@yahoo.com>

from connect import connect
from datetime import datetime

commandFile = 'keithley.txt' # Name of file with commands

# Sends a command and prints the error status
def command(socket, line):
    line = line.strip()              # Remove extra whitespace
    if not line             : return # Empty line
    if line.startswith('%') : return # Comment
    socket.sendall(line + '\n')
    print(line)
    socket.sendall('system:error?\n')
    print(socket.recv(4096))

s = connect()
command(s, 'system:clear') # Clear error queue

# Set date and time
now = datetime.now()
command(s, 'system:date {0}, {1}, {2}'.format(now.date().year, now.date().month, now.date().day))
command(s, 'system:time {0}, {1}, {2}'.format(now.time().hour, now.time().minute, now.time().second))

# Load commands from file and send to device
with open(commandFile, 'rb') as f :
    for line in f :
        command(s, line)
s.close()
