#!/usr/bin/python
# Copyright 2014-2015 Thomas M. Parks <tmparks@yahoo.com>

import os.path
import connect

base = 'data'       # Base file name
chan = 4            # Number of channels to read

# Find file name that does not already exist
for n in range(10000) :
    name = base + '-{0:04d}.csv'.format(n)
    if not os.path.exists(name) : break

# Save data from Keithley device in a CSV file
total = 0
s = connect.connect()
s.sendall('format:elements reading, channel, rnumber, tstamp\n')
s.sendall('trace:points:actual?\n')
total = int(s.recv(4096))
total -= total % chan # Truncate to a multiple of chan
print('Reading ' + str(total) + ' data points.')
with open(name, 'wb') as f :
    # Write heading row to file
    heading = 'V{0},T{0},D{0},RDNG,CHAN'
    for n in range(chan) :
        if (n > 0) : f.write(',')
        f.write(heading.format(101 + n))
    f.write('\n')
    for n in range(0, total, chan) :
        s.sendall('trace:data:selected? ' + str(n) + ', ' + str(chan) + '\n')
        f.write(s.recv(4096))
s.close()

print('Wrote ' + str(total/chan) + ' rows to ' + name)
