from modelo.socio import Socio
from errores.biblioteca_exception import BibliotecaException


class GestionSocios:

    def __init__(self, socios, libros):
        self.socios = socios
        self.libros = libros

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


    def anadir_socio(self, registrar_evento):
        print("\n--- AÑADIR SOCIO ---")

        try:
            codigo_socio = int(
                input("Introduce el codigo del socio: ")
            )

            socio_existente = False

            for socio in self.socios:
                if socio.codigo_socio == codigo_socio:
                    socio_existente = True

            if socio_existente:
                raise BibliotecaException(
                    "Ya existe un socio con ese codigo.", 9
                )
            else:
                nombre = input("Introduce el nombre: ")
                email = input("Introduce el email: ")

                socio = Socio(codigo_socio, nombre, email)
                self.socios.append(socio)

                registrar_evento(
                    "ALTA_SOCIO",
                    f"Codigo: {codigo_socio}, Nombre: {nombre}"
                )

                print("Socio añadido correctamente.")

        except BibliotecaException as error:
            print(f"Error: {error}")
            print(f"Codigo de error: {error.codigo_error}")

        except ValueError:
            print("Error: debes introducir un codigo numerico.")

