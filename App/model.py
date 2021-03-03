"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import selectionsort as ss
from DISClib.Algorithms.Sorting import insertionsort as si
from DISClib.Algorithms.Sorting import mergesort as mer
from DISClib.Algorithms.Sorting import quicksort as qu
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
def initcatalog(listType):
    return {"videos":lt.newList(listType)}

def subList(list, size):
    muestra=lt.subList(list,0,size)
    return {"lista":muestra}
    
# Construccion de modelos

# Funciones para agregar informacion al catalogo
def addvideo(catalog,video):
    lt.addLast(catalog["videos"],video)
# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpVideosByViews(video1, video2):
    return (int(video1['views']) < int(video2['views']))
# Funciones de ordenamiento
def sortVideos(catalog, listSortType):
    if listSortType==1:
        ss.sort(catalog, cmpVideosByViews)
    elif listSortType==2:
        si.sort(catalog, cmpVideosByViews)
    elif listSortType==3:
        sa.sort(catalog, cmpVideosByViews)
    elif listSortType==4:
        mer.sort(catalog, cmpVideosByViews)
    else:
        qu.sort(catalog, cmpVideosByViews)