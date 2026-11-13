from modelo.libro import Libro
from errores.biblioteca_exception import BibliotecaException


class GestionLibros:

    def __init__(self, libros):
        self.libros = libros

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

    # Funcion para añadir libros
    def anadir_libro(self, registrar_evento):
        print("\n--- AÑADIR LIBRO ---")

        try:
            codigo = int(input("Introduce el codigo del libro: "))

            libro_existente = False

            for libro in self.libros:
                if libro.codigo == codigo:
                    libro_existente = True

            if libro_existente:
                raise BibliotecaException(
                    "Ya existe un libro con ese codigo.", 8
                )
            else:
                titulo = input("Introduce el titulo: ")
                autor = input("Introduce el autor: ")
                anio = int(input("Introduce el año: "))
                categoria = input("Introduce la categoria: ")

                libro = Libro(codigo, titulo, autor, anio, categoria)
                self.libros.append(libro)

                registrar_evento(
                    "ALTA_LIBRO",
                    f"Codigo: {codigo}, Titulo: {titulo}"
                )

                print("Libro añadido correctamente.")

        except BibliotecaException as error:
            print(f"Error: {error}")
            print(f"Codigo de error: {error.codigo_error}")

        except ValueError:
            print("Error: el codigo y el año deben ser numericos.")