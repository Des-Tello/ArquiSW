import socket

def registro(nombre,rut,contrasena,telefono,rol,jardin):
    #LARGO PARA PODER ASIGNARLE EN EL BUS
    largo=len(nombre)+len(rut)+len(contrasena)+len(telefono)+len(rol)+len(jardin)+5+6

    #CREAR EL SOCKET PARA LA CONEXIÓN
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #CONECTARSE AL HOST Y PUERTO
    server_address = ('localhost', 5000)
    sock.connect(server_address)

    try:
        #ENVIAR DATA AL BUS
        message = f'000{largo}regis {nombre} {rut} {contrasena} {telefono} {rol} {jardin}'.encode()
        sock.sendall(message)

        #LOOK FOR THE RESPONSE
        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = sock.recv(4096)
            print(data)
    finally:
        sock.close()