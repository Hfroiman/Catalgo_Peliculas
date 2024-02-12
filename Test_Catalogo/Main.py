from Dominio.Pelicula import Pelicula
from Servicio.Catalo_Pelicula import CatalogoPeliculas as cp


opcion = -1
while opcion !=4:
    print("Opciones")
    print("1- Agregar pelicula.")
    print("2- Listar peliculas")
    print("3- Eliminar catalogo.")
    print("4- Salir")
    opcion=int (input("Ingresar opcion: "))
    if opcion == 1:
        peli = Pelicula(input("Ingresar pelicula: "))
        cp.Agregar_Peliculas(peli)
    else:
        if opcion == 2:
            cp.Listar_Peliculas()
        else:
            if opcion == 3:
                cp.Eliminar_Catalogo()
            else:
                break;