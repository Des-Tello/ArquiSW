import socket
import time
import sys
import logging

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


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

def respuestaLogin():
    time.sleep(2)
    data = sock.recv(4096).decode()
    print("recibido")
    if 'exito' in data:
        #print(data.split()[1])
        rol = int(data.split()[1])
        return True,rol
    return False

def respuesta():
    time.sleep(2)
    data = sock.recv(4096).decode()
    print("recibido")
    if 'exito' in data:
        return True
    return False

def respuesta_registro_alumno():
    time.sleep(2)
    data = sock.recv(4096).decode()
    print("hola")
    logging.info("Datos sexuales {!r}".format(data))
    print("Datos sexuales {!r}".format(data))

def respuestaCrearJardin():
    time.sleep(2)
    data = sock.recv(4096).decode()
    print("recibido")
    print(data.split()[1].replace('-',' '))

def respuestaActualizarJardin():
    data = sock.recv(4096).decode()
    print("recibido")
    print(data.split()[1].replace('-',' '))
    
def respuestaEliminarJardin():
    data = sock.recv(4096).decode()
    print("recibido")
    print(data.split()[1].replace('-',' '))

def respuestaEstadisticasJardin():
    data = sock.recv(4096).decode()
    print("recibido")
    print(data.split()[1].replace('-',' '))

