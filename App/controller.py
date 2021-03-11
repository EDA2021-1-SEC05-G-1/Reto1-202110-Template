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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""
def initcatalog():
    catalogo=model.newCatalog()
    return catalogo
def cargardatos(catalog):
    videofile=cf.data_dir+'videos-large.csv'
    input_file=csv.DictReader(open(videofile,encoding="utf-8"))
    for video in input_file:
        model.addvideo(catalog,video)
def cargarcategorias(catalog):
    categoriasfile=cf.data_dir+'category-id.csv'
    input_file=csv.DictReader(open(categoriasfile,encoding="utf-8"), delimiter='\t')
    for categoria in input_file:
        model.addcategory(catalog,categoria)
def buscarcategoria(categoria,catalog):
    return model.buscacategoria(categoria,catalog)
def filtrada_controll(catalogo,pais,id_categoria,numero_videos):
    return model.filtrada(catalogo,pais,id_categoria,numero_videos)
def sortVideos(catalog, size):
    return model.sortVideos(catalog, size)
def subList(list, size):
    return model.subList(list,size)
def sortVideos(catalog, listSortType):
    return model.sortVideos(catalog, listSortType)
def getFirstVideo(catalog):
    return model.getFirstVideo(catalog)


def getMostViewedVideosByCountryAndCategory(catalog, country, categoryId, n):
    lst = model.sortVideosByViews(catalog)
    emptyLst = model.emptyList()
    count = 0
    for video in lt.iterator(lst):
        if(count < int(n)):
            if(video['country'] == country and video['category_id'] == categoryId):
                lt.addLast(emptyLst, video)
                count += 1
    return emptyLst


def getVideoWithMostTrendingDaysByCountry(catalog, country):
    lst = model.sortVideosByTrendingDays(catalog)
    for video in lt.iterator(lst):
        if(video['country'] == country):
            return video


def getVideoWithMostTrendingDaysByCategory(catalog, categoryId):
    lst = model.sortVideosByTrendingDays(catalog)
    for video in lt.iterator(lst):
        if(video['category_id'] == categoryId):
            return video


def getTrendingDays(video):
    return model.getTrendingDays(video)


def getMostLikedVideosByCountryAndTag(catalog, country, tag, n):
    lst = model.sortVideosByLikes(catalog)
    emptyLst = model.emptyList()
    count = 0
    for video in lt.iterator(lst):
        if(count < int(n)):
            if(video['country'] == country):
                hasTag = False
                for tagItem in video['tags'].split('|'):
                    finalTag = tagItem.replace('"', "")
                    if(finalTag == tag):
                        hasTag = True
                if(hasTag):
                    lt.addLast(emptyLst, video)
                    count += 1
    return emptyLst

# Inicialización del Catálogo de libros

# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
