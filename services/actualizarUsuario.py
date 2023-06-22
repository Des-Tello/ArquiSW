#Servicio actualizar usuario
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
server_address = ('localhost', 5000)
print ('connecting to {} port {}'.format (*server_address))
sock.connect (server_address)
try:
    #Send data
    message = b'00010sinitupdus'
    print ('sending {!r}'.format (message))
    sock.sendall (message)
    while True:
        #Look for the response
        print ("Waiting for control transaction")
        amount_received = 0
        amount_expected = int(sock.recv(5))
        while amount_received < amount_expected:
            data = sock.recv (amount_expected - amount_received)
            amount_received += len (data)
            print('received {!r}'.format(data))
            print ("Actualización de Usuario...")
            data = data.decode().split()
            try:
                opcion = data[1]
                userID = data[2]
                Nombre = data[3]
                Apellido = data[4]
                Rut = data[5]
                Email = data[6]
                Contrasena = data[7]

                largo = len(userID+Nombre+Apellido+Rut+Email+Contrasena+opcion) + 15

                message = '000{}datos {} {} {} {} {} {} {}'.format(largo,userID,Nombre,Apellido,Rut,Email,Contrasena,opcion).encode()
                print ('sending to bbdd {!r}'.format (message))
                sock.sendall(message)
                if sock.recv(4096):
                    message = '00010updusexito'.encode()
                    print ('sending {!r}'.format (message))
                    sock.send(message)
            except:
                pass
            print('-------------------------------')
finally:
    print ('closing socket')
    sock.close ()