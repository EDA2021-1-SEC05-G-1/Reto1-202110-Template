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
    print("1- Cargar información")
    print("2- Encontrar buenos videos por categoría y país")
    print("3- Encontrar video tendencia por país")
    print("4- Encontrar video tendencia por categoría")
    print("5- Buscar los videos con más Likes")
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
        print("Cargando información de los archivos ....")
        catalog=controller.initcatalog()
        controller.cargardatos(catalog)
        controller.cargarcategorias(catalog)
        print("Se cargo la información del catalogo")
        print("Se cargaron "+ str(lt.size(catalog["videos"]))+ " videos.")
        print("Cargando información del primer video cargado...")
        print("La información del primer video cargado es:")
        primer=lt.firstElement(catalog['videos'])
        print('title: ' + primer['title'])
        print('channel_title: '+ primer['channel_title'])
        print('trending_date: '+ primer['trending_date'])
        print('country: '+ primer['country'])
        print('views: '+ primer['views'])
        print('likes: '+ primer['likes'])
        print('dislikes: '+ primer['dislikes'])
        #lt.getElement(catalog['categories'],0)['id']
        for categoria in catalog["categories"]['elements']:
            print(categoria)
        
    elif int(inputs[0]) == 2:
        categoria=str(input("Ingrese la categoria deseada: "))
        pais=str(input("Ingrese el pais deseado: "))
        numero_videos=int(input("Ingrese el número de videos para listar: "))
        lista_n=lt.newList('ARRAY_LIST')
        x=lt.subList(catalog['videos'],1,(lt.size(catalog['videos'])))
        id_categoria=controller.buscarcategoria(categoria,catalog)
        tad=controller.filtrada_controll(catalog,pais,id_categoria,numero_videos)
        for a in range(lt.size(tad)):
            print("Video: "+str(a+1))
            print("trending_date:" +tad['elements'][a]['trending_date'])
            print('title:'+tad['elements'][a]['title'])
            print('channel_title:'+tad['elements'][a]['channel_title'])
            print('publish_time:'+tad['elements'][a]['publish_time'])
            print('views:'+tad['elements'][a]['views'])
            print('likes:'+tad['elements'][a]['likes'])
            print('dislikes:'+tad['elements'][a]['dislikes'])

    elif int(inputs[0]) == 3:
        country = input('Ingrese el pais (country):\n')
        video = controller.getVideoWithMostTrendingDaysByCountry(
            catalog, country)
        print("*"*asteriskNumber)
        print("title: "+video['title'])
        print("channel_title: "+video['channel_title'])
        print("country: "+video['country'])
        print("Días: "+str(controller.getTrendingDays(video)))
    elif int(inputs[0]) == 4:
        category = input('Ingrese la categoria (category_id):\n')
        video = controller.getVideoWithMostTrendingDaysByCategory(
            catalog, category)
        print("*"*asteriskNumber)
        print("title: "+video['title'])
        print("channel_title: "+video['channel_title'])
        print("category_id: "+video['category_id'])
        print("Días: "+str(controller.getTrendingDays(video)))
    elif int(inputs[0]) == 5:
        country = input('Ingrese el pais (country):\n')
        tag = input('Ingrese el tag:\n')
        n = input('Numeros de videos a listar:\n')
        videosTag = controller.getMostLikedVideosByCountryAndTag(
            catalog, country, tag, n)
        for video in lt.iterator(videosTag):
            print("*"*asteriskNumber)
            print("Title: "+video['title'])
            print("channel_title: "+video['channel_title'])
            print("publish_time: "+video['publish_time'])
            print("views: "+video['views'])
            print("likes: "+video['likes'])
            print("dislikes: "+video['dislikes'])
            print("tags: "+video['tags'])
    else:
        sys.exit(0)
sys.exit(0)
