# Guia 8: Archivos, Pilas, Colas y Diccionarios
from queue import Queue
from queue import LifoQueue as Pila
import random


# 1: ARCHIVOS (1 al 7)
# Que aprendi?
"""
-1.2) linea.split(): divide una cadena en una lista de elementos utilizando espacios en blanco como separador por defecto
ej.: linea = "123,Matemáticas,2023-10-25,90.5" -> ['123,Matemáticas,2023-10-25,90.5']

-2) linea.lstrip(): método de cadenas que elimina espacios en blanco y otros caracteres especificados al principio (izquierda) de una cadena.
También puedes pasar un argumento a lstrip() para especificar los caracteres que deseas eliminar. 
Por ejemplo:
linea = "****¡Hola, mundo!"
nueva_linea = linea.lstrip("*!") -> print(nueva_linea) -> "Hola, mundo!"

-3) 
-with open(nombre_archivo) as archivo:
        lineas = archivo.readlines()
El uso de with asegura que los archivos se cierren adecuadamente después de su uso. 
Esto es importante para evitar posibles problemas de manejo de recursos y pérdida de datos.
Y ademas esta asignandolo a la variable "archivo", y luego leyendo sus lineas.
KEY: se trabaja dentro del bloque with; cuando se sale de este, el archivo se cierra

-lineas.reverse() -> Revertir el orden de las líneas

-if not linea.endswith('\n'): #chequear si la linea termina con un string en particular
    linea += '\n' #agregar este caracter
archivo_revertido.write(linea) 


-4)
-with open(nombre_archivo, "a") as archivo:
    archivo.write(frase)
-> abrir el archivo en formato "append" (a): se escribiran lineas al final del archivo


-5)
with open(nombre_archivo, "r+") as archivo:
    contenido_original = archivo.read()
    archivo.seek(0)
    archivo.write(frase + contenido_original)
r+: Open for reading and writing. The stream is positioned at the beginning of the file.
archivo.read(): Leer el contenido original del archivo, luego lo almacenamos variable contenido_original.
archivo.seek(0): Mover el puntero al principio del archivo
archivo.write(frase + contenido_original): Escribir al archivo primero la frase y luego el contenido_original


-6)
with open(nombre_archivo, "rb") as f:
    contenido = f.read()
    for secuencia in contenido:
        char = chr(secuencia)
rb: read mode + binary mode
Al hacer read() vamos a obtener una secuencia de bytes, que al hacer chr(byte) {aca chr(secuencia)} 
nos va a devolver un caracter correspondiente al byte leido.

"""


# -----------
# Ejercicio 1 OK 23/10
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

# print(existe_palabra("qe", "guia8texto.txt")) # False
# print(existe_palabra("tal", "guia8texto.txt")) # True


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
# Ejercicio 2 OK 24/10
# -----------

# Dado un archivo de texto con comentarios, implementar una funcion clonar sin comentarios(in nombre archivo : str)
# que toma un archivo de entrada y genera un nuevo archivo que tiene el contenido original sin las lıneas comentadas. 
# Para este ejercicio vamos a considerar comentarios como aquellas lıneas que tienen un caracter ‘#’como primer caracter de la lınea, o si
# no es el primer caracter, se cumple que todos los anteriores son espacios.
# Ejemplo:
# # esto es un comentario
# # esto tambien
# esto no es un comentario # esto tampoco

def clonar_sin_comentarios(nombre_archivo : str) -> None:
    archivo = open(nombre_archivo)

    lineas: list[str] = archivo.readlines()
    archivo_clonado: list[str] = []

    def es_comentario(linea: str) -> bool:
        return linea.lstrip()[0] == '#'

    for linea in lineas:
        if not es_comentario(linea):
            archivo_clonado.append(linea)
    
    return archivo_clonado

# print(clonar_sin_comentarios("guia8texto.txt"))



# -----------
# Ejercicio 3 OK 23/10, corregido 24/10
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



def revertir_archivo_corregido(nombre_archivo: str) -> None:
    """
    Esta implementacion es mejor por las siguientes razones:
    -Utiliza un administrador de contexto (with): El uso de with asegura que los archivos se cierren adecuadamente después de su uso. 
    Esto es importante para evitar posibles problemas de manejo de recursos y pérdida de datos.

    -Simplifica el proceso: En lugar de manipular índices y crear una lista separada para las líneas revertidas, 
    simplemente usamos el método reverse() para invertir la lista de líneas original. 
    Esto hace que el código sea más claro y menos propenso a errores.

    -Manejo adecuado del carácter de nueva línea: Mi implementación verifica si cada línea original tiene un carácter de nueva línea al final y, 
    si no lo tiene, lo agrega antes de escribir la línea en el archivo "reverso.txt". 
    Esto evita que la primera línea del archivo resultante se pegue a la segunda línea.
    """
    with open(nombre_archivo) as archivo:
        lineas = archivo.readlines()

    # Revertir el orden de las líneas
    lineas.reverse()

    archivo_revertido_nombre = "reverso.txt"
    with open(archivo_revertido_nombre, "w") as archivo_revertido:
        for linea in lineas:
            if not linea.endswith('\n'):
                linea += '\n'
            archivo_revertido.write(linea)    

