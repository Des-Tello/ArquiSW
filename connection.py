import sqlite3
import socket
import sys
init_sql_file = "./db/init.sql"

def read_init_sql(file_path):
    with open(file_path, "r") as sql_file:
        sql_script = sql_file.read()
        cursor.executescript(sql_script)

def registro(nombre, rut, correo, contrasena, telefono, rol, jardin):
    cursor.execute("""
        SELECT COUNT(*) FROM Usuarios WHERE Rut = ?
    """, (rut,))
    count = cursor.fetchone()[0]
    
    if count > 0:
        print("El usuario ya está registrado.")
    else:
        cursor.execute("""
            INSERT INTO Usuarios (Nombre, Rut, Correo, Contrasena, Telefono, Rol, Jardin)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (nombre, rut, correo, contrasena, telefono, rol, jardin))
        conn.commit()
        print("Usuario registrado con éxito.")

def login(rut, contrasena):
    cursor.execute("""
        SELECT COUNT(*) FROM Usuarios WHERE Rut = ? AND Contrasena = ?
    """, (rut, contrasena))
    rows = cursor.fetchall()

    if len(rows) > 0:
        print("Login Exitoso.")

def registroAlumno(Rut,Nombre,Apellido,FechaNacimiento,NombreJardin,CursoID):
    cursor.execute("""
        SELECT COUNT(*) FROM ALUMNO WHERE Rut = ?
    """, (Rut,))
    count_alumno = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*) FROM JARDIN WHERE NombreJardin = ?
    """, (NombreJardin,))
    count_jardin = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*) FROM CURSO WHERE CursoID = ? and NombreJardin = ?
    """, (CursoID,NombreJardin))
    count_curso = cursor.fetchone()[0]
    
    if count_alumno > 0:
        print("El alumno ya está registrado.")
    elif count_jardin < 1:
        print("El jardín no existe.")
    # elif count_curso < 1:
    #     print("El curso no existe en el jardín asociado.")
    else:
        cursor.execute("""
            INSERT INTO ALUMNO (Rut, Nombre, Apellido, FechaNacimiento, NombreJardin, CursoID)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (Rut, Nombre, Apellido, FechaNacimiento, NombreJardin, CursoID))
        conn.commit()
        print("Alumno registrado con éxito.")

def actualizarAlumno(Rut,Nombre,Apellido,FechaNacimiento,NombreJardin,CursoID):
    cursor.execute("""
        SELECT COUNT(*) FROM ALUMNO WHERE Rut = ?
    """, (Rut,))
    count_alumno = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*) FROM JARDIN WHERE NombreJardin = ?
    """, (NombreJardin,))
    count_jardin = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*) FROM CURSO WHERE CursoID = ? and NombreJardin = ?
    """, (CursoID,NombreJardin))
    count_curso = cursor.fetchone()[0]
    
    if count_alumno < 1:
        print("Alumno no existente.")
    elif count_jardin < 1:
        print("El jardín no existe.")
    # elif count_curso < 1:
    #     print("El curso no existe en el jardín asociado.")
    else:
        cursor.execute("""
            UPDATE ALUMNO 
            SET CursoID = ?, NombreJardin = ?, Nombre = ?, Apellido = ?, FechaNacimiento = ?
            WHERE Rut = ?
        """, (CursoID, NombreJardin, Nombre, Apellido, FechaNacimiento, Rut))
        conn.commit()
        print("Alumno actualizado con éxito.")
        
def borrarAlumno(Rut):
    cursor.execute("""
        SELECT COUNT(*) FROM ALUMNO WHERE Rut = ?
    """, (Rut,))
    count = cursor.fetchone()[0]
    
    if count > 0:
        cursor.execute("""
            DELETE FROM ALUMNO 
            WHERE Rut = ?
        """, (Rut,))
        conn.commit()
        print("Alumno borrado con éxito.")
    else:
        print("No hay ningun alumno existente.")
        
