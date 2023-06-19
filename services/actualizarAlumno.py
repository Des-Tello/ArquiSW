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
    message = b'00010sinitupdal'
    print ('sending {!r}'.format (message))
    sock.sendall (message)
    while True:
        # Look for the response
        print ("Waiting for Update transaction")
        amount_received = 0
        amount_expected = int(sock.recv(5))
        while amount_received < amount_expected:
            data = sock.recv (amount_expected - amount_received)
            amount_received += len (data)
            print('received {!r}'.format(data))
            print ("Actualizando Alumno...")
            data = data.decode().split()
            try:
                opcion = data[1]
                Rut = data[2]
                Nombre = data[3]
                Apellido = data[4]
                FechaNacimiento = data[5]
                JardinID = data[6]
                CursoID = data[7]
                
                largo = len(Rut+Nombre+Apellido+FechaNacimiento+JardinID+CursoID+opcion) + 13
                message = '000{}datos {} {} {} {} {} {} {}'.format(largo,opcion,Rut,Nombre,Apellido,FechaNacimiento,JardinID,CursoID).encode()
                print ('sending to bbdd {!r}'.format (message))
                sock.sendall(message)
                if sock.recv(4096):
                    message = '00010updalexito'.encode()
                    print ('sending {!r}'.format (message))
                    sock.send(message)
            except:
                pass
            print('-------------------------------')

finally:
    print ('closing socket')
    sock.close ()