# revertir_archivo("guia8texto.txt")
# revertir_archivo_corregido("guia8texto.txt")


# -----------
# Ejercicio 4 OK 24/10
# -----------

# Dado un archivo de texto y una frase, 
# implementar una funcion que la agregue al final del archivo original (sin hacer una copia)

def agregar_frase(nombre_archivo: str, frase: str) -> None:
    with open(nombre_archivo, "a") as archivo:
        archivo.write(frase)
    
# agregar_frase("guia8texto.txt", "\nyo se que estas ahi")


# -----------
# Ejercicio 5 OK 24/10 (solucion buscada en GPT)
# -----------
# Idem, pero agregando la frase al comienzo del archivo original (de nuevo, sin hacer una copia del archivo).
def agregar_frase_al_comienzo(nombre_archivo: str, frase: str) -> None:
    """
    Esta función abre el archivo especificado en modo lectura/escritura ("r+"), 
    lee el contenido original del archivo, y agrega la frase proporcionada al principio del archivo. 
    El archivo original se modifica directamente.

    Funcionamiento:
    r+: Open for reading and writing. The stream is positioned at the beginning of the file.
    archivo.read(): Leer el contenido original del archivo, luego lo almacenamos variable contenido_original.
    archivo.seek(0): Mover el puntero al principio del archivo
    """
    with open(nombre_archivo, "r+") as archivo:
        contenido_original = archivo.read()
        archivo.seek(0)  # Mover el puntero al principio del archivo
        archivo.write(frase + contenido_original)

# agregar_frase_al_comienzo("guia8texto.txt", "quiero conocerte cambiarias un poquito de mi suerte\n")


# -----------
# Ejercicio 6 OK 24/10 - interesante
# -----------

# Implementar una funcion que lea un archivo en modo binario y devuelva la lista de palabras legibles, 
# donde vamos a definir una palabra legible como:
# secuencias de texto formadas por numeros, letras mayusculas/minusculas y los caracteres ‘ ’(espacio) y ‘_’(guion bajo)
# que tienen longitud >= 5
# Una vez implementada la funci´on, probarla con diferentes archivos binarios (.exe, .zip, .wav, .mp3, etc).
# Referencia: https://docs.python.org/es/3/library/functions.html#open
# Para resolver este ejercicio se puede abrir un archivo en modo binario ‘b’. Al hacer read() vamos a obtener
# una secuencia de bytes, que al hacer chr(byte) nos va a devolver un caracter correspondiente al byte leıdo.

def palabras_legibles(nombre_archivo: str) -> list[str]:

    def es_caracter_legible(char: str) -> bool:
        return char.isalnum() or char == ' ' or char == '_'
    
    palabra: str = ""
    palabras_legibles: list[str] = []

    with open(nombre_archivo, "rb") as f:
        contenido = f.read()
        for secuencia in contenido:
            char = chr(secuencia)
            if es_caracter_legible(char):
                palabra += char
            else:
                if len(palabra) >= 5: 
                    palabras_legibles.append(palabra)
                palabra = ""
    
    return palabras_legibles


# print(palabras_legibles("guia8texto.txt"))
# print(palabras_legibles("t10.pdf"))
# print(palabras_legibles("t10.zip"))
# print(palabras_legibles("gheist.mp3"))


# -----------
# Ejercicio 7 OK 24/10 interesante
# -----------
# Implementar una funcion que lea un archivo de texto separado por comas (comma-separated values, o .csv) 
# que contiene las notas de toda la carrera de un grupo de alumnos y calcule el promedio final de un alumno dado. 
# La funcion es promedioEstudiante(in lu : str) → float. 
# El archivo tiene el siguiente formato:
# nro de LU ( str ) , materia ( str ) , fecha ( str ) , nota ( float )
def promedio_estudiante(num_libreta : str) -> float:

    def extraer_notas(lineas: list[str]) -> list[float]:
        notas: list[int] = []
        for linea in lineas:
            palabras: list[str] = linea.split()
            libreta_en_archivo: str = palabras[0].replace(",", "")
            if num_libreta == libreta_en_archivo:
                nota = palabras[-1]
                notas.append(float(nota))
        return notas

    def promediar(notas: list[float]) -> float:
        return round(sum(notas) / len(notas), 2)

    archivo_notas_alumnos = "notas.csv"
    with open(archivo_notas_alumnos) as libreta:
        # Leer contenido
        contenido = libreta.readlines()
        notas = extraer_notas(contenido)
        return promediar(notas)


# print(promedio_estudiante("869/12")) # 7.38
# print(promedio_estudiante("869/13")) # 7.5
# print(promedio_estudiante("868/12")) # 9.0

# 2: PILAS (8 al 12) (falta 9, 11, 12)

# -----------
# Ejercicio 8 OK 23/10
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


# generar_nums_azar(5, 10, 11)


# ------------
# Ejercicio 9 OK
# ------------
# Implementar una funcion cantidad elementos(in p : pila) → int 
# que, dada una pila, cuente y devuelva la can tidad de elementos que contiene. 
# No se puede utilizar la funicion LifoQueue.qsize(). 
# Si se usa get() para recorrer la pila, esto modifica el parametro de entrada. 
# Y como la especificacion dice que es de tipo in hay que restaurarla.





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








