from Dominio.Pelicula import Pelicula
import os


class CatalogoPeliculas:

    @classmethod
    def Agregar_Peliculas(cls, pelicula):
        try:
            archivo = open('Peliculas.txt', 'a')
            archivo.write(pelicula._nombre + '\n')
        except Exception as e:
            print(e)
        finally:
            archivo.close()

    @classmethod
    def Listar_Peliculas(cls):
        try:
            archivo = open('Peliculas.txt', 'r')
            print(archivo.read())
        except Exception as e:
            print(e)
        finally:
            archivo.close()
    @classmethod
    def Eliminar_Catalogo(cls):
        try:
            os.remove("Peliculas.txt")
        except Exception as e:
            print(e)