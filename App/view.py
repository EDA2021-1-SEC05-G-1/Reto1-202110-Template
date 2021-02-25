"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """
import time
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Ordenar videos por vistas")
    print("3- Encontrar video tendencia por país")
    print("4- Video tendencia por categoria")
    print("5- Videos por más likes")
    print("6- Salir")
catalog = None
muestra = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        listTypeOption=input("Seleccione el tipo de representación de la lista:\n 1-ARRAY_LIST \n 2-LINKED_LIST(por defecto)\n")
        print("Cargando información de los archivos ....")
        if int(listTypeOption[0])==1:
            catalog=controller.initcatalog("ARRAY_LIST")
        else:
            catalog=controller.initcatalog("LINKED_LIST")
        controller.cargardatos(catalog)
        print("Se cargo la información del catalogo")
        print("Se cargaron "+ str(lt.size(catalog["videos"]))+ " videos.")
    elif int(inputs[0]) == 2:
        subListSize = int(input("Ingrese el tamaño de la muestra\n"))
        if int(subListSize)>lt.size(catalog["videos"]):
            print("El tamaño de la muestra no puede superar el tamaño de la lista")
        else:
            muestra = controller.subList(catalog["videos"],subListSize)
            print("El tamaño de la lista de muestra es igual a", lt.size(muestra["lista"]))
        listSortType = int(input("Seleccione el tipo de algoritmo de ordenamiento iterativo:\n1-selection\n2-insertion\n3-shell(por defecto)\n"))
        t1=time.process_time()
        print("Se ejecuto requerimiento 1")
        controller.sortVideos(muestra["lista"],listSortType)
        t2=time.process_time()
        print("Tiempo de {:0.6f} ejecución".format(t2-t1))

    elif int(inputs[0]) == 3:
        t1=time.process_time()
        print("Se ejecuto requerimiento 2")
        t2=time.process_time()
        print("Tiempo de {:0.6f} ejecución".format(t2-t1))

    elif int(inputs[0]) == 4:
        t1=time.process_time()
        print("Se ejecuto requerimiento 3")
        t2=time.process_time()
        print("Tiempo de {:0.6f} ejecución".format(t2-t1))

    elif int(inputs[0]) == 5:
        t1=time.process_time()
        print("Se ejecuto requerimiento 4")
        t2=time.process_time()
        print("Tiempo de {:0.6f} ejecución".format(t2-t1))
    
    else:
        sys.exit(0)
sys.exit(0)
