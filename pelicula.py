# Módulo que define la clase Pelicula (Programación Orientada a Objetos)

class Pelicula:
    def __init__(self, id_pelicula, titulo, genero, anio, director):
        self.id = id_pelicula
        self.titulo = titulo
        self.genero = genero
        self.anio = anio
        self.director = director

    def a_diccionario(self):
        """Convierte el objeto Pelicula a un diccionario para guardarlo en JSON."""
        return {
            "id": self.id,
            "titulo": self.titulo,
            "genero": self.genero,
            "anio": self.anio,
            "director": self.director
        }

    @staticmethod
    def desde_diccionario(datos):
        """Crea un objeto Pelicula a partir de un diccionario del JSON."""
        return Pelicula(
            datos["id"],
            datos["titulo"],
            datos["genero"],
            datos["anio"],
            datos["director"]
        )