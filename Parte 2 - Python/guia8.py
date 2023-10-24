# Guia 8: Archivos, Pilas, Colas y Diccionarios
from queue import Queue
from queue import LifoQueue as Pila
import random


# 1: ARCHIVOS

# -----------
# Ejercicio 1 OK
# -----------

# Ejercicio 1. Implementar en Python:
# 1.1 Una funcion contar lineas(in nombre archivo : str) → int 
# que cuenta y devuelva la cantidad de l´ıneas de texto del archivo dado
def contar_lineas (nombre_archivo: str) -> int:
    archivo = open(nombre_archivo, "r", encoding='utf8')
    lineas: list[str] = archivo.readlines()
    archivo.close()
    return len(lineas)


# print(contar_lineas("ejemplomapi.txt"))

# 1.2 Una funcion existe palabra(in palabra : str, in nombre archivo : str) → bool 
# que dice si una palabra existe en un archivo de texto o no
def existe_palabra (palabra: str, nombre_archivo: str) -> bool:
    archivo = open(nombre_archivo, "r", encoding='utf8')

    # Itera sobre cada linea del archivo (que es un string con varias palabras)
    for linea in archivo.readlines():
        # Separar las palabras de este string y ver si el param "palabra" coincide con alguna
        if palabra in linea.split():
            return True
        
    archivo.close()

    return False

# print(existe_palabra("linea", "ejemplomapi.txt")) # False
# print(existe_palabra("lineas", "ejemplomapi.txt")) # True


# 1.3 Una funcion cantidad apariciones(in nombre archivo : str, in palabra : str) → int 
# que devuelve la cantidad de apariciones de una palabra en un archivo de texto
def contar_apariciones (nombre_archivo: str, palabra: str) -> int:
    archivo = open(nombre_archivo)
    cantidad_apariciones: int = 0

    # Contar la cantidad de veces que "palabra" aparece en cada linea, y sumarla a la cantidad total de apariciones 
    for linea in archivo.readlines():
        cantidad_apariciones += linea.split().count(palabra)
    
    return cantidad_apariciones

# print(contar_apariciones("ejemplomapi.txt", "lineas"))


# -----------
# Ejercicio 2 TO-DO
# -----------

# Dado un archivo de texto con comentarios, implementar una funcion clonar sin comentarios(in nombre archivo : str)
# que toma un archivo de entrada y genera un nuevo archivo que tiene el contenido original sin las lıneas comentadas. 
# Para este ejercicio vamos a considerar comentarios como aquellas l´ıneas que tienen un caracter ‘#’como primer caracter de la l´ınea, o si
# no es el primer caracter, se cumple que todos los anteriores son espacios.
# Ejemplo:
# # esto es un comentario
# # esto tambien
# esto no es un comentario # esto tampoco

# def clonar_sin_comentarios(nombre_archivo : str) -> None:


# -----------
# Ejercicio 3 OK
# -----------
# Dado un archivo de texto, implementar una funcion que escribe un archivo nuevo llamado reverso.txt que tiene
# las mismas lıneas que el original, pero en el orden inverso.
# Ejemplo: si el archivo original es:
# Esta es la primera linea .
# Y esta es la segunda .
# debe generar:
# Y esta es la segunda .
# Esta es la primera linea 

def revertir_archivo(nombre_archivo: str) -> None:
    archivo = open(nombre_archivo)
    archivo_revertido_nombre = "reverso.txt"

    destino = open(archivo_revertido_nombre, "w", encoding='utf8') # Abre archivo nuevo
    destino.truncate() #Borra todo el contenido de un archivo

    lineas = archivo.readlines() 
    last_item = lineas[-1] + "\n" # Agregarle caracter nueva linea a la ultima linea

    archivo_revertido_contenido = []
    for i in range(len(lineas)):
        if i != len(lineas) - 1:
            archivo_revertido_contenido.insert(0,lineas[i]) # Agregar la linea original si no es la ultima
        else:
            archivo_revertido_contenido.insert(0,last_item)  # Si es la ultima linea, agregar la linea modificada


    for linea in archivo.readlines():
        archivo_revertido_contenido.insert(0,linea)
    
    for linea in archivo_revertido_contenido:
        destino.write(linea) 
    

