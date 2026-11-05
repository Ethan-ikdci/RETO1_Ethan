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

libros = cargar_libros()
socios = cargar_socios()

print(f"Total de libros: {len(libros)}")
print(f"Total de socios: {len(socios)}")