while True:
    # Create a TCP/IP socket
    sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 5000)
    print ('connecting to {} port {}'.format (*server_address))
    sock.connect (server_address)

    print("Menu Principal")
    print("0 - Salir")
    print("1 - Login")
    opcion = input("¿Que desea hacer?")
    try:
        if opcion == '0':
            print("Saliendo...")
        
        # Login
        if opcion == '1':
            Rut = obtenerRut()
            Contrasena = input("Ingrese la Contrasena:")
            largo = len(Rut+Contrasena+opcion)+13
            message = '000{}login {} {} {}'.format(largo,opcion,Rut,Contrasena).encode()
            print ('sending {!r}'.format (message))
            sock.sendall (message)
            loginState,rol = respuestaLogin()

            if loginState == True and rol == 1: #Director
                print("Login de director realizado correctamente")
                
                while True:
                    print("1 - Actualización Alumno")
                    print("2 - Borrar Alumno")
                    print('3 - Registo Personal')
                    print("4 - Control Asistencia")
                    print("5 - Asistencia por Jardin")
                    print("6 - Comparación Asistencia")
                    print("7 - Visualización Asistencia de Personal")
                    opcion = input("¿Que desea hacer? ")
                    try:
                        if opcion == '1':
                            # Actualización Alumno - updal
                            Rut = obtenerRut()
                            Nombre = input("Ingrese el Nombre: ")
                            Apellido = input("Ingrese el Apellido: ")
                            FechaNacimiento = input("Ingrese el Fecha de Nacimiento (YYYY-MM-DD): ")
                            NombreJardin = input("Ingrese el nombre del Jardin: ").replace(" ", "-")
                            CursoID = input("Ingrese el ID del Curso: ")

                            largo = len( Rut+Nombre+Apellido+FechaNacimiento+NombreJardin+CursoID ) + 13 + 1

                            message = '000{}updal {} {} {} {} {} {} {}'.format( largo,4,Rut,Nombre,Apellido,FechaNacimiento,NombreJardin,CursoID ).encode()
                            print ('sending {!r}'.format (message))
                            sock.sendall( message )
                            if respuesta():
                                print("Alumno actualizado correctamente")

                            elif loginState == True and rol == 'nopro':
                                print("Login de usuario normal realizado correctamente")
                    
                        # Borrar Alumno - delal
                        elif opcion == '2':
                            Rut = obtenerRut()

                            largo = len( Rut ) + 13 + 1

                            message = '000{}delal {} {}'.format( largo,5,Rut ).encode()
                            print ('sending {!r}'.format (message))
                            sock.sendall( message )
                            if respuesta():
                                print("Almuno eliminado correctamente")

                        #Registrar Personal - newpe
                        elif opcion == '3':
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

                        # Control Asistencia - conas
                        elif opcion == '4':
                            Rut = obtenerRut()
                            Fecha = input("Ingrese la Fecha (YYYY-MM-DD): ")
                            Estado = input("Asiste (1-SI 0-NO) ")

                            largo = len( Rut+Fecha+Estado ) + 13 + 1

                            message = '000{}conas {} {} {} {}'.format( largo,6,Rut,Fecha,Estado ).encode()
                            print ('sending {!r}'.format (message))
                            sock.sendall( message )
                            if respuesta():
                                print("Asistencia mostrada correctamente en el servicio")

                        # Asistencia por jardin - asija
                        elif opcion == '5':
                            NombreJardin = input("Ingrese Nombre de Jardin: ")
                            FechaDesde = input("Ingrese Fecha desde (YYYY-MM-DD): ")
                            FechaHasta = input("Ingrese Fecha hasta (YYYY-MM-DD): ")
                            
                            largo = len(NombreJardin+FechaDesde+FechaHasta) + 10 + 2

                            message = '000{}asija {} {} {} {}'.format(largo,14,NombreJardin,FechaDesde,FechaHasta).encode()
                            print ('sending {!r}'.format (message))
                            sock.sendall( message )
                            if respuesta():
                                print("Asistencia presentada en el servicio correspondiente")

                        # Comparación Asistencia - comas
                        elif opcion == '6':
                            NivelEducativo1 = input("Ingrese Nivel Educativo 1: ")
                            NivelEducativo2 = input("Ingrese Nivel Educativo 2: ")
                            FechaDesde = input("Ingrese Fecha desde (YYYY-MM-DD): ")
                            FechaHasta = input("Ingrese Fecha hasta (YYYY-MM-DD): ")
                            
                            largo = len(NivelEducativo1+NivelEducativo2+FechaDesde+FechaHasta) + 10 + 2

                            message = '000{}comas {} {} {} {} {}'.format(largo,15,NivelEducativo1,NivelEducativo2,FechaDesde,FechaHasta).encode()
                            print ('sending {!r}'.format (message))
                            sock.sendall( message )
                            if respuesta():
                                print("Asistencia presentada en el servicio correspondiente")

                        # Visualización Asistencia de Personal - asipe
                        elif opcion == '7':
                            PersonalID = input("Ingrese ID de Personal: ")
                            Fecha = input("Ingrese Fecha (YYYY-MM-DD): ")
                            
                            largo = len(PersonalID+Fecha) + 10 + 2

                            message = '000{}asipe {} {} {}'.format(largo,16,PersonalID,Fecha).encode()
                            print ('sending {!r}'.format (message))
                            sock.sendall( message )
                            if respuesta():
                                print("Asistencia presentada en el servicio correspondiente")

                    except:
                        pass
            
            elif loginState == True and rol == 2: #Administrador
                print("Login de administrador realizado correctamente")
                while True:
                    print("1 - Registro Usuario")
                    print('2 - Eliminar Usuario')
                    print("3 - Creacion Jardín")
                    print("4 - Actualización Jardín")
                    print("5 - Eliminar Jardín")
                    print("6 - Estadísticas Jardín")
                    opcion = input("¿Que desea hacer? ")
                    try:
                        # Registro
                        if opcion == '1':
                            Roles = {
                                'Director':1,
                                'Administrador':2,
                                'Usuario':3
                            }
                            Nombre = input("Ingrese el Nombre:")
                            Rut = obtenerRut()
                            Correo = input("Ingrese el Correo:")
                            Contrasena = input("Ingrese la Contrasena:")
                            Telefono = obtenerNumero()
                            Rol = input("Ingrese el Rol (Director - Usuario):")
                            Jardin  = input("Ingrese el Jardin :")
                            Rol = Roles[Rol]
                            largo = len(Nombre+Rut+Correo+Contrasena+Telefono+Rol+Jardin) + 13 + 1

                            message = '000{}regis {} {} {} {} {} {} {} {}'.format(largo,2,Nombre,Rut,Correo,Contrasena,Telefono,Rol,Jardin).encode()
                            print ('sending {!r}'.format (message))
                            sock.sendall (message)
                            if respuesta():
                                print("Registro realizado correctamente")

                        #Eliminar usuario - delus
                        elif opcion == '2': 
                            Rut = obtenerRut()

                            largo = len( Rut ) + 10 + 2

                            message = '000{}delus {} {}'.format( largo,11,Rut ).encode()
                            print ('sending {!r}'.format (message))
                            sock.sendall( message )
                            if respuesta():
                                print("Usuario eliminado correctamente")
                    
                        # Creacion Jardin - newja
                        elif opcion == '3':
                            NombreJardin = input("Ingrese el nombre del jardín a crear: ").replace(' ','-')
                            Direccion = input("Ingrese la dirección del jardín: ").replace(' ','-')
                            Telefono = obtenerNumero()

                            largo = len(NombreJardin+Direccion+Telefono) + 12 + 1

                            message = '000{}newja {} {} {} {}'.format( largo,7,NombreJardin,Direccion,Telefono ).encode()
                            print ('sending {!r}'.format (message))
                            sock.sendall( message)
                            respuestaCrearJardin()
                    
                        # Actualizar Jardin - updja
                        elif opcion == '4':
                            Nombre1 = input("Ingrese el nombre del jardín a actualizar: ")
                            Nombre2 = input("Ingrese el nuevo nombre para este jardin: ").replace(' ','-')
                            Direccion = input("Ingrese la nueva dirección: ").replace(' ','-')
                            Telefono = obtenerNumero()

                            largo = len( Nombre1+Nombre2+Direccion+Telefono ) + 13 + 1

                            message = '000{}updja {} {} {} {} {}'.format( largo,8,Nombre1,Nombre2,Direccion,Telefono ).encode()
                            print ('sending {!r}'.format (message))
                            sock.sendall( message )
                            respuestaActualizarJardin()
                    
                        # Eliminar Jardin - delja
                        elif opcion == '5':
                            Nombre = input("Ingrese el nombre del jardín a eliminar: ").replace(' ','-')

                            largo = len( Nombre ) + 10 + 1

                            message = '000{}delja {} {}'.format( largo,9,Nombre ).encode()
                            print ('sending {!r}'.format (message))
                            sock.sendall( message )
                            respuestaEliminarJardin()

                        # Estadisticas Jardin - estja
                        elif opcion == '6':
                            Nombre = input("Ingrese el nombre del jardín para consultar estadisticas: ").replace(' ','-')
                            
                            largo = len( Nombre ) + 10 + 2

                            message = '000{}estja {} {}'.format( largo,10,Nombre ).encode()
                            print ('sending {!r}'.format (message))
                            sock.sendall( message )
                            respuestaEstadisticasJardin()

                    except:
                        pass

            elif loginState == True and rol == 3: #Usuario
                print("Login de usuario realizado correctamente")
                while True:
                    print("1 - Registro Alumno")
                    print('2 - Actualizar Usuario')
                    opcion = input("¿Que desea hacer? ")
                    try:
                        # Registro Alumno - newal
                        if opcion == '1':
                            Rut = obtenerRut()
                            Nombre = input("Ingrese el Nombre: ")
                            Apellido = input("Ingrese el Apellido: ")
                            FechaNacimiento = input("Ingrese el Fecha de Nacimiento (YYYY-MM-DD): ")
                            NombreJardin = input("Ingrese el nombre del Jardin: ").replace(" ", "-")
                            CursoID = input("Ingrese el ID del Curso: ")

                            largo = len(Rut+Nombre+Apellido+FechaNacimiento+NombreJardin+CursoID) + 13 + 1

                            message = '000{}newal {} {} {} {} {} {} {}'.format(largo,3,Rut,Nombre,Apellido,FechaNacimiento,NombreJardin,CursoID).encode()
                            print ('sending {!r}'.format (message))
                            sock.sendall( message )

                            respuesta_registro_alumno()

                            # if respuesta():
                            #     print("Registro de alumno realizado correctamente")
                            
                        #Actualizacion de usuario - updus
                        elif opcion == '2':
                            Rut = obtenerRut()
                            Nombre = input("Ingrese el nuevo nombre: ")
                            Correo = input("Ingrese el nuevo correo: ")
                            Contrasena = input("Ingrese la nueva contraseña: ")
                            Telefono = obtenerNumero()
                            Rol = input("Ingrese el nuevo rol: ")
                            Jardin = input("Ingrese el nuevo jardin: ")

                            largo = len( Nombre+Rut+Correo+Contrasena+Telefono+Rol+Jardin ) + 16 + 1

                            message = '000{}updus {} {} {} {} {} {} {} {}'.format( largo,4,Nombre,Rut,Correo,Contrasena,Telefono,Rol,Jardin ).encode()
                            print ('sending {!r}'.format (message))
                            sock.sendall( message )
                            if respuesta():
                                print("Usuario actualizado correctamente")

                    except:
                        pass
        
    finally:
        sock.close ()
