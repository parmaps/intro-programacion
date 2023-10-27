# Guia 8: Archivos, Pilas, Colas y Diccionarios
from queue import LifoQueue as Pila
from queue import Queue as Cola
import random


# Que aprendi?
"""
ARCHIVOS
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

"""
PILAS

11) CLAVE PARA PENSAR CON PILAS (registro de parentesis para chequeo de formula balanceada)

12) 
-pila.qsize(): tamaño aproximado para pilas 
-//: operacion de division entera

"""

"""
COLAS: terminados 26/10, pendiente agregar al 26/10
"""

# 1: ARCHIVOS (1 al 7)
# -----------
# Ejercicio 1 OK 23/10
# -----------


# Ejercicio 1. Implementar en Python:
# 1.1 Una funcion contar lineas(in nombre archivo : str) → int
# que cuenta y devuelva la cantidad de l´ıneas de texto del archivo dado
def contar_lineas(nombre_archivo: str) -> int:
    archivo = open(nombre_archivo, "r", encoding="utf8")
    lineas: list[str] = archivo.readlines()
    archivo.close()
    return len(lineas)


# print(contar_lineas("ejemplomapi.txt"))


# 1.2 Una funcion existe palabra(in palabra : str, in nombre archivo : str) → bool
# que dice si una palabra existe en un archivo de texto o no
def existe_palabra(palabra: str, nombre_archivo: str) -> bool:
    archivo = open(nombre_archivo, "r", encoding="utf8")

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
def contar_apariciones(nombre_archivo: str, palabra: str) -> int:
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


def clonar_sin_comentarios(nombre_archivo: str) -> None:
    archivo = open(nombre_archivo)

    lineas: list[str] = archivo.readlines()
    archivo_clonado: list[str] = []

    def es_comentario(linea: str) -> bool:
        return linea.lstrip()[0] == "#"

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

    destino = open(archivo_revertido_nombre, "w", encoding="utf8")  # Abre archivo nuevo
    destino.truncate()  # Borra todo el contenido de un archivo

    lineas = archivo.readlines()
    last_item = lineas[-1] + "\n"  # Agregarle caracter nueva linea a la ultima linea

    archivo_revertido_contenido = []
    for i in range(len(lineas)):
        if i != len(lineas) - 1:
            archivo_revertido_contenido.insert(
                0, lineas[i]
            )  # Agregar la linea original si no es la ultima
        else:
            archivo_revertido_contenido.insert(
                0, last_item
            )  # Si es la ultima linea, agregar la linea modificada

    for linea in archivo.readlines():
        archivo_revertido_contenido.insert(0, linea)

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
            if not linea.endswith("\n"):
                linea += "\n"
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
        return char.isalnum() or char == " " or char == "_"

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
def promedio_estudiante(num_libreta: str) -> float:
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

# 2: PILAS (8 al 12) OK 25/10

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
    # p.put(50)
    # print(p.queue)
    return p


# generar_nums_azar(5, 10, 11)


# ------------
# Ejercicio 9 OK 24/10 - interesante
# ------------
# Implementar una funcion cantidad elementos(in p : pila) → int
# que, dada una pila, cuente y devuelva la can tidad de elementos que contiene.
# No se puede utilizar la funicion LifoQueue.qsize().
# Si se usa get() para recorrer la pila, esto modifica el parametro de entrada.
# Y como la especificacion dice que es de tipo in hay que restaurarla.
def cantidad_elementos(p: Pila) -> int:
    total_elems = 0
    pila_aux = Pila()

    p.put(1)
    p.put(2)
    p.put(4)
    p.put(8)
    print(p.queue)

    while not p.empty():
        elem = p.get()
        pila_aux.put(elem)
        total_elems += 1

    while not pila_aux.empty():
        elem = pila_aux.get()
        p.put(elem)

    print(p.queue)
    return total_elems


pila9 = Pila()
# print(cantidad_elementos(pila9))


# ------------
# Ejercicio 10 OK 23/10
# ------------
# Dada una pila de enteros, implementar una funcion buscar el maximo(in p : pila) → int
# que devuelva el maximo elemento.


# Esto esta bien, pero no respeta que el parametro sea solo in (lo esta modificando y esto no tiene que pasar)
def buscar_el_maximo(p: Pila) -> int:
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


def buscar_el_maximo_respetando_in(p: Pila) -> int:
    p.put(1)
    p.put(150)
    p.put(2)
    p.put(3)
    print(p.queue)  # IMPRIMIR TODA LA PILA
    maximo: int = p.get()
    aux: Pila = Pila()
    aux.put(maximo)

    while not p.empty():
        actual: int = p.get()
        # print(actual)
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


pila10 = Pila()
# print(buscar_el_maximo_respetando_in(pila10))

# ------------
# Ejercicio 11 OK 25/10 CLAVE PARA ENTENDER PILAS
# ------------


# Implementar una funci´on esta bien balanceada(in s : str) → bool
# que dado un string con una formula aritmetica sobre los enteros,
# diga si los parentesis estan bien balanceados. Las formulas pueden formarse con:
# los numeros enteros
# las operaciones basicas +, −, x y /
# parentesis
# espacios
def esta_bien_balanceada_mal(s: str) -> bool:
    p = Pila()
    # s_reverse = s[::-1]
    for char in s:
        p.put(char)
    print(p.queue, "\n")

    def es_operacion(char: str) -> bool:
        return char == "+" or char == "-" or char == "*" or char == "/"

    def es_parentesis(char: str) -> bool:
        return char == "(" or char == ")"

    def es_caracter_valido(char: str) -> bool:
        return (
            es_operacion(char)
            or es_parentesis(char)
            or char.isnumeric()
            or char.isspace()
        )

    flag_parentesis_abre = False

    # def abre_parentesis_mal(char:str, flag: bool) -> bool:
    #     if not flag and char == "(":
    #         return False
    #     elif char == ")":
    #         flag = True

    parentesis_izq = 0
    parentesis_der = 0

    while not p.empty():
        elem = p.get()
        print(elem)
        if es_caracter_valido(elem):
            print("elem es valido\n")
            print("flag:", flag_parentesis_abre)

            if (
                not flag_parentesis_abre and elem == "("
            ):  # Chequea si aparece un parentesis que abre antes en la pila (contando desde atras!)
                return False
            elif elem == ")":
                flag_parentesis_abre = True

        else:
            print("elem no es valido\n")
            return False

    # print(parentesis_der, parentesis_izq)

    #     if char.isalpha():
    #         print("char es alfa", char)
    #         return False


def esta_bien_balanceada(s: str) -> bool:
    """
    Idea: utilizar la pila para registrar los parentesis y determinar si su aparicion es correcta
    Va a estar balanceada si:
        -no aparece primero un parentensis de cierre
        -tienen la misma cantidad de parentesis de apertura que de cierre
    ->
    a) Cuando aparece "(", apilarlo
    b) Cuando aparece ")", chequear si la pila esta vacia
        -si esta vacia, esta antes que uno de apertura -> formula no balanceada
        -si no esta vacia, desapilar el de apertura (estos se balancean)
    c) Al final este proceso chequear si la pila esta vacia
        -si esta vacia, todos los parentesis se balancearon
        -si no, la formula esta desbalanceada

    """
    pila: Pila = Pila()

    for char in s:
        if char == "(":
            pila.put(char)  # apilo parentesis de apertura
        elif char == ")":
            if (
                pila.empty()
            ):  # si aparece primero el parentesis de cierre -> formula no balanceada (False)
                return False
            pila.get()  # desapilo parentesis de apertura

    return pila.empty()


# print(esta_bien_balanceada("1 + (2*3)")) # True
# print(esta_bien_balanceada("1 + ( 2 x 3 = ( 2 0 / 5 ) )")) # True
# print(esta_bien_balanceada("10 * ( 1 + ( 2 * ( =1)))")) # True
# print(esta_bien_balanceada("1 + ) 2 x 3 ( ()")) # False
# print(esta_bien_balanceada("1 + ()) 2 x 3 ( ()")) # False
# print(esta_bien_balanceada("1 + ( 2 x 3 ( ()))"))  # True

# ------------
# Ejercicio 12 OK 25/10
# ------------
"""
La notacion polaca inversa, tambien conocida como notacion postfix, 
es una forma de escribir expresiones matematicas en la que los operadores siguen a sus operandos. 
Por ejemplo, la expresion “3 + 4” se escribe como “3 4 +” en notacion postfix. 
Para evaluar una expresion en notacion postfix, se puede usar una pila.

