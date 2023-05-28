import socket
import sqlite3

#CONECTAR A LA DB (SI NO EXISTE, SE CREA).
conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            nombre TEXT,
            rut TEXT,
            contraseña INTEGER,
            telefono INTEGER,
            rol TEXT,
            jardin
        )
    ''')

cursor = conn.cursor()
postgreSQL_select_Query = f"select * from usuarios"
cursor.execute(postgreSQL_select_Query)
mobile_records = cursor.fetchall()
print(mobile_records)

#CREAR SOCKET PARA AL CONEXIÓN
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#CONECTARSE AL HOST Y PUERTO ESPECÍFICO
server_address = ('localhost', 5000)
print('starting up on {} port {}'.format(*server_address))
sock.connect(server_address)

#INICIALIZACIÓN DEL SERVICIO REGISTRO
message = b'00010sinitregis'
print('sending {!r}'.format(message))
sock.send(message)

#CICLO PARA ESPERAR RESPUESTAS
while True:
    recibido=sock.recv(4096) #RESPUESTA QUE RECIBE
    if recibido:
        print('hola',recibido.decode().split(' '))
        if len(recibido.decode().split(' '))==7:
            nombre=recibido.decode().split(' ')[1]
            rut=recibido.decode().split(' ')[2]
            contrasena=recibido.decode().split(' ')[3]
            telefono=recibido.decode().split(' ')[4]
            rol=recibido.decode().split(' ')[5]
            jardin=recibido.decode().split(' ')[6]
            cursor = conn.cursor()
            postgreSQL_select_Query = f"select * from usuarios where rut ='{rut}'"
            cursor.execute(postgreSQL_select_Query)
            mobile_records = cursor.fetchall()
            print(mobile_records)
            if len(mobile_records)>0:
                    sock.send(b'00026regis Rut ya registrado en al base de datos')
            else:
                try:
                    postgreSQL_select_Query = f"insert into usuarios (nombre,rut,contraseña,telefono,rol, jardin) VALUES ('{nombre}','{rut}','{contrasena}','{telefono}','{rol}','{jardin}')"
                    cursor.execute(postgreSQL_select_Query)
                    commit=conn.commit()
                    print(commit)
                    sock.send(b'00022regis Usuario registrado de forma exitoso')
                except:
                    print("Error")
