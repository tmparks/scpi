# Open a socket connection.
import socket

port = 1394

direct = '169.254.1.1'
colgate = '149.43.56.221'
home = '192.168.1.37'

hosts = (direct, colgate, home)

def connect():
    isConnected = False
    for host in hosts:
        s = socket.socket()
        s.settimeout(10.0)
        address = (host, port)
        try:
            s.connect(address)
            isConnected = True
            break
        except socket.error as e :
            error = e
            s.close()
    if False == isConnected :
        print 'Connection failed!'
        raise error
    return s
