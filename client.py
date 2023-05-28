import socket
import time
import sys
# Create a TCP/IP socket
sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
server_address = ('localhost', 5000)
print ('connecting to {} port {}'.format (*server_address))
sock.connect (server_address)
try:
    # Send data
    message = b'00009servi 1 3'
    print ('sending {!r}'.format (message))
    sock.sendall (message)

    data = sock.recv(1024).decode()
    print('received {!r}'.format(data))
    print ("Processing ...")
    
    while True:
        # Look for the response
        print ("Waiting for transaction")
        time.sleep(2)
        data = sock.recv(4096).decode()
        # amount_received += len (data)
        print('received {!r}'.format(data))
        print ("Processing ...")

finally:
    print ('closing socket')
    sock.close ()
