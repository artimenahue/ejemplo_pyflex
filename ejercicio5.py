import os

def crear_tabla(numero):
    contenido = ""
    for i in range(1, 11):
        resultado = numero * i
        contenido += f"{numero} x {i} = {resultado}\n"
    
    nombre_archivo = f"tabla-{numero}.txt"
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(contenido)
    
    print(f"Tabla de multiplicar {numero} generada y guardada en el archivo {nombre_archivo}.")

def mostrar_tabla(numero):
    nombre_archivo = f"tabla-{numero}.txt"
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            print(f"Tabla de multiplicar {numero}:\n{contenido}")
    except FileNotFoundError:
        print(f"No se encontró el archivo {nombre_archivo}.")
        

def mostrar_menu():
    print("1. Generar tabla de multiplicar")
    print("2. Mostrar tabla de multiplicar")
    print("3. Salir")

def validar_opcion(opcion):
    return opcion in ['1', '2', '3']

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if validar_opcion(opcion):
            if opcion == '1':
                numero = int(input("Ingrese un número entero: "))
                crear_tabla(numero)
            elif opcion == '2':
                numero = int(input("Ingrese un número entero: "))
                mostrar_tabla(numero)
            else:
                print("¡Hasta luego!")
                break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == '__main__':
    main()
