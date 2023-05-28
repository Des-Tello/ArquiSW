from registro_cliente import registro

def main():
    print('Que hacer? \n Opción 1.- Registro')
    opcion = input()
    if opcion == '1':
        nombre = input("Nombre de Usuario: ")
        rut = input('Rut: ')
        contrasena = input('Contraseña: ')
        telefono = input('Telefono: ')
        rol = input('Rol: ')
        jardin = input('Jardin: ')

        registro(nombre,rut,contrasena,telefono,rol,jardin)
        
main()