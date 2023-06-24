import sqlite3
import socket
import sys
import logging

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

init_sql_file = "/home/users/rodrigo.ordenes/ArquiSW/db/init.sql"

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
        logging.info("El usuario ya está registrado.")
    else:
        cursor.execute("""
            INSERT INTO Usuarios (Nombre, Rut, Correo, Contrasena, Telefono, Rol, Jardin)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (nombre, rut, correo, contrasena, telefono, rol, jardin))
        conn.commit()
        logging.info("Usuario registrado con éxito.")

def login(rut, contrasena):
    cursor.execute("""
        SELECT COUNT(*) FROM Usuarios WHERE Rut = ? AND Contrasena = ?
    """, (rut, contrasena))
    rows = cursor.fetchall()

    if len(rows) > 0:
        logging.info("Login Exitoso.")

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
        logging.info("El alumno ya está registrado.")
    elif count_jardin < 1:
        logging.info("El jardín no existe.")
    # elif count_curso < 1:
    #     logging.info("El curso no existe en el jardín asociado.")
    else:
        cursor.execute("""
            INSERT INTO ALUMNO (Rut, Nombre, Apellido, FechaNacimiento, NombreJardin, CursoID)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (Rut, Nombre, Apellido, FechaNacimiento, NombreJardin, CursoID))
        conn.commit()
        logging.info("Alumno registrado con éxito.")

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
        logging.info("Alumno no existente.")
    elif count_jardin < 1:
        logging.info("El jardín no existe.")
    # elif count_curso < 1:
    #     logging.info("El curso no existe en el jardín asociado.")
    else:
        cursor.execute("""
            UPDATE ALUMNO 
            SET CursoID = ?, NombreJardin = ?, Nombre = ?, Apellido = ?, FechaNacimiento = ?
            WHERE Rut = ?
        """, (CursoID, NombreJardin, Nombre, Apellido, FechaNacimiento, Rut))
        conn.commit()
        logging.info("Alumno actualizado con éxito.")
        
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
        logging.info("Alumno borrado con éxito.")
    else:
        logging.info("No hay ningun alumno existente.")
        
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
        logging.info("No se ha encontrado ningun rut asociado")
    else:
        cursor.execute("""
            INSERT INTO ASISTENCIA (PersonaRut, Fecha, Estado)
            VALUES (?, ?, ?);
        """, (PersonaRut, Fecha, Estado))
        conn.commit()
        logging.info("Asistencia registrada con éxito.")

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
            logging.info("Jardin creado correctamente")
        else:
            logging.info(f"El jardin {NombreJardin} ya está registrado")
    except sqlite3.Error as error:
        logging.info(error)

def actualizarJardin(Nombre1, Nombre2, Direccion, Telefono):
    cursor.execute("""
    SELECT COUNT(*) FROM Jardin WHERE NombreJardin = ?
    """,(Nombre1,))
    existe = cursor.fetchone()[0]
    if existe == 0:
        logging.info(f"El jardin {Nombre1} no existe en la base de datos")
    else:
        cursor.execute("""
            UPDATE Jardin SET NombreJardin = ?, Direccion = ?, telefono = ? WHERE NombreJardin = ?
        """, (Nombre2, Direccion, Telefono, Nombre1))
        conn.commit()
        logging.info("Datos actualizados correctamente")

def eliminarJardin(Nombre):
    try:
        cursor.execute("""
        SELECT COUNT(*) FROM Jardin WHERE NombreJardin = ?
        """,(Nombre,))
        existe = cursor.fetchone()[0]
        if existe == 0:
            logging.info(f"El jardin {Nombre} no existe en la base de datos")
        else:
            cursor.execute("""
                DELETE FROM Jardin WHERE NombreJardin = ?
            """, (Nombre,))
            conn.commit()
            logging.info(f"El jardin {Nombre} se ha eliminado correctamente")
    except sqlite3.Error as error:
        logging.info("Error al eliminar el jardín:", error)
        
def estadisticasJardin(Nombre):
    cursor.execute("""
        SELECT COUNT(*) FROM JARDIN WHERE NombreJardin = ?
    """, (Nombre,))
    count_jardin = cursor.fetchone()[0]

    if count_jardin < 1:
        logging.info("El jardin no existe.")
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

        logging.info(f"El jardin {Nombre} tiene:")
        logging.info(f"{Nalumnos} alumnos registrados")
        logging.info(f"{Npersonal} trabajadores registrados")

