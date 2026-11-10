
from modelo.libro import Libro
from modelo.socio import Socio


class GestionBiblioteca:

    def __init__(self):
        self.libros = self.cargar_libros()
        self.socios = self.cargar_socios()

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

    # Funcion para listar todos los libros
    def listar_libros(self):
        print("\n--- LISTADO DE TODOS LOS LIBROS ---")

        for libro in self.libros:
            print("------------------------------")
            libro.mostrar_informacion()

    # Funcion para listar los libros disponibles
    def listar_libros_disponibles(self):
        print("\n--- LIBROS DISPONIBLES ---")

        for libro in self.libros:
            if libro.esta_disponible():
                print("------------------------------")
                libro.mostrar_informacion()

    # Funcion para buscar libros por titulo
    def buscar_libros(self):
        titulo_buscar = input(
            "\nIntroduce el titulo: "
        ).lower()

        encontrados = False

        for libro in self.libros:
            if titulo_buscar in libro.titulo.lower():
                print("------------------------------")
                libro.mostrar_informacion()
                encontrados = True

        if encontrados == False:
            print("No se han encontrado libros con ese titulo.")

    # Funcion para hacer el prestamo del libro
    def prestar_libro(self):
        print("\n--- PRESTAR LIBRO ---")

        codigo_libro = int(
            input("Introduce el codigo del libro: ")
        )

        libro_encontrado = None

        for libro in self.libros:
            if libro.codigo == codigo_libro:
                libro_encontrado = libro

        # Comprobamos si el libro existe
        if libro_encontrado is None:
            print("No existe ningun libro con ese codigo.")

        # Comprobamos si el libro ya esta prestado
        elif not libro_encontrado.esta_disponible():
            print("El libro ya esta prestado.")

        else:
            codigo_socio = int(
                input("Introduce el codigo del socio: ")
            )

            socio_encontrado = None

            for socio in self.socios:
                if socio.codigo_socio == codigo_socio:
                    socio_encontrado = socio

            # Comprobamos si el socio existe
            if socio_encontrado is None:
                print("No existe ningun socio con ese codigo.")

            # Comprobamos si el socio ya tiene un libro
            elif socio_encontrado.tiene_libro():
                print("Este socio ya tiene un libro prestado.")

            else:
                # Asociamos el libro con el socio
                libro_encontrado.codigo_socio = codigo_socio
                socio_encontrado.codigo_libro = codigo_libro

                print("Prestamo realizado correctamente.")

        # Funcion para devolver un libro
    def devolver_libro(self):
        print("\n--- DEVOLVER LIBRO ---")

        codigo_socio = int(
            input("Introduce el codigo del socio: ")
        )

        socio_encontrado = None

        # Buscamos al socio
        for socio in self.socios:
            if socio.codigo_socio == codigo_socio:
                socio_encontrado = socio

        # Comprobamos si el socio existe
        if socio_encontrado is None:
            print("No existe ningun socio con ese codigo.")

        # Comprobamos si tiene un libro prestado
        elif not socio_encontrado.tiene_libro():
            print("Este socio no tiene ningun libro prestado.")

        else:
            codigo_libro = socio_encontrado.codigo_libro
            libro_encontrado = None

            # Buscamos el libro prestado
            for libro in self.libros:
                if libro.codigo == codigo_libro:
                    libro_encontrado = libro

            if libro_encontrado is None:
                print("No se encuentra el libro asociado al socio.")

            else:
                # Liberamos el libro y al socio
                libro_encontrado.codigo_socio = None
                socio_encontrado.codigo_libro = None

                print("Libro devuelto correctamente.")

    # Funcion para mostrar los socios que tienen libros prestados
    def mostrar_socios_con_prestamos(self):
        print("\n--- SOCIOS CON LIBROS PRESTADOS ---")

        encontrados = False

        for socio in self.socios:
            if socio.tiene_libro():
                print("------------------------------")
                socio.mostrar_informacion()

                for libro in self.libros:
                    if libro.codigo == socio.codigo_libro:
                        print("Informacion del libro:")
                        libro.mostrar_informacion()

                encontrados = True

        if encontrados == False:
            print("No hay socios con libros prestados.")
