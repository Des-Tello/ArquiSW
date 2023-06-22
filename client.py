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
print("2 - Registro Usuario")
print("3 - Registro Alumno")
print("4 - Actualización Alumno")
print("5 - Borrar Alumno")
print("6 - Control Asistencia")
print("7 - Creacion Jardín")
print("8 - Actualización Jardín")
print("9 - Eliminar Jardín")
print("10 - Estadísticas Jardín")
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
    
    # Registro Alumno - newal
    elif opcion == '3':
        Rut = input("Ingrese el Rut: ")
        Nombre = input("Ingrese el Nombre: ")
        Apellido = input("Ingrese el Apellido: ")
        FechaNacimiento = input("Ingrese el Fecha de Nacimiento (YYYY-MM-DD): ")
        JardinID = input("Ingrese el ID del Jardin: ")
        CursoID = input("Ingrese el ID del Curso: ")

        largo = len(Rut+Nombre+Apellido+FechaNacimiento+JardinID+CursoID+opcion) + 13

        message = '000{}newal {} {} {} {} {} {} {}'.format(largo,opcion,Rut,Nombre,Apellido,FechaNacimiento,JardinID,CursoID).encode()
        print ('sending {!r}'.format (message))
        sock.sendall( message )

    # Actualización Alumno - updal
    elif opcion == '4':
        Rut = input("Ingrese el Rut: ")
        Nombre = input("Ingrese el Nombre: ")
        Apellido = input("Ingrese el Apellido: ")
        FechaNacimiento = input("Ingrese el Fecha de Nacimiento (YYYY-MM-DD): ")
        JardinID = input("Ingrese el ID del Jardin: ")
        CursoID = input("Ingrese el ID del Curso: ")

        largo = len( Rut+Nombre+Apellido+FechaNacimiento+JardinID+CursoID+opcion ) + 13

        message = '000{}updal {} {} {} {} {} {} {}'.format( largo,opcion,Rut,Nombre,Apellido,FechaNacimiento,JardinID,CursoID ).encode()
        print ('sending {!r}'.format (message))
        sock.sendall( message )

    # Borrar Alumno - delal
    elif opcion == '5':
        Rut = input("Ingrese el Rut: ")

        largo = len( Rut ) + 13

        message = '000{}delal {} {}'.format( largo,opcion,Rut ).encode()
        print ('sending {!r}'.format (message))
        sock.sendall( message )

    # Control Asistencia - conas
    elif opcion == '6':
        Rut = input("Ingrese el rut del alumno o personal: ")
        Fecha = input("Ingrese la Fecha (YYYY-MM-DD): ")
        Estado = input("Asiste (1-SI 0-NO) ")

        largo = len( Rut+Fecha+Estado ) + 13

        message = '000{}conas {} {} {} {}'.format( largo,opcion,Rut,Fecha,Estado ).encode()
        print ('sending {!r}'.format (message))
        sock.sendall( message )

    # Creacion Jardin - newja
    elif opcion == '7':
        Nombre = input("Ingrese el nombre del jardín a crear: ").replace(' ','-')
        Direccion = input("Ingrese la dirección del jardín: ").replace(' ','-')
        Telefono = input("Ingrese el numero de telefono asociado: +56 9 ")

        largo = len(Nombre+Direccion+Telefono) + 12

        message = '000{}newja {} {} {} {}'.format( largo,opcion,Nombre,Direccion,Telefono ).encode()
        print ('sending {!r}'.format (message))
        sock.sendall( message )

    # Actializar Jardin - updja
    elif opcion == '8':
        Nombre = input("Ingrese el nombre del jardín a actualizar: ")
        Direccion = input("Ingrese la nueva dirección: ").replace(' ','-')
        Telefono = input("Ingrese el nuevo numero de telefono: +56 9")

        largo = len( Nombre+Direccion+Telefono ) + 12

        message = '000{}updja {} {} {} {}'.format( largo,opcion,Nombre,Direccion,Telefono ).encode()
        print ('sending {!r}'.format (message))
        sock.sendall( message )

    # Eliminar Jardin - delja
    elif opcion == '9':
        Nombre = input("Ingrese el nombre del jardín a eliminar: ")

        largo = len( Nombre ) + 10

        message = '000{}delja {} {}'.format( largo,opcion,Nombre ).encode()
        print ('sending {!r}'.format (message))
        sock.sendall( message )
    
    # Estadisticas Jardin - estja
    elif opcion == '10':
        Nombre = input("Ingrese el nombre del jardín para consultar estadisticas: ")
        
        largo = len( Nombre ) + 10

        message = '000{}estja {} {}'.format( largo,opcion,Nombre ).encode()
        print ('sending {!r}'.format (message))
        sock.sendall( message )


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
