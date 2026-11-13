
from gestion_libros import GestionLibros
from gestion_socios import GestionSocios
from modelo.libro import Libro
from modelo.socio import Socio

from datetime import datetime

from errores.biblioteca_exception import BibliotecaException


class GestionBiblioteca:
        
    def __init__(self):
        self.libros = self.cargar_libros()
        self.socios = self.cargar_socios()

        self.gestion_libros = GestionLibros(self.libros)
        self.gestion_socios = GestionSocios(self.socios, self.libros)
        
        print(f"Se han cargado {len(self.libros)} libros.")
        print(f"Se han cargado {len(self.socios)} socios.")


    # Funcion para cargar los libros del txt
    def cargar_libros(self):
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

        return libros

    # Funcion para cargar los socios del txt
    def cargar_socios(self):
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
   
    # Funcion para hacer el prestamo del libro
    def prestar_libro(self):
        print("\n--- PRESTAR LIBRO ---")

        try:
            codigo_libro = int(input("Introduce el codigo del libro: "))
            codigo_socio = int(input("Introduce el codigo del socio: "))

            libro_encontrado = None
            socio_encontrado = None

            for libro in self.libros:
                if libro.codigo == codigo_libro:
                    libro_encontrado = libro

            for socio in self.socios:
                if socio.codigo_socio == codigo_socio:
                    socio_encontrado = socio

            if libro_encontrado is None:
                raise BibliotecaException(
                    "No existe ningun libro con ese codigo.", 1
                )

            if socio_encontrado is None:
                raise BibliotecaException(
                    "No existe ningun socio con ese codigo.", 2
                )

            if not libro_encontrado.esta_disponible():
                raise BibliotecaException(
                    "El libro ya esta prestado.", 3
                )   

            if socio_encontrado.tiene_libro():
                raise BibliotecaException(
                    "El socio ya tiene un libro prestado.", 4
                )

            libro_encontrado.codigo_socio = codigo_socio
            socio_encontrado.codigo_libro = codigo_libro

            self.registrar_evento(
                "PRESTAMO",
                f"Libro: {codigo_libro}, Socio: {codigo_socio}"
            )

            print("Prestamo realizado correctamente.")

        except BibliotecaException as error:
            print(f"Error: {error}")
            print(f"Codigo de error: {error.codigo_error}")

        except ValueError:
            print("Error: debes introducir codigos numericos.")
        
    def devolver_libro(self):
        print("\n--- DEVOLVER LIBRO ---")

        try:
            codigo_socio = int(
                input("Introduce el codigo del socio: ")
            )

            socio_encontrado = None

            for socio in self.socios:
                if socio.codigo_socio == codigo_socio:
                    socio_encontrado = socio

            if socio_encontrado is None:
                raise BibliotecaException(
                    "No existe ningun socio con ese codigo.", 5
                )
            elif not socio_encontrado.tiene_libro():
                raise BibliotecaException(
                    "Este socio no tiene ningun libro prestado.", 6
                )
            else:
                codigo_libro = socio_encontrado.codigo_libro
                libro_encontrado = None

                for libro in self.libros:
                    if libro.codigo == codigo_libro:
                        libro_encontrado = libro

                if libro_encontrado is None:
                    raise BibliotecaException(
                        "No se encuentra el libro asociado al socio.", 7
                    )
                else:
                    libro_encontrado.codigo_socio = None
                    socio_encontrado.codigo_libro = None

                    self.registrar_evento(
                        "DEVOLUCION",
                        f"Libro: {codigo_libro}, Socio: {codigo_socio}"
                    )

                    print("Libro devuelto correctamente.")

        except BibliotecaException as error:
            print(f"Error: {error}")
            print(f"Codigo de error: {error.codigo_error}")

        except ValueError:
            print("Error: debes introducir un codigo numerico.")

    # Funcion para gestionar las altas
    def anadir_datos(self):
        opcion = ""

        while opcion != "3":
            print("\n--- AÑADIR DATOS ---")
            print("1. Añadir libro")
            print("2. Añadir socio")
            print("3. Volver al menu principal")

            opcion = input("Selecciona una opcion: ")

            if opcion == "1":
                self.gestion_libros.anadir_libro(self.registrar_evento)
            elif opcion == "2":
                self.gestion_socios.anadir_socio(self.registrar_evento)
            elif opcion == "3":
                print("Volviendo al menu principal.")
            else:
                print("Opcion no valida.")

    # Funcion para guardar los libros en el txt
    def guardar_libros(self):
        with open("libros.txt", "w", encoding="utf-8") as archivo:
            for libro in self.libros:
                codigo_socio = libro.codigo_socio

                if codigo_socio is None:
                    codigo_socio = "None"

                linea = (
                    f"{libro.codigo};{libro.titulo};{libro.autor};"
                    f"{libro.anio};{libro.categoria};{codigo_socio}\n"
                )

                archivo.write(linea)

    # Funcion para guardar los socios en el txt
    def guardar_socios(self):
        with open("socios.txt", "w", encoding="utf-8") as archivo:
            for socio in self.socios:
                codigo_libro = socio.codigo_libro

                if codigo_libro is None:
                    codigo_libro = "None"

                linea = (
                    f"{socio.codigo_socio};{socio.nombre};"
                    f"{socio.email};{codigo_libro}\n"
                )

                archivo.write(linea)

    # Funcion para guardar todos los datos
    def guardar_datos(self):
        self.guardar_libros()
        self.guardar_socios()

        self.registrar_evento(
            "GUARDADO",
            "Libros y socios guardados correctamente"
        )

        print("Datos guardados correctamente.")

    # Funcion para registrar eventos en el log
    def registrar_evento(self, nombre_evento, detalles):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("log.txt", "a", encoding="utf-8") as archivo:
            archivo.write(
                f"[{fecha}][{nombre_evento}][{detalles}]\n"
            )