# revertir_archivo("ejemplomapi.txt")


# 2: PILAS (8 al 12) (falta 9, 11, 12)

# -----------
# Ejercicio 8 OK
# -----------

# Implementar una funcion generar nros al azar(in n : int, in desde : int, in hasta : int) → pila 
# que genere una pila de n numeros enteros al azar en el rango [desde, hasta]. 
# Pueden user la funcion random.randint(< desde >, < hasta >) 
# y la clase LifoQueue() que es un ejemplo de una implementacion basica:
# from queue import LifoQueue as Pila
# p = Pila ()
# p . put (1) # apilar
# elemento = p . get () # desapilar
# p . empty () # vacia ?

def generar_nums_azar(n: int, desde: int, hasta: int) -> Pila:
    p = Pila()
    for i in range(n):
        p.put(random.randint(desde, hasta))
    p.put(50)
    # print(p.queue)
    return p


generar_nums_azar(5, 10, 11)

# ------------
# Ejercicio 10 OK
# ------------
# Dada una pila de enteros, implementar una funcion buscar el maximo(in p : pila) → int 
# que devuelva el maximo elemento.

# Esto esta bien, pero no respeta que el parametro sea solo in (lo esta modificando y esto no tiene que pasar)
def buscar_el_maximo(p:Pila) -> int:
    p.put(1)
    p.put(150)
    p.put(2)
    p.put(3)
    # print(p.queue) # IMPRIMIR TODA LA PILA
    maximo: int = p.get()
    while not p.empty():
        actual: int = p.get()
        if actual > maximo:
            maximo = actual 
    
    return maximo


def buscar_el_maximo_respetando_in(p:Pila) -> int:
    p.put(1)
    p.put(150)
    p.put(2)
    p.put(3)
    # print(p.queue) # IMPRIMIR TODA LA PILA
    maximo: int = p.get()
    aux: Pila = Pila()
    aux.put(maximo)

    while not p.empty():
        actual: int = p.get()
        aux.put(actual)
        if actual > maximo:
            maximo = actual 

    # Volver a armar la pila original
    while not aux.empty():
        actual = aux.get()
        p.put(actual)

    # print(p.queue)
    # print(p.get())
    
    return maximo



cola = Pila()
# print(buscar_el_maximo_respetando_in(cola))


# 3: COLAS (13 al 18) (falta 13 - 18)


# 4: DICCIONARIOS (19 al 23) (falta 20 - 23)
# ------------
# Ejercicio 19 OK
# ------------
# Para esta seccion vamos a usar el tipo dict que nos provee python
# Leer un archivo de texto y agrupar la cantidad de palabras de acuerdo a su longitud. 
# Implementar la funcion agrupar por longitud(in nombre archivo : str) → dict que devuelve un diccionario {longitud en letras : cantidad de palabras}
# Ej el diccionario
# {
# 1: 2 ,
# 2: 10 ,
# 5: 4
# }
# indica que se encontraron 2 palabras de longitud 1, 10 palabras de longitud 2 y 5 palabras de longitud 4. 
# Para este ejercicio vamos a considerar palabras a todas aquellas secuencias de caracteres que no tengan espacios en blanco.
def agrupar_por_longitud(nombre_archivo:str) -> dict:
    archivo = open(nombre_archivo)
    lineas = archivo.readlines()

    dict_longitudes = dict()

    for linea in lineas:
        # print("linea", linea)
        # print("linea spliteada", linea.split())
        palabras = linea.split()
        for palabra in palabras:
            # print(word)
            largo = len(palabra)
            if largo not in dict_longitudes.keys():
                # if d.get(largo) is None:
                dict_longitudes[largo] = 1
            else:
                dict_longitudes[largo] += 1
    

    # FORMA DE CLASE
    lista_gigante_de_palabras = []
    for linea in lineas: 
        lista_gigante_de_palabras.append(linea.split(" "))

    return dict_longitudes


            

# print(agrupar_por_longitud("ejemplomapi.txt"))








