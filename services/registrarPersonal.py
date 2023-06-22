import socket
import sys
# Create a TCP/IP socket
sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
server_address = ('localhost', 5000)
print ('connecting to {} port {}'.format (*server_address))
sock.connect (server_address)
try:
    # Send data
    message = b'00010sinitnewpe'
    print ('sending {!r}'.format (message))
    sock.sendall (message)
    while True:
        # Look for the response
        print ("Waiting for register transaction")
        amount_received = 0
        amount_expected = int(sock.recv(5))
        while amount_received < amount_expected:
            data = sock.recv (amount_expected - amount_received)
            amount_received += len (data)
            print('received {!r}'.format(data))
            print ("Registrando Personal...")
            data = data.decode().split()
            try:
                opcion = data[1]
                Nombre = data[2]
                Apellido = data[3]
                Rut = data[4]
                Cargo = data[5]
                FechaNacimiento = data[6]
                Jardin = data[7]

                largo = len(Nombre+Apellido+Rut+Cargo+FechaNacimiento+Jardin+opcion) + 15

                message = '000{}datos {} {} {} {} {} {} {}'.format(largo,Nombre,Apellido,Rut,Cargo,FechaNacimiento,Jardin,opcion).encode()
                print ('sending to bbdd {!r}'.format (message))
                sock.sendall(message)
            except:
                pass
            print('-------------------------------')
finally:
    print ('closing socket')
    sock.close ()