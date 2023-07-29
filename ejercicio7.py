import json

def agregar_contacto():
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    telefono = input("Ingrese el teléfono: ")
    direccion = input("Ingrese la dirección: ")

    contacto = {
        "nombre": nombre,
        "apellido": apellido,
        "teléfono": telefono,
        "dirección": direccion
    }

    with open("contactos.json", "a") as archivo:
        json.dump(contacto, archivo)
        archivo.write('\n')

    print("Contacto agregado exitosamente.")

def ver_informacion():
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")

    with open("contactos.json", "r") as archivo:
        contactos = archivo.readlines()

        for contacto in contactos:
            contacto_dict = json.loads(contacto)
            if contacto_dict["nombre"] == nombre and contacto_dict["apellido"] == apellido:
                print("Información del contacto:")
                print(f"Nombre: {contacto_dict['nombre']}")
                print(f"Apellido: {contacto_dict['apellido']}")
                print(f"Teléfono: {contacto_dict['teléfono']}")
                print(f"Dirección: {contacto_dict['dirección']}")
                return

        print("No se encontró información del contacto.")

def mostrar_menu():
    print("1. Agendar contacto")
    print("2. Ver información de contacto")
    print("3. Salir")

def validar_opcion(opcion):
    return opcion in ['1', '2', '3']

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if validar_opcion(opcion):
            if opcion == '1':
                agregar_contacto()
            elif opcion == '2':
                ver_informacion()
            else:
                print("¡Hasta luego!")
                break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == '__main__':
    main()
