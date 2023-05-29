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
        INSERT INTO Usuarios (Nombre, Rut, Correo, Contrasena, Telefono, Rol, Jardin)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (nombre, rut, correo, contrasena, telefono, rol, jardin))
    conn.commit()
    print("Usuario registrado con éxito.")

def login(rut, contrasena):
    cursor.execute("""
        SELECT COUNT(*) FROM Usuarios WHERE Rut = ? AND Contrasena = ?
    """, (rut, contrasena))
    count = cursor.fetchone()[0]
    if count > 0:
        print("El usuario existe en la tabla.")
    else:
        print("El usuario no existe en la tabla.")

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
                Nombre = data[1]
                Rut = data[2]
                Correo = data[3]
                Contrasena = data[4]
                Telefono = data[5]
                Rol = data[6]
                Jardin = data[7]
                print('Registrando....')
                registro(Nombre,Rut,Correo,Contrasena,Telefono,Rol,Jardin)

                message = '00010datosexito'.encode()
                print ('sending {!r}'.format (message))
                sock.send(message)
            except:
                pass
            

finally:
    print ('closing socket')
    sock.close ()


# registro("Juan Pérez", "123456789", "juan@example.com", "contrasena123", "1234567890", "Administrador", "Mi Jardín")

# login("123456789", "contrasena123")

conn.commit()
conn.close()
