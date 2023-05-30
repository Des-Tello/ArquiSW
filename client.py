import socket
import time
import sys

# Create a TCP/IP socket
sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
server_address = ('localhost', 5000)
print ('connecting to {} port {}'.format (*server_address))
sock.connect (server_address)

print("Menu: ")
print("1 - Login")
print("2 - Registro")
opcion = input("¿Que desea hacer? ")
try:
    # Login
    if opcion == '1':
        Rut = input("Ingrese el Rut:")
        Contrasena = input("Ingrese la Contrasena:")

        largo = len(Rut+Contrasena+opcion) + 13

        message = '000{}login {} {} {}'.format(largo,opcion,Rut,Contrasena).encode()
        print ('sending {!r}'.format (message))
        sock.sendall (message)
    
    # Registro
    elif opcion == '2':
        Nombre = input("Ingrese el Nombre:")
        Rut = input("Ingrese el Rut:")
        Correo = input("Ingrese el Correo:")
        Contrasena = input("Ingrese la Contrasena:")
        Telefono = input("Ingrese el Telefono :")
        Rol = input("Ingrese el Rol:")
        Jardin  = input("Ingrese el Jardin :")

        largo = len(Nombre+Rut+Correo+Contrasena+Telefono+Rol+Jardin+opcion) + 13

        message = '000{}regis {} {} {} {} {} {} {} {}'.format(largo,opcion,Nombre,Rut,Correo,Contrasena,Telefono,Rol,Jardin).encode()
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
