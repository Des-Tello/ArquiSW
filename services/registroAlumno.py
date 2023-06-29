import socket
import sys
import logging

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

def respuesta_registro_alumno():
    time.sleep(2)
    data = sock.recv(4096).decode()
    if 'exito' in data:
        return 1
    elif 'alumnoexistente' in data:
        return 2
    elif 'jardinnoexistente' in data:
        return 3
    else:
        return 4

# Create a TCP/IP socket
sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
server_address = ('localhost', 5000)
logging.info ('connecting to {} port {}'.format (*server_address))
sock.connect (server_address)
try:
    # Send data
    message = b'00010sinitnewal'
    logging.info ('sending {!r}'.format (message))
    sock.sendall (message)
    while True:
        # Look for the response
        logging.info ("Waiting for register transaction")
        amount_received = 0
        amount_expected = int(sock.recv(5))
        while amount_received < amount_expected:
            data = sock.recv (amount_expected - amount_received)
            amount_received += len (data)
            logging.info('received {!r}'.format(data))
            logging.info ("Registrando Alumno...")
            data = data.decode().split()
            try:
                opcion = data[1]
                Rut = data[2]
                Nombre = data[3]
                Apellido = data[4]
                FechaNacimiento = data[5]
                NombreJardin = data[6]
                CursoID = data[7]
                
                largo = len(Rut+Nombre+Apellido+FechaNacimiento+NombreJardin+CursoID+opcion) + 13
                message = '000{}datos {} {} {} {} {} {} {}'.format(largo,opcion,Rut,Nombre,Apellido,FechaNacimiento,NombreJardin,CursoID).encode()
                logging.info ('sending to bbdd {!r}'.format (message))
                sock.sendall(message)

                result = respuesta_registro_alumno()
                if result == 1:
                    message = '00010newalexito'.encode()
                else:
                    message = '00012newalfallido'.encode()

                logging.info ('sending {!r}'.format (message))
                    sock.send(message)
                    
            except:
                pass
            logging.info('-------------------------------')

finally:
    logging.info ('closing socket')
    sock.close ()