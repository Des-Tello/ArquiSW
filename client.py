import socket
import time
import sys

def obtenerRut():
    while True:
        rut = input("Ingrese el Rut sin puntos y con guion: ")

        rut = rut.lower()
        rut = rut.replace(".", "")
        rut = rut.replace("-", "")
        cuerpo, dv = rut[:-1], rut[-1]
        
        if not cuerpo.isdigit() or dv not in '0123456789k':
            print("* * * Ingrese un rut valido * * *")
        else:
            reverse_cuerpo = cuerpo[::-1]
            factor = 2
            suma = 0
            for c in reverse_cuerpo:
                suma += factor * int(c)
                factor = factor + 1 if factor < 7 else 2

            res = suma % 11
            dvr = 'k' if 11 - res == 10 else str(11 - res)
            if (dv == dvr):
                return rut

def obtenerNumero():
    while True:
        Telefono = input("Ingrese el numero telefonico: ")
        if not Telefono.isdigit() and (len(Telefono)!=8):
            print("* * * Porfavor ingrese un numero valido * * *")
        else:
            return Telefono

def respuesta():
    time.sleep(2)
    data = sock.recv(4096).decode()
    print("recibido")
    if 'exito' in data:
        return True
    return False



while True:
    # Create a TCP/IP socket
    sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 5000)
    print ('connecting to {} port {}'.format (*server_address))
    sock.connect (server_address)

    print("Menu: ")
    print("0 - Salir")
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
    print('11 - Eliminar Usuario')
    print('12 - Actualizar Usuario')
    print('13 - Registo Personal ')
    print("14 - Asistencia por Jardin")
    print("15 - Comparación Asistencia")
    print("16 - Visualización Asistencia de Personal")

    opcion = input("¿Que desea hacer? ")
    try:
        if opcion == '0':
            print("Saliendo...")
        # Login
        if opcion == '1':
            Rut = obtenerRut()
            Contrasena = input("Ingrese la Contrasena:")

            largo = len(Rut+Contrasena+opcion) + 13

            message = '000{}login {} {} {}'.format(largo,opcion,Rut,Contrasena).encode()
            print ('sending {!r}'.format (message))
            sock.sendall (message)
            if respuesta():
                print("Login realizado correctamente")
        
        # Registro
        elif opcion == '2':
            Nombre = input("Ingrese el Nombre:")
            Rut = obtenerRut()
            Correo = input("Ingrese el Correo:")
            Contrasena = input("Ingrese la Contrasena:")
            Telefono = obtenerNumero()
            Rol = input("Ingrese el Rol:")
            Jardin  = input("Ingrese el Jardin :")

            largo = len(Nombre+Rut+Correo+Contrasena+Telefono+Rol+Jardin+opcion) + 13

            message = '000{}regis {} {} {} {} {} {} {} {}'.format(largo,opcion,Nombre,Rut,Correo,Contrasena,Telefono,Rol,Jardin).encode()
            print ('sending {!r}'.format (message))
            sock.sendall (message)
            if respuesta():
                print("Registro realizado correctamente")

        # Registro Alumno - newal
        elif opcion == '3':
            Rut = obtenerRut()
            Nombre = input("Ingrese el Nombre: ")
            Apellido = input("Ingrese el Apellido: ")
            FechaNacimiento = input("Ingrese el Fecha de Nacimiento (YYYY-MM-DD): ")
            NombreJardin = input("Ingrese el nombre del Jardin: ").replace(" ", "-")
            CursoID = input("Ingrese el ID del Curso: ")

            largo = len(Rut+Nombre+Apellido+FechaNacimiento+NombreJardin+CursoID+opcion) + 13

            message = '000{}newal {} {} {} {} {} {} {}'.format(largo,opcion,Rut,Nombre,Apellido,FechaNacimiento,NombreJardin,CursoID).encode()
            print ('sending {!r}'.format (message))
            sock.sendall( message )
            if respuesta():
                print("Registro de alumno realizado correctamente")

        # Actualización Alumno - updal
        elif opcion == '4':
            Rut = obtenerRut()
            Nombre = input("Ingrese el Nombre: ")
            Apellido = input("Ingrese el Apellido: ")
            FechaNacimiento = input("Ingrese el Fecha de Nacimiento (YYYY-MM-DD): ")
            NombreJardin = input("Ingrese el nombre del Jardin: ").replace(" ", "-")
            CursoID = input("Ingrese el ID del Curso: ")

            largo = len( Rut+Nombre+Apellido+FechaNacimiento+NombreJardin+CursoID+opcion ) + 13

            message = '000{}updal {} {} {} {} {} {} {}'.format( largo,opcion,Rut,Nombre,Apellido,FechaNacimiento,NombreJardin,CursoID ).encode()
            print ('sending {!r}'.format (message))
            sock.sendall( message )
            if respuesta():
                print("Alumno actualizado correctamente")

        # Borrar Alumno - delal
        elif opcion == '5':
            Rut = obtenerRut()

            largo = len( Rut ) + 13

            message = '000{}delal {} {}'.format( largo,opcion,Rut ).encode()
            print ('sending {!r}'.format (message))
            sock.sendall( message )
            if respuesta():
                print("Almuno eliminado correctamente")

        # Control Asistencia - conas
        elif opcion == '6':
            Rut = obtenerRut()
            Fecha = input("Ingrese la Fecha (YYYY-MM-DD): ")
            Estado = input("Asiste (1-SI 0-NO) ")

            largo = len( Rut+Fecha+Estado ) + 13

            message = '000{}conas {} {} {} {}'.format( largo,opcion,Rut,Fecha,Estado ).encode()
            print ('sending {!r}'.format (message))
            sock.sendall( message )
            if respuesta():
                print("Asistencia mostrada correctamente en el servicio")

        # Creacion Jardin - newja
        elif opcion == '7':
            NombreJardin = input("Ingrese el nombre del jardín a crear: ").replace(' ','-')
            Direccion = input("Ingrese la dirección del jardín: ").replace(' ','-')
            Telefono = obtenerNumero()

            largo = len(NombreJardin+Direccion+Telefono+opcion) + 12

            message = '000{}newja {} {} {} {}'.format( largo,opcion,NombreJardin,Direccion,Telefono ).encode()
            print ('sending {!r}'.format (message))
            sock.sendall( message )
            if respuesta():
                print("Jardin creado correctamente")

        # Actualizar Jardin - updja
        elif opcion == '8':
            Nombre1 = input("Ingrese el nombre del jardín a actualizar: ")
            Nombre2 = input("Ingrese el nuevo nombre para este jardin: ").replace(' ','-')
            Direccion = input("Ingrese la nueva dirección: ").replace(' ','-')
            Telefono = obtenerNumero()

            largo = len( Nombre1+Nombre2+Direccion+Telefono ) + 13

            message = '000{}updja {} {} {} {} {}'.format( largo,opcion,Nombre1,Nombre2,Direccion,Telefono ).encode()
            print ('sending {!r}'.format (message))
            sock.sendall( message )
            if respuesta():
                print("Jardin actualizado correctamente")

        # Eliminar Jardin - delja
        elif opcion == '9':
            Nombre = input("Ingrese el nombre del jardín a eliminar: ").replace(' ','-')

            largo = len( Nombre ) + 10

            message = '000{}delja {} {}'.format( largo,opcion,Nombre ).encode()
            print ('sending {!r}'.format (message))
            sock.sendall( message )
            if respuesta():
                print("Jardin eliminado correctamente") 

        # Estadisticas Jardin - estja
        elif opcion == '10':
            Nombre = input("Ingrese el nombre del jardín para consultar estadisticas: ").replace(' ','-')
            
            largo = len( Nombre ) + 10

            message = '000{}estja {} {}'.format( largo,opcion,Nombre ).encode()
            print ('sending {!r}'.format (message))
            sock.sendall( message )
            if respuesta():
                print("Estadisticas del jardin presentadas en el servicio")

        #Eliminar usuario - delus
        elif opcion == '11': 
            Rut = obtenerRut()

            largo = len( Rut ) + 10

            message = '000{}delus {} {}'.format( largo,opcion,Rut ).encode()
            print ('sending {!r}'.format (message))
            sock.sendall( message )
            if respuesta():
                print("Usuario eliminado correctamente")

        #Actualizacion de usuario - updus
        elif opcion == '12':
            Rut = obtenerRut()
            Nombre = input("Ingrese el nuevo nombre: ")
            Correo = input("Ingrese el nuevo correo: ")
            Contrasena = input("Ingrese la nueva contraseña: ")
            Telefono = obtenerNumero()
            Rol = input("Ingrese el nuevo rol: ")
            Jardin = input("Ingrese el nuevo jardin: ")

            largo = len( Nombre+Rut+Correo+Contrasena+Telefono+Rol+Jardin ) + 16

            message = '000{}updus {} {} {} {} {} {} {} {}'.format( largo,opcion,Nombre,Rut,Correo,Contrasena,Telefono,Rol,Jardin ).encode()
            print ('sending {!r}'.format (message))
            sock.sendall( message )
            if respuesta():
                print("Usuario actualizado correctamente")

        #Registrar Personal - newpe
        elif opcion == '13':
            Rut = obtenerRut()
            Jardin = input("Ingrese el nombre del jardin: ")
            Nombre = input("Ingrese el nombre del personal: ")
            Apellido = input("Ingrese el apellido del personal: ")
            Cargo = input("Ingrese el cargo del personal: ")
            FechaNacimiento = input("Ingrese la fecha de nacimiento del personal (YYYY-MM-DD): ")

            largo = len( Rut+Jardin+Nombre+Apellido+Cargo+FechaNacimiento ) + 15

            message = '000{}newpe {} {} {} {} {} {} {}'.format( largo,opcion,Rut,Jardin,Nombre,Apellido,Cargo,FechaNacimiento ).encode()
            print ('sending {!r}'.format (message))
            sock.sendall( message )
            if respuesta():
                print("Personal registrado correctamente")

        # Comparación Asistencia - comas
        elif opcion == '14':
            NivelEducativo1 = input("Ingrese Nivel Educativo 1: ")
            NivelEducativo2 = input("Ingrese Nivel Educativo 2: ")
            FechaDesde = input("Ingrese Fecha desde (YYYY-MM-DD): ")
            FechaHasta = input("Ingrese Fecha hasta (YYYY-MM-DD): ")
            
            largo = len(NivelEducativo1+NivelEducativo2+FechaDesde+FechaHasta+opcion) + 10

            message = '000{}comas {} {} {} {} {}'.format(largo,opcion,NivelEducativo1,NivelEducativo2,FechaDesde,FechaHasta).encode()
            print ('sending {!r}'.format (message))
            sock.sendall( message )
            if respuesta():
                print("Asistencia presentada en el servicio correspondiente")

        # Visualización Asistencia de Personal - asipe
        elif opcion == '15':
            PersonalID = input("Ingrese ID de Personal: ")
            Fecha = input("Ingrese Fecha (YYYY-MM-DD): ")
            
            largo = len(PersonalID+Fecha+opcion) + 10

            message = '000{}asipe {} {} {}'.format(largo,opcion,PersonalID,Fecha).encode()
            print ('sending {!r}'.format (message))
            sock.sendall( message )
            if respuesta():
                print("Asistencia presentada en el servicio correspondiente")

        # Asistencia por jardin - asija
        elif opcion == '16':
            NombreJardin = input("Ingrese Nombre de Jardin: ")
            FechaDesde = input("Ingrese Fecha desde (YYYY-MM-DD): ")
            FechaHasta = input("Ingrese Fecha hasta (YYYY-MM-DD): ")
            
            largo = len(NombreJardin+FechaDesde+FechaHasta+opcion) + 10

            message = '000{}asija {} {} {} {}'.format(largo,opcion,NombreJardin,FechaDesde,FechaHasta).encode()
            print ('sending {!r}'.format (message))
            sock.sendall( message )
            if respuesta():
                print("Asistencia presentada en el servicio correspondiente")


    finally:
        sock.close ()
        
        # print ('closing socket')
        