def eliminarUsuario(Rut):
    try:
        cursor.execute("""
            SELECT COUNT(*) FROM Usuarios WHERE Rut = ?
        """, (Rut,))
        count_usuario = cursor.fetchone()[0]

        if count_usuario < 1:
            logging.info("El usuario no existe.")
        else:
            cursor.execute("""
                DELETE FROM Usuarios WHERE Rut = ?
            """, (Rut,))
            conn.commit()
            logging.info(f'El usuario {Rut} se ha eliminado correctamente')
    except sqlite3.Error as error:
        logging.info("Error al eliminar el usuario:", error)

#ActualizarUsuario
def actualizarUsuario(Nombre, Rut, Correo, Contrasena, Telefono, Rol, Jardin):
    ver = True
    try:
        cursor.execute("""
            SELECT COUNT(*) FROM Usuarios WHERE Rut = ?
        """, (Rut,))
        count_usuario = cursor.fetchone()[0]

        #Verificamos Jardin
        cursor.execute("""
            SELECT COUNT(*) FROM Jardin WHERE NombreJardin = ?
        """, (Jardin,))

        count_jardin = cursor.fetchone()[0]

        if count_usuario < 1:
            logging.info("El Rut de usuario no es valido.")
            ver = False
        if count_jardin < 1:
            logging.info("El jardin no existe.")
            ver = False

        if ver == True:
            cursor.execute("""
                UPDATE Usuarios SET Nombre = ?, Correo = ?, Contrasena = ?, Telefono = ?, Rol = ?, Jardin = ? WHERE Rut = ?
            """, (Nombre, Correo, Contrasena, Telefono, Rol, Jardin, Rut))
            conn.commit()
            logging.info("Datos actualizados correctamente")

    except sqlite3.Error as error:
        logging.info("Error al actualizar el usuario:", error)

       
