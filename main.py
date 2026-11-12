from gestion_biblioteca import GestionBiblioteca

biblioteca = GestionBiblioteca()

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

opcion = ""

while opcion != "8":
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        biblioteca.gestion_libros.listar_libros()

    elif opcion == "2":
        biblioteca.gestion_libros.listar_libros_disponibles()

    elif opcion == "3":
        biblioteca.gestion_libros.buscar_libros()

    elif opcion == "4":
        biblioteca.prestar_libro()

    elif opcion == "5":
        biblioteca.devolver_libro()

    elif opcion == "6":
        biblioteca.gestion_socios.mostrar_socios_con_prestamos()
        
    elif opcion == "7":
        biblioteca.anadir_datos()

    elif opcion == "8":
        biblioteca.guardar_datos()
        print("Saliendo del programa...")
    else:
        print("Opcion no valida.")