def controlAsistencia(PersonaRut,Fecha,Estado):
    cursor.execute("""
        SELECT COUNT(*) FROM ALUMNO WHERE Rut = ?
    """, (PersonaRut,))
    count_alumno = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*) FROM ALUMNO WHERE Rut = ?
    """, (PersonaRut,))
    count_personal = cursor.fetchone()[0]

    if count_alumno < 1 and count_personal < 1:
        print("No se ha encontrado ningun rut asociado")
    else:
        cursor.execute("""
            INSERT INTO ASISTENCIA (PersonaRut, Fecha, Estado)
            VALUES (?, ?, ?);
        """, (PersonaRut, Fecha, Estado))
        conn.commit()
        print("Asistencia registrada con éxito.")

def creacionJardin(NombreJardin, Direccion, Telefono):
    try:
        cursor.execute("""
            SELECT COUNT(*) FROM Jardin WHERE NombreJardin = ?
        """,(NombreJardin,))
        existe = cursor.fetchone()[0]
        if existe == 0:
            cursor.execute("""
                INSERT INTO Jardin (NombreJardin, Direccion, Telefono) VALUES (?, ?, ?)
            """, (NombreJardin, Direccion, Telefono))
            conn.commit()
            print("Jardin creado correctamente")
        else:
            print(f"El jardin {NombreJardin} ya está registrado")
    except sqlite3.Error as error:
        print(error)

def actualizarJardin(Nombre1, Nombre2, Direccion, Telefono):
    cursor.execute("""
    SELECT COUNT(*) FROM Jardin WHERE NombreJardin = ?
    """,(Nombre1,))
    existe = cursor.fetchone()[0]
    if existe == 0:
        print(f"El jardin {Nombre1} no existe en la base de datos")
    else:
        cursor.execute("""
            UPDATE Jardin SET NombreJardin = ?, Direccion = ?, telefono = ? WHERE NombreJardin = ?
        """, (Nombre2, Direccion, Telefono, Nombre1))
        conn.commit()
        print("Datos actualizados correctamente")

def eliminarJardin(Nombre):
    try:
        cursor.execute("""
        SELECT COUNT(*) FROM Jardin WHERE NombreJardin = ?
        """,(Nombre,))
        existe = cursor.fetchone()[0]
        if existe == 0:
            print(f"El jardin {Nombre} no existe en la base de datos")
        else:
            cursor.execute("""
                DELETE FROM Jardin WHERE NombreJardin = ?
            """, (Nombre,))
            conn.commit()
            print(f"El jardin {Nombre} se ha eliminado correctamente")
    except sqlite3.Error as error:
        print("Error al crear el jardín:", error)
        
def estadisticasJardin(Nombre):
    cursor.execute("""
        SELECT COUNT(*) FROM JARDIN WHERE NombreJardin = ?
    """, (Nombre,))
    count_jardin = cursor.fetchone()[0]

    if count_jardin < 1:
        print("El jardin no existe.")
    else:
        # JardinID = resultado[0]
        cursor.execute("""
            SELECT COUNT(*) FROM Alumno WHERE NombreJardin = ?
        """,(Nombre,))
        Nalumnos = cursor.fetchone()[0]

        cursor.execute("""
            SELECT COUNT(*) FROM Personal WHERE NombreJardin = ?
        """,(Nombre,))
        Npersonal = cursor.fetchone()[0]

        print(f"El jardin {Nombre} tiene:")
        print(f"{Nalumnos} alumnos registrados")
        print(f"{Npersonal} trabajadores registrados")

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

read_init_sql(init_sql_file)

sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 5000)
print ('connecting to {} port {}'.format (*server_address))
sock.connect (server_address)
try:
    # Send data
    message = b'00010sinitdatos'
    print ('sending {!r}'.format (message))
    sock.sendall (message)
    while True:
        # Look for the response
        print ("Waiting for transaction BBDD")
        amount_received = 0
        amount_expected = int(sock.recv (5))
        while amount_received < amount_expected:
            data = sock.recv (amount_expected - amount_received)
            amount_received += len (data)
            print('received {!r}'.format(data))
            print ("Processing sql...")
            try:
                data = data.decode().split()
                opcion = data[1]
                if opcion == '1':
                    Rut = data[2]
                    Contrasena = data[2]
                    print('Ingresando...')
                    login(Rut,Contrasena)
                    message = '00015datosloginexito'.encode()
                    print ('sending {!r}'.format (message))
                    sock.send(message)

                elif opcion == '2':
                    Nombre = data[2]
                    Rut = data[3]
                    Correo = data[4]
                    Contrasena = data[5]
                    Telefono = data[6]
                    Rol = data[7]
                    Jardin = data[8]
                    print('Registrando...')
                    registro(Nombre,Rut,Correo,Contrasena,Telefono,Rol,Jardin)
                    message = '00015datosregisexito'.encode()
                    print ('sending {!r}'.format (message))
                    sock.send(message)

                elif opcion == '3':
                    Rut = data[2]
                    Nombre = data[3]
                    Apellido = data[4]
                    FechaNacimiento = data[5]
                    NombreJardin = data[6]
                    CursoID = data[7]

                    print('Registrando Alumno...')
                    registroAlumno(Rut,Nombre,Apellido,FechaNacimiento,NombreJardin,CursoID)
                    message = '00015datosnewalexito'.encode()
                    print ('sending {!r}'.format (message))
                    sock.send(message)

                elif opcion == '4':
                    Rut = data[2]
                    Nombre = data[3]
                    Apellido = data[4]
                    FechaNacimiento = data[5]
                    NombreJardin = data[6]
                    CursoID = data[7]

                    print('Actualizando Alumno...')
                    actualizarAlumno(Rut,Nombre,Apellido,FechaNacimiento,NombreJardin,CursoID)
                    message = '00015datosupdalexito'.encode()
                    print ('sending {!r}'.format (message))
                    sock.send(message)

                elif opcion == '5':
                    Rut = data[2]

                    print('Borrando Alumno...')
                    borrarAlumno( Rut )
                    message = '00015datosdelalexito'.encode()
                    print ('sending {!r}'.format (message))
                    sock.send(message)

                elif opcion == '6':
                    PersonaRut = data[2]
                    Fecha = data[3]
                    Estado = data[4]

                    print('Asistencia Alumno...')
                    controlAsistencia(PersonaRut,Fecha,Estado)
                    message = '00015datosconasexito'.encode()
                    print ('sending {!r}'.format (message))
                    sock.send(message)

                elif opcion == '7':
                    # CREAR JARDIN
                    Nombre = data[2]
                    Direccion = data[3]
                    Telefono = data[4]

                    print('Creacion Jardin...')
                    creacionJardin(Nombre,Direccion,Telefono)
                    message = '00015datosnewjaexito'.encode()
                    print ('sending {!r}'.format (message))
                    sock.send(message)

                elif opcion == '8':
                    # ACTUALIZAR JARDIN
                    Nombre1 = data[2]
                    Nombre2 = data[3]
                    Direccion = data[4]
                    Telefono = data[5]

                    print('Actualizando Jardin...')
                    actualizarJardin(Nombre1,Nombre2,Direccion,Telefono)
                    message = '00015datosupdjaexito'.encode()
                    print ('sending {!r}'.format (message))
                    sock.send(message)        

                elif opcion == '9':
                    # ELIMINAR JARDIN
                    Nombre = data[2]

                    print('Eliminando Jardin...')
                    eliminarJardin(Nombre)
                    message = '00015datosdeljaexito'.encode()
                    print ('sending {!r}'.format (message))
                    sock.send(message)

                elif opcion == '10':
                    # ESTADISTICAS JARDIN
                    Nombre = data[2]

                    print('Obteniendo estadisticas de Jardin...')
                    estadisticasJardin(Nombre)
                    message = '00015datosestjaexito'.encode()
                    print ('sending {!r}'.format (message))
                    sock.send(message)

            except:
                pass
            print('-------------------------------')
            

finally:
    print ('closing socket')
    sock.close ()

conn.commit()
conn.close()
