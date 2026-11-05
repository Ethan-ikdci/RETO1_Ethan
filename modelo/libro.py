class Libro:
    
    def _init_(self, codigo, titulo, autor, anio, categoria, codigo_socio=None):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.categoria = categoria
        self.codigo_socio = codigo_socio
    
    def esta_disponible(self):
        disponible = False

        if self.codigo_socio is None:
            disponible = True

        return disponible
    
    def mostrar_informacion(self):
        estado = "Disponible"

        if self.codigo_socio is not None:
            estado = "Prestado"

        print(f"Código: {self.codigo}\n")
        print(f"Título: {self.titulo}\n")
        print(f"Autor: {self.autor}\n")
        print(f"Año: {self.anio}\n")
        print(f"Categoría: {self.categoria}\n")
        print(f"Estado: {estado}")
        