def registrarPersonal(Rut, Jardin, Nombre, Apellido, Cargo, FechaNacimiento):
    val = True
    try:
        #Reviso que exista un persona con ese rut
        cursor.execute("""
            SELECT COUNT(*) FROM Personal WHERE Rut = ?
        """, (Rut,))
        count_personal = cursor.fetchone()[0]
        #Reeviso que existasta el jardin
        cursor.execute("""
            SELECT COUNT(*) FROM Jardin WHERE NombreJardin = ?
        """, (Jardin,))
        count_jardin = cursor.fetchone()[0]

        if count_personal > 0 :
            logging.info("El rut ya se encuentra registrado.")
            val = False
        if count_jardin < 1:
            logging.info("El jardin no existe.")
            val = False
        if val == True:
            cursor.execute("""
                INSERT INTO Personal (Rut, NombreJardin, Nombre, Apellido, Cargo, FechaNacimiento)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (Rut, Jardin, Nombre, Apellido, Cargo, FechaNacimiento))
            conn.commit()
            logging.info("Personal registrado correctamente")

    except sqlite3.Error as error:
        logging.info("Error al registrar el personal:", error)

def comparacionAsistencia(NivelEducativo1,NivelEducativo2,FechaDesde,FechaHasta):
    try:
        #cursor.execute("""
        #        INSERT INTO Curso (CursoID,NombreJardin,PersonalID) VALUES (2, sexo, 1)
        #    """)
        cursor.execute("""
            SELECT CURSO.CursoID, ALUMNO.Nombre, ALUMNO.Apellido, ASISTENCIA.Fecha, ASISTENCIA.Estado FROM ASISTENCIA JOIN ALUMNO ON ASISTENCIA.PersonaRut = ALUMNO.Rut
                    JOIN CURSO ON ALUMNO.CursoID = CURSO.CursoID
                    WHERE CURSO.CursoID IN (?,?) AND ASISTENCIA.Fecha BETWEEN ? AND ?
        """,(NivelEducativo1,NivelEducativo2,FechaDesde,FechaHasta,))
        conn.commit()
        Npersonal = cursor.fetchall()
        logging.info("Comparación de Asistencia a continuación.")
        #Npersonal = cursor.fetchall()
        logging.info(Npersonal)
    except sqlite3.Error as error:
        logging.info("Error al comparar asistencia:", error)

def visualizacionAsistenciaPersonal(PersonalID,Fecha):
    try:
        #cursor.execute("""
        #        INSERT INTO PERSONAL (Rut,NombreJardin,Nombre,Apellido,Cargo,FechaNacimiento) VALUES ('20245835-1','Sandeli','Abel','Baulloza','ProGOD','2000-07-12')
        #    """)

        cursor.execute("""
            SELECT * FROM ASISTENCIA JOIN PERSONAL ON ASISTENCIA.PersonaRut = PERSONAL.Rut
            WHERE PERSONAL.Rut = ? AND ASISTENCIA.Fecha = ?
        """,(PersonalID,Fecha,))
        conn.commit()

        Npersonal = cursor.fetchall()

        #Npersonal = cursor.fetchall()
        logging.info("Visualización Asistencia de Personal a continuación.")
        logging.info(Npersonal)
    except sqlite3.Error as error:
        logging.info("Error al visualizar asistencias de personal:", error)

def asistenciaPorJardin(NombreJardin,FechaDesde,FechaHasta):
    try:
        cursor.execute("""
            SELECT * FROM ASISTENCIA JOIN ALUMNO ON ASISTENCIA.PersonaRut = ALUMNO.Rut
            WHERE ALUMNO.NombreJardin = ? AND ASISTENCIA.Fecha BETWEEN ? AND ?
        """,(NombreJardin,FechaDesde,FechaHasta))
        conn.commit()

        Npersonal = cursor.fetchall()

        #Npersonal = cursor.fetchall()
        logging.info("Asistencia por Jardin a continuación.")
        logging.info(Npersonal)
    except sqlite3.Error as error:
        logging.info("Error al revisar las asistencias por jardín:", error)

conn = sqlite3.connect("/home/users/rodrigo.ordenes/ArquiSW/services/database.db")
cursor = conn.cursor()

read_init_sql(init_sql_file)

sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 5000)
logging.info ('connecting to {} port {}'.format (*server_address))
sock.connect (server_address)
try:
    # Send data
    message = b'00010sinitdatos'
    logging.info ('sending {!r}'.format (message))
    sock.sendall (message)
    while True:
        # Look for the response
        logging.info ("Waiting for transaction BBDD")
        amount_received = 0
        amount_expected = int(sock.recv (5))
        while amount_received < amount_expected:
            data = sock.recv (amount_expected - amount_received)
            amount_received += len (data)
            logging.info('received {!r}'.format(data))
            logging.info ("Processing sql...")
            try:
                data = data.decode().split()
                opcion = data[1]
                if opcion == '1':
                    Rut = data[2]
                    Contrasena = data[2]
                    logging.info('Ingresando...')
                    login(Rut,Contrasena)
                    message = '00015datosloginexito'.encode()
                    logging.info ('sending {!r}'.format (message))
                    sock.send(message)

                elif opcion == '2':
                    Nombre = data[2]
                    Rut = data[3]
                    Correo = data[4]
                    Contrasena = data[5]
                    Telefono = data[6]
                    Rol = data[7]
                    Jardin = data[8]
                    logging.info('Registrando...')
                    registro(Nombre,Rut,Correo,Contrasena,Telefono,Rol,Jardin)
                    message = '00015datosregisexito'.encode()
                    logging.info ('sending {!r}'.format (message))
                    sock.send(message)

                elif opcion == '3':
                    Rut = data[2]
                    Nombre = data[3]
                    Apellido = data[4]
                    FechaNacimiento = data[5]
                    NombreJardin = data[6]
                    CursoID = data[7]

                    logging.info('Registrando Alumno...')
                    registroAlumno(Rut,Nombre,Apellido,FechaNacimiento,NombreJardin,CursoID)
                    message = '00015datosnewalexito'.encode()
                    logging.info ('sending {!r}'.format (message))
                    sock.send(message)

                elif opcion == '4':
                    Rut = data[2]
                    Nombre = data[3]
                    Apellido = data[4]
                    FechaNacimiento = data[5]
                    NombreJardin = data[6]
                    CursoID = data[7]

                    logging.info('Actualizando Alumno...')
                    actualizarAlumno(Rut,Nombre,Apellido,FechaNacimiento,NombreJardin,CursoID)
                    message = '00015datosupdalexito'.encode()
                    logging.info ('sending {!r}'.format (message))
                    sock.send(message)

                elif opcion == '5':
                    Rut = data[2]

                    logging.info('Borrando Alumno...')
                    borrarAlumno( Rut )
                    message = '00015datosdelalexito'.encode()
                    logging.info ('sending {!r}'.format (message))
                    sock.send(message)

                elif opcion == '6':
                    PersonaRut = data[2]
                    Fecha = data[3]
                    Estado = data[4]

                    logging.info('Asistencia Alumno...')
                    controlAsistencia(PersonaRut,Fecha,Estado)
                    message = '00015datosconasexito'.encode()
                    logging.info ('sending {!r}'.format (message))
                    sock.send(message)

                elif opcion == '7':
                    # CREAR JARDIN
                    Nombre = data[2]
                    Direccion = data[3]
                    Telefono = data[4]

                    logging.info('Creacion Jardin...')
                    creacionJardin(Nombre,Direccion,Telefono)
                    message = '00015datosnewjaexito'.encode()
                    logging.info ('sending {!r}'.format (message))
                    sock.send(message)

                elif opcion == '8':
                    # ACTUALIZAR JARDIN
                    Nombre1 = data[2]
                    Nombre2 = data[3]
                    Direccion = data[4]
                    Telefono = data[5]

                    logging.info('Actualizando Jardin...')
                    actualizarJardin(Nombre1,Nombre2,Direccion,Telefono)
                    message = '00015datosupdjaexito'.encode()
                    logging.info ('sending {!r}'.format (message))
                    sock.send(message)        

                elif opcion == '9':
                    # ELIMINAR JARDIN
                    Nombre = data[2]

                    logging.info('Eliminando Jardin...')
                    eliminarJardin(Nombre)
                    message = '00015datosdeljaexito'.encode()
                    logging.info ('sending {!r}'.format (message))
                    sock.send(message)

                elif opcion == '10':
                    # ESTADISTICAS JARDIN
                    Nombre = data[2]

                    logging.info('Obteniendo estadisticas de Jardin...')
                    estadisticasJardin(Nombre)
                    message = '00015datosestjaexito'.encode()
                    logging.info ('sending {!r}'.format (message))
                    sock.send(message)
                
                elif opcion =='11':
                    #ELIMINAR USUARIO
                    Rut = data[2]

                    logging.info('Eliminando Usuario...')
                    eliminarUsuario(Rut)
                    message = '00015datosdelusrexito'.encode()
                    logging.info ('sending {!r}'.format (message))
                    sock.send(message)

                elif opcion =='12':
                    #ACTUALIZAR USUARIO
                    Nombre = data[2]
                    Rut = data[3]
                    Correo = data[4]
                    Contrasena = data[5]
                    Telefono = data[6]
                    Rol = data[7]
                    Jardin = data[8]

                    logging.info('Actualizando Usuario...')
                    actualizarUsuario(Nombre,Rut,Correo,Contrasena,Telefono,Rol,Jardin)
                    message = '00015datosupdusrexito'.encode()
                    logging.info ('sending {!r}'.format (message))
                    sock.send(message)

                elif opcion =='13':
                    #REGISTRAR PERSONAL
                    Rut = data[2]
                    Jardin = data[3]
                    Nombre = data[4]
                    Apellido = data[5]
                    Cargo = data[6]
                    FechaNacimiento = data[7]

                    logging.info('Registrando Personal...')
                    registrarPersonal(Rut,Jardin,Nombre,Apellido,Cargo,FechaNacimiento)
                    message = '00015datosnewpexito'.encode()
                    logging.info ('sending {!r}'.format (message))
                    sock.send(message)

                elif opcion == '14':
                    #   Asistencia por Jardin
                    NombreJardin = data[2]
                    FechaDesde = data[3]
                    FechaHasta = data[4]

                    logging.info('Visualizando asistencias ...')
                    asistenciaPorJardin(NombreJardin,FechaDesde,FechaHasta)
                    message = '00015datosasipeexito'.encode()
                    logging.info ('sending {!r}'.format (message))
                    sock.send(message)

                elif opcion == '15':
                    #   COMPARACIÓN ASISTENCIA
                    NivelEducativo1 = data[2]
                    NivelEducativo2 = data[3]
                    FechaDesde = data[4]
                    FechaHasta = data[5]


                    logging.info('Comparando asistencias ...')
                    comparacionAsistencia(NivelEducativo1,NivelEducativo2,FechaDesde,FechaHasta)
                    message = '00015datoscomasexito'.encode()
                    logging.info ('sending {!r}'.format (message))
                    sock.send(message)

                elif opcion == '16':
                    #   Visualizacion ASISTENCIA por personal
                    PersonalID = data[2]
                    Fecha = data[3]

                    logging.info('Visualizando asistencias ...')
                    visualizacionAsistenciaPersonal(PersonalID,Fecha)
                    message = '00015datosasipeexito'.encode()
                    logging.info ('sending {!r}'.format (message))
                    sock.send(message)

                

            except:
                pass
            logging.info('-------------------------------')
            

finally:
    logging.info ('closing socket')
    sock.close ()

conn.commit()
conn.close()
