class Socio:

    def __init__(self, codigo_socio, nombre, email, codigo_libro=None):
        self.codigo_socio= codigo_socio
        self.nombre= nombre
        self.email = email
        self.codigo_libro = codigo_libro
        
    def tiene_libro(self):
        prestamo = False

        if self.codigo_libro is not None:
            prestamo= True
        
        return prestamo
    
    def mostrar_informacion(self):
        
        libro_prestado = "Ninguno"

        if self.codigo_libro is not None:
            libro_prestado = self.codigo_libro

        print(f"Código de socio: {self.codigo_socio}\n")
        print(f"Nombre: {self.nombre}\n")
        print(f"Email: {self.email}\n")
        print(f"Libro prestado: {libro_prestado}")