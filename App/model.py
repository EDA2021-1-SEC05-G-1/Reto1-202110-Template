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
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
def newCatalog():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'videos': None,
               'categories': None,}
    catalog['videos'] = lt.newList('ARRAY_LIST',cmpfunction=cmpvideosid)
    catalog['categories'] = lt.newList('ARRAY_LIST',
                                    cmpfunction=comparecategories)
 
    return catalog
def cmpvideosid(video1,video2):
    if (video1.lower() in video2['video_id'].lower()):
        return 0
    return -1
def comparecategories(category1,category2):
    if (category1.lower() in category2['category_id'].lower()):
        return 0
    return -1
def cmptags(name,tag):
    return (name==tag['videos'])
def addvideo(catalog,video):
    lt.addLast(catalog['videos'],video)
def addcategory(nuevo_cat,categoria):
    lt.addLast(nuevo_cat["categories"],categoria)
def cmpVideosByViews(video1,video2):
    return (float(video1['views'])> float(video2['views']))
def subList(list, size):
    muestra=lt.subList(list,1,size)
    return {"lista":muestra}
    
def buscacategoria(categoria,catalog):
    i=0
    while i<=lt.size(catalog['categories']):
        tempelement=lt.getElement(catalog['categories'],i)
        if tempelement['name']==str(" "+categoria):
            return int(tempelement['id'])
        i+=1
    return i


def filtrada(catalog,pais,id_categoria,numero_videos):
    tad=lt.newList('ARRAY_LIST')
    lista_n=[]
    i=1
    while i< (lt.size(catalog['videos'])):
        if (pais in (lt.getElement(catalog['videos'],i)['country'])) and (str(id_categoria) in (lt.getElement(catalog['videos'],i)['category_id'])):
            lt.addLast(tad,lt.getElement(catalog['videos'],i))
        i+=1
    a=tad.copy()
    mer.sort(a,cmpVideosByViews)
    b=lt.subList(a,1,numero_videos)
    return b
def emptyList():
    return lt.newList('SINGLE_LINKED')
def getFirstVideo(catalog):
    return lt.firstElement(catalog["videos"])


def getVideosByCountry(catalog, country):
    countryList = mp.get(catalog['videos'], country)
    if countryList:
        return me.getValue(countryList)
    return None


def getTrendingDays(video):
    publishTimeString = video['publish_time'].split("-")
    publishTime = datetime.datetime(int(
        publishTimeString[0]), int(publishTimeString[1]), int(publishTimeString[2][0:2]))
    trendingDateString = video['trending_date'].split(".")
    trendingDate = datetime.datetime(int(
        "20"+trendingDateString[0]), int(trendingDateString[2]), int(trendingDateString[1]))
    return (trendingDate - publishTime).days


def compareViews(video1, video2):
    return (int(video1['views']) > int(video2['views']))


def compareTrendingDays(video1, video2):
    return (getTrendingDays(video1) > getTrendingDays(video2))


def compareLikes(video1, video2):
    return (int(video1['likes']) > int(video2['likes']))


def sortVideosByViews(catalog):
    lst = catalog['videos']
    sa.sort(lst, compareViews)
    return lst


def sortVideosByTrendingDays(catalog):
    lst = catalog['videos']
    sa.sort(lst, compareTrendingDays)
    return lst


def sortVideosByLikes(catalog):
    lst = catalog['videos']
    sa.sort(lst, compareLikes)
    return lst




        
def sortVideos(catalog, listSortType):
    return mer.sort(catalog,cmpVideosByViews)


# Construccion de modelos

# Funciones para agregar informacion al catalogo

# Funciones utilizadas para comparar elementos dentro de una lista
# Funciones de ordenamiento
