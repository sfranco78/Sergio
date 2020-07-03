lista = []
salida = "No"

def agregarContacto():
    nuevo_contacto = {}
    nuevo_contacto['nombre'] = input("Ingresa el nombre del contacto:")
    nuevo_contacto['correo'] = input("Ingresa el correo del contacto")
    nuevo_contacto['dirección'] = input("Ingresa la dirección del contacto")
    lista.append(nuevo_contacto)


while(salida == "No"):
    entrada = input("Escribe la acción a efecturar")
    if entrada == "Nuevo ":
         agregarContacto()
         print("Contacto agregado ")
    elif entrada == "show ":
        print(lista[:])
    elif entrada == "Salir" :
        exit()
    else:
        print("Opcion inválida ")