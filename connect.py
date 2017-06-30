# Open a socket connection.
# Copyright 2014-2017 Thomas M. Parks <tmparks@yahoo.com>

import socket

port = 1394

direct = '169.254.1.1'
campus = '149.43.56.221'
home = '192.168.1.37'

hosts = (direct, campus, home)

def connect():
    print 'Connecting from',
    for (_, _, _, _, (host, _)) in socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET) :
        print host,
    print
    s = None
    error = None
    for host in hosts :
        try :
            s = socket.socket()
            s.settimeout(5.0)
            address = (host, port)
            s.connect(address)
            break
        except socket.error as e :
            print host, e
            error = e
            s.close()
            s = None
    if s is None :
        print 'Connection failed!'
        raise error
    (host, _) = s.getpeername()
    print 'Connected to', host
    s.settimeout(10.0)
    return s
