#!/usr/bin/python
# -*- coding: ascii -*-

import os.path
import connect
import traceback

base = 'data'				# Base file name

# Find file name that does not already exist
seq = 0
while True :
    file = '%s-%04d.csv' % (base, seq)
    if not os.path.exists(file) : break
    seq += 1

total = 0
start = 0
count = 3
# Save data from Keithley device in a CSV file
s = connect.connect()
s.send('format:elements reading, channel, rnumber, tstamp\n')
s.send('trace:points:actual?\n')
total = int(s.recv(4096))
total -= total % count # Truncate to a multiple of count
print 'Reading ' + str(total) + ' data points.'
with open(file, 'wb') as f :
    # Write heading row to file
    f.write('VDC,TIME,DATE,RDNG,CHAN,')
    f.write('VDC,TIME,DATE,RDNG,CHAN,')
    f.write('VDC,TIME,DATE,RDNG,CHAN\n')
    while start < total :
        s.send('trace:data:selected? ' + str(start) + ', ' + str(count) + '\n')
        f.write(s.recv(4096))
        start += count
s.close()

print 'Wrote ' + str(total/count) + ' rows to ' + file
