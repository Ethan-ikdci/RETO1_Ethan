from modelo.libro import Libro
from modelo.socio import Socio

def cargar_libros():
    libros = []

    with open("libros.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            datos = linea.strip().split(";")

            codigo = int(datos[0])
            titulo = datos[1]
            autor = datos[2]
            anio = int(datos[3])
            categoria = datos[4]
            codigo_socio = datos[5]

            if codigo_socio == "None":
                codigo_socio = None
            else:
                codigo_socio = int(codigo_socio)

            libro = Libro(
                codigo, titulo, autor, anio,
                categoria, codigo_socio
            )

            libros.append(libro)

    print("Se han cargado los libros correctamente.")

    return libros

def cargar_socios():
    socios = []

    with open("socios.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            datos = linea.strip().split(";")

            codigo_socio = int(datos[0])
            nombre = datos[1]
            email = datos[2]
            codigo_libro = datos[3]

            if codigo_libro == "None":
                codigo_libro = None
            else:
                codigo_libro = int(codigo_libro)

            socio = Socio(
                codigo_socio, nombre, email, codigo_libro
            )

            socios.append(socio)

    return socios

def listar_libros(libros):
    print("\n--- LISTADO DE TODOS LOS LIBROS ---")

    for libro in libros:
        print("------------------------------")
        libro.mostrar_informacion()


def listar_libros_disponibles(libros):
    print("\n--- LIBROS DISPONIBLES ---")

    for libro in libros:
        if libro.esta_disponible():
            print("------------------------------")
            libro.mostrar_informacion()



def buscar_libros(libros):
    titulo_buscar = input("\nIntroduce el título: ").lower()

    encontrados = False

    for libro in libros:
        if titulo_buscar in libro.titulo.lower():
            print("------------------------------")
            libro.mostrar_informacion()
            encontrados = True

    if encontrados == False:
        print("No se han encontrado libros con ese título.")


def mostrar_menu():
    print("\n========== BIBLIOTECA ==========")
    print("1. Listar todos los libros")
    print("2. Listar libros disponibles")
    print("3. Buscar libros por título")
    print("4. Prestar libro a un socio")
    print("5. Devolver libro")
    print("6. Mostrar socios con préstamos")
    print("7. Añadir libros y socios")
    print("8. Guardar y salir")
    print("================================")

libros = cargar_libros()
socios = cargar_socios()

opcion = ""

while opcion != "8":
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        listar_libros(libros)

    elif opcion == "2":
        listar_libros_disponibles(libros)

    elif opcion == "3":
        buscar_libros(libros)