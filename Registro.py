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
    message = b'00010sinitregis'
    print ('sending {!r}'.format (message))
    sock.sendall (message)
    while True:
        # Look for the response
        print ("Waiting for transaction Register")
        amount_received = 0
        amount_expected = int(sock.recv(5))
        while amount_received < amount_expected:
            data = sock.recv (amount_expected - amount_received)
            amount_received += len (data)
            print('received {!r}'.format(data))
            print ("Processing register...")
            data = data.decode().split()
            try:
                Nombre = data[1]
                Rut = data[2]
                Correo = data[3]
                Contrasena = data[4]
                Telefono = data[5]
                Rol = data[6]
                Jardin = data[7]
                
                largo = len(Nombre+Rut+Correo+Contrasena+Telefono+Rol+Jardin) + 12
                message = '000{}datos {} {} {} {} {} {} {}'.format(largo,Nombre,Rut,Correo,Contrasena,Telefono,Rol,Jardin).encode()
                print ('sending to bbdd {!r}'.format (message))
                sock.sendall(message)
                if sock.recv(4096):
                    message = '00010regisexito'.encode()
                    print ('sending {!r}'.format (message))
                    sock.send(message)
            except:
                pass
            print('-------------------------------')

finally:
    print ('closing socket')
    sock.close ()