Escribi una funcion en Python que tome una expresion en notacion postfix y la evalue. 
La expresion estara representada como una cadena de caracteres, 
donde los operandos y operadores estaran separados por espacios. 
Para simplificar el problema, solo vamos a considerar los operandos 
‘+’, ‘-’, ‘*’ y ‘/’(suma, resta, multiplicacion y division), los operadores son numeros.

Para resolver este problema, se recomienda seguir el siguiente algoritmo:
1. Dividir la expresion en tokens (operandos y operadores) utilizando espacios como delimitadores.
2. Recorre los tokens uno por uno.
a) Si es un operando, agregalo a una pila.
b) Si es un operador, saca los dos operandos superiores de la pila, 
aplicale el operador y luego coloca el resultado en la
pila.
3. Al final de la evaluacion, la pila contendra el resultado de la expresion.

Ejemplo de uso:
expresion = "3 4 + 5 * 2 -"
resultado = evaluar_expresion(expresion)
print(resultado) # Deberia devolver 33
"""


def evaluar_expresion_postfix(expresion: str) -> int:
    pila: Pila = Pila()

    # Diferenciar operandos y operadores
    def es_operacion(char: str) -> bool:
        return char == "+" or char == "-" or char == "*" or char == "/"

    def aplicar_operacion(char: str, num1: int, num2: int) -> int:
        print("aplicando operacion:", char, "en numeros", num1, num2)
        if char == "+":
            return int(num1) + int(num2)
        elif char == "-":
            return int(num1) - int(num2)
        elif char == "*":
            return int(num1) * int(num2)
        elif char == "/":
            return int(num1) // int(num2)

    # Dividir expresion en tokens (chars)
    for char in expresion:
        # Si es un operando, agregalo a una pila
        if char.isnumeric():
            # print("es operando:", char)
            pila.put(char)
        # Si es un operador
        elif es_operacion(char):
            # print("es operador", char)
            # print("tamanio pila:", pila.qsize(), "; pila:", pila.queue, "\n")

            # sacar los dos operandos superiores de la pila
            operando2: int = pila.get(char)
            operando1: int = pila.get(char)

            # aplicarles el operador y colocar el resultado en la pila
            resultado = aplicar_operacion(char, operando1, operando2)
            print(resultado, "\n")
            pila.put(resultado)

    return pila.get()


# print(evaluar_expresion_postfix("3 4 + 5 * 2 -")) # 33
# print(evaluar_expresion_postfix("3 4 + 2 * 7 /")) # 2
# print(evaluar_expresion_postfix("5 1 2 + 4 * + 3 -")) # 14


# 3: COLAS (13 al 18) OK 26/10

# ------------
# Ejercicio 13 OK 25/10
# ------------
# Usando la funcion generar nros al azar() definida en la seccion anterior,
# implementar una funcion que arme una cola de enteros con los numeros generados al azar.
# Pueden usar la clase Queue() que es un ejemplo de una implementacion basica:
# c = Cola ()
# c . put (1) # encolar
# elemento = c . get () # desencolar ()
# c . empty () # vacia ?


def generar_nros_al_azar_cola(n: int, desde: int, hasta: int) -> Cola:
    pila_nros_azar = generar_nums_azar(n, desde, hasta)
    print(pila_nros_azar.queue)

    cola = Cola()

    while not pila_nros_azar.empty():
        num = pila_nros_azar.get()
        cola.put(num)

    print(cola.queue)
    return cola


# generar_nros_al_azar_cola(5, 1,10)


# ------------
# Ejercicio 14 OK 25/10
# ------------


# Implementar una funcion cantidad elementos(in c : cola) → int
# que, dada una cola, cuente y devuelva la cantidad de elementos que contiene.
# Comparar con la version usando pila. No se puede utilizar la funcion Queue.qsize()
def cantidad_elementos_cola(cola: Cola) -> int:
    total_elems: int = 0
    cola_aux: Cola = Cola()

    print(cola.queue)

    while not cola.empty():
        elem = cola.get()
        print(elem)
        total_elems += 1
        cola_aux.put(elem)

    while not cola_aux.empty():
        elem = cola_aux.get()
        cola.put(elem)

    print("cola aux:", cola_aux.queue)
    print(cola.queue)

    return total_elems


cola14 = Cola()
cola14.put(1)
cola14.put(2)
cola14.put(3)
cola14.put(4)
cola14.put(5)
# print(cantidad_elementos_cola(cola14))


# ------------
# Ejercicio 15 OK 25/10
# ------------
# Dada una cola de enteros, implementar una funcion buscar el maximo(in c : cola) → int
# que devuelva el maximo elemento. Comparar con la version usando pila.
def buscar_maximo_cola(cola: Cola) -> int:
    print("cola original:", cola.queue)

    # Definir el primer numero como el maximo
    maximo: int = cola.get()

    # Crear cola auxiliar y agregar el primer numero
    cola_aux: Cola = Cola()
    cola_aux.put(maximo)

    # Mientras cola tenga elementos, sacar el primero, compararlo con el maximo y redefinir el maximo si corresponde
    while not cola.empty():
        actual: int = cola.get()
        cola_aux.put(actual)
        if maximo < actual:
            maximo = actual

    # Restaurar la cola original
    while not cola_aux.empty():
        elem: int = cola_aux.get()
        cola.put(elem)

    print("cola original:", cola.queue)

    return maximo


# Crear y llenar la cola
cola15 = Cola()
cola15.put(20)
cola15.put(10)
cola15.put(2)
cola15.put(101)
# print(buscar_maximo_cola(cola15))


# ------------
# Ejercicio 16 OK 26/10
# ------------
# Bingo: un carton de bingo contiene 12 numeros al azar en el rango [0, 99]

# 16.1)
# Implementar una funcion armar secuencia de bingo() → Cola[int]
# que genere una cola con los numeros del 0 al 99 ordenados al azar.


def armar_secuencia_de_bingo() -> Cola:
    """
    Esta función devuelve una cola que contiene números enteros para un juego de bingo.
    """
    cola = Cola()
    # numeros = [x for x in range(99)]
    numeros = [x for x in range(100)]
    random.shuffle(numeros)  # ordenar aleatoriamente la lista de numeros
    for numero in numeros:
        cola.put(numero)

    return cola


# print(armar_secuencia_de_bingo().queue)

# 16.2)
# Implementar una funcion jugar carton de bingo(in carton : list[int], in bolillero : cola[int]) → int
# que toma un carton de Bingo y una cola de enteros (que corresponden a las bolillas numeradas)
# y determina cual es la cantidad de jugadas de ese bolillero que se necesitan para ganar.


def jugar_carton_de_bingo(carton: list[int], bolillero: Cola) -> int:
    """
    Esta funcion toma un carton de bingo y una cola de enteros (que corresponden a las bolillas numeradas) y determina cual es la cantidad de jugadas de ese bolillero que se necesitan para ganar.

    Args:
    carton: list[int]
    bolillero: Cola[int]

    Retorna:
    cantidad_de_jugadas: int
    """

    cantidad_de_jugadas = 0
    print("carton de bingo:", carton)
    print("bolillero:", bolillero.queue)

    # Variables para evitar modificar los parametros in
    carton_copy = carton.copy()
    bolillero_copy = Cola()

    # Contar cantidad de jugadas y mientras ir copiando el bolillero
    while len(carton_copy) > 0:  # Itero por el bolillero y saco un numero
        numero_bolillero: int = bolillero.get()
        bolillero_copy.put(numero_bolillero)
        cantidad_de_jugadas += 1
        for numero in carton_copy:
            if numero == numero_bolillero:
                carton_copy.remove(numero)
                break
        # print("carton_copy", carton)

    # Si quedaron numeros en el bolillero original, extraerlos y enviarlos a la copia
    while not bolillero.empty():
        numero_bolillero = bolillero.get()
        bolillero_copy.put(numero_bolillero)

    # Restaurar el bolillero original
    while not bolillero_copy.empty():
        numero_bolillero = bolillero_copy.get()
        bolillero.put(numero_bolillero)

    print("carton al final:", carton, "\n")
    print("bolillero al final:", bolillero.queue, "\n")
    print("bolillero copy al final:", bolillero_copy.queue, "\n")

    return cantidad_de_jugadas


# Generar lista de 12 numeros aleatorios entre 0 inclusive y 100 no inclusive
# Con este metodo pueden repetirse
carton_bingo_repetidos: list[int] = [random.randint(0, 100) for _ in range(12)]

# Con este metodo no se repiten, usando un while loop
carton_bingo_no_repetidos_while: list[int] = []
while len(carton_bingo_no_repetidos_while) < 12:
    numero = random.randint(0, 100)
    if numero not in carton_bingo_no_repetidos_while:
        carton_bingo_no_repetidos_while.append(numero)

# Carton manual para testeo
carton_bingo_manual: list[int] = [0, 1, 2]

# jugar_carton_de_bingo(carton_bingo_manual, armar_secuencia_de_bingo()) # version manual
# print("cantidad de jugadas para ganar:", jugar_carton_de_bingo(carton_bingo_no_repetidos_while, armar_secuencia_de_bingo())) # version random


# ------------
# Ejercicio 17 OK 26/10
# ------------
"""
Vamos a modelar una guardia de un hospital usando una cola donde se van almacenando 
los pedidos de atención para los pacientes que van llegando. A cada paciente 
se le asigna una prioridad del 1 al 10 (donde la prioridad 1 es la mas urgente
y requiere atención inmediata) junto con su nombre y la especialidad medica que le corresponde.
Implementar la función n_pacientes_urgentes(in c : Cola[(int, str, str)]) → int 
que devuelve la cantidad de pacientes de la cola que tienen prioridad en el rango [1, 3].
"""


def n_pacientes_urgentes(cola: Cola) -> int:
    """
    Args: Cola[(int, str, str)] = Cola[(prioridad, nombre, especialidad)]
    Return: int = cantidad de pacientes de la cola que tienen prioridad en el rango [1, 3]
    """
    cantidad_de_pacientes_urgentes: int = 0
    # print("\ncola inicial:", cola.queue)
    cola_aux = Cola()

    while not cola.empty():
        paciente: (int, str, str) = cola.get()
        cola_aux.put(paciente)
        prioridad_actual: int = paciente[0]
        if prioridad_actual <= 3:
            cantidad_de_pacientes_urgentes += 1

    while not cola_aux.empty():
        paciente: (int, str, str) = cola_aux.get()
        cola.put(paciente)

    # print("\ncola final:", cola.queue)

    return cantidad_de_pacientes_urgentes


cola17 = Cola()
paciente_1 = (1, "Juen", "Cardiologia")
cola17.put(paciente_1)
cola17.put((2, "Ramiro", "Otorrino"))
cola17.put((3, "Tomas", "Traumatologia"))
cola17.put((4, "Peluca", "Insomnio"))
cola17.put((5, "Mapi", "Ansiedad"))
cola17.put((6, "Roman", "Traumatologia"))
cola17.put((7, "Curry", "Traumatologia"))
# print(cola17.queue)

# print("cantidad de pacientes urgentes:", n_pacientes_urgentes(cola17))

# ------------
# Ejercicio 18 OK 26/10
# ------------

"""
La gerencia de un banco nos pide modelar la atención de los clientes usando una cola 
donde se van registrando los pedidos de atención. Cada vez que ingresa una persona a la entidad, 
debe completar sus datos en una pantalla que está a la entrada: Nombre y Apellido, DNI, tipo de cuenta 
(si es preferencial o no) y si tiene prioridad por ser adulto +65, embarazada o con movilidad reducida (prioridad si o no).
La atención a los clientes se da por el siguiente orden: primero las personas que tienen prioridad, 
luego las que tienen cuenta bancaria preferencial y por último el resto. 
Dentro de cada subgrupo de clientes, se respeta el orden de llegada.
1. Dar una especificación para el problema planteado.
2. Implementar en Python la función 
a_clientes(in c : Cola[(str, int, bool, bool)]) → Cola[(str, int, bool, bool)] 
que dada la cola de ingreso de clientes al banco devuelve la cola en la que van a ser atendidos.
"""

def orden_atencion(cola: Cola) -> Cola:
    """
    Args:
    Cola de ingreso de clientes al banco
    -> Cola[(str, int, bool, bool)] = Cola[(nombre_y_apellido, DNI, es_preferencial, es_prioritario)]


    Return:
    Cola en el el orden en que van a ser atendidos.
    -> Cola[(str, int, bool, bool)] = Cola[(nombre_y_apellido, DNI, es_preferencial, es_prioritario)]
    """
    print("\ncola original:", cola.queue)
    cola_aux: Cola = Cola()
    cola_ordenada: Cola = Cola()
    cola_no_prioritarios: Cola = Cola()
    cola_resto_clientes: Cola = Cola()

    # Pasar clientes a la cola auxiliar, para poder restaurar la cola original
    while not cola.empty():
        cliente = cola.get()
        cola_aux.put(cliente)

    # Encolar clientes prioritarios
    while not cola_aux.empty():
        cliente = cola_aux.get()
        cola.put(cliente) #  Restaurar cola original
        es_prioritario = cliente[3]
        if es_prioritario:
            cola_ordenada.put(cliente)
        else:
            cola_no_prioritarios.put(cliente) 

    # Encolar clientes preferenciales
    while not cola_no_prioritarios.empty():
        cliente = cola_no_prioritarios.get()
        es_preferencial = cliente[2]
        if es_preferencial:
            cola_ordenada.put(cliente)
        else:
            cola_resto_clientes.put(cliente)

    # Encolar el resto de clientes
    while not cola_resto_clientes.empty():
        cliente = cola_resto_clientes.get()
        cola_ordenada.put(cliente)

 
    # print("\ncola original:", cola.queue)
    # print("\ncola ordenada:", cola_ordenada.queue)
    return cola_ordenada

cola18 = Cola()
clientes: list[(str, int, bool, bool)] = [
    ("Juen", 1, True, False),
    ("Rami", 2, True, True),
    ("Peluca", 3, False, False),
    ("Perro", 4, False, True),
    ("Roman", 5, True, False),
    ("Mapi", 6, False, False),
    ("Mex", 7, True, True),
    ("Curry", 8, True, False),
    ("Lio", 9, False, True),
]
for cliente in clientes:
    cola18.put(cliente)
# Orden deberia ser: 
# Rami, Perro, Mex, Lio (prioritarios)  _ True
# Juen, Roman, Curry (preferenciales)   True False
# Peluca, Mapi (resto)                  False False

# print("\ncola ordenada:", orden_atencion(cola18).queue)



# 4: DICCIONARIOS (19 al 23) (falta 22 - 23)
# ------------
# Ejercicio 19 OK 23/10
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
def agrupar_por_longitud(nombre_archivo: str) -> dict:
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

    archivo.close()

    return dict_longitudes


# print(agrupar_por_longitud("ejemplomapi.txt"))

# ------------
# Ejercicio 20 OK 27/10
# ------------
# Volver a implementar la función que calcula el promedio de las notas de los alumnos, 
# pero ahora devolver un # diccionario {libreta universitaria : promedio} 
# con los promedios de todos los alumnos.
def promedio_estudiantes(nombre_archivo_notas: str) -> dict[str, float]:

    notas_por_alumno: dict[str, list[float]] = dict()
    
    with open(nombre_archivo_notas) as archivo:
        lineas = archivo.readlines()

        for linea in lineas:
            libreta:str = linea.split()[0].replace(",", "")
            print("libreta:", libreta)
            nota:float = float(linea.split()[-1])
            print("libreta:", nota)

            if libreta not in notas_por_alumno.keys():
                notas_por_alumno[libreta] = [nota]
            else:
                notas_por_alumno[libreta].append(nota)

    promedio_por_alumno: dict[str, float] = dict()

    def calcular_promedio(notas: list[float]) -> float:
        return sum(notas) / len(notas)

    for key in notas_por_alumno:
        promedio_por_alumno[key] = calcular_promedio(notas_por_alumno[key])
    
    return promedio_por_alumno

# print(promedio_estudiantes("notas.csv"))


# ------------
# Ejercicio 21 OK 27/10
# ------------

# Implementar la función la palabra mas frecuente(in nombre archivo : str) → str 
# que devuelve la palabra que más veces aparece en un archivo de texto. 
# Se aconseja utilizar un diccionario de palabras para resolver el problema.

def palabra_mas_frecuente(nombre_archivo_palabras: str) -> str:
    with open(nombre_archivo_palabras) as archivo:
        lineas:list[str] = archivo.readlines()

        frecuencia_palabras: dict[str, int] = {}

        for linea in lineas:
            for palabra in linea.split():
                palabra = palabra.replace(",", "")
                if palabra not in frecuencia_palabras.keys():
                    frecuencia_palabras[palabra] = 1
                else:
                    frecuencia_palabras[palabra] += 1

        frecuencia_maxima: int = 0
        palabra_mayor_frecuencia: str = ""

        for key, item in frecuencia_palabras.items():
            if item > frecuencia_maxima:
                frecuencia_maxima = item
                palabra_mayor_frecuencia = key
            
    return palabra_mayor_frecuencia


# (print("la palabra mas frecuente es", palabra_mas_frecuente("palabras_frecuentes.txt")))

# ------------
# Ejercicio 22 27/10
# ------------

"""
Nos piden desarrollar un navegador web muy simple que debe llevar un registro de los sitios web visitados por los
usuarios del sistema. El navegador debe permitir al usuario navegar hacia atrás y hacia adelante en la historia de navegación.
1. Crea un diccionario llamado historiales que almacenará el historial de navegación para cada usuario. Las claves del
diccionario serán los nombres de usuario y los valores serán pilas.
2. Implementa una función llamada visitar sitio(historiales, usuario, sitio) que reciba el diccionario de historiales,
el nombre de usuario y el sitio web visitado. La función debe agregar el sitio web al historial del usuario correspondiente.
3. Implementa una función llamada navegar atras(historiales, usuario) que permita al usuario navegar hacia atrás en
la historia de navegación. Esto implica sacar el sitio web más reciente del historial del usuario.
4. Implementa una función llamada navegar adelante(historiales, usuario) que permita al usuario navegar hacia ade-
lante en la historia de navegación. Esto implica volver a agregar el sitio web previamente sacado.
Ejemplo de uso:
historiales = {}
visitar_sitio(historiales, "Usuario1", "google.com")
visitar_sitio(historiales, "Usuario1", "facebook.com")
navegar_atras(historiales, "Usuario1")
visitar_sitio(historiales, "Usuario2", "youtube.com")
navegar_adelante(historiales, "Usuario1")
"""