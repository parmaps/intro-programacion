# P: En mi caso habia especificado el tipo de dato como list[int], y luego llame a la funcion con palabras, pero en ninguno momento tuve un error.
# Por que es esto? como deberia funcionar?
"""
R:
En Python, las anotaciones de tipo son principalmente sugerencias para herramientas y desarrolladores, y no afectan la ejecución del código. 
Python es un lenguaje de tipado dinámico, lo que significa que no se verifica estáticamente el tipo de datos durante la compilación.

Cuando anotas el tipo de parámetro como list[int], estás sugiriendo que la función debería recibir una lista de enteros. 
Sin embargo, en tiempo de ejecución, Python no realiza una verificación estricta de tipo en la llamada a la función. 
Puedes pasarle una lista de cualquier tipo, y Python intentará ejecutar el código siempre que sea posible.

En tu caso, especificaste list[int], pero llamaste a la función con una lista de palabras (List[str]). 
Python no lanzó un error porque las anotaciones de tipo son opcionales y no afectan la ejecución del código.

Es importante destacar que las anotaciones de tipo son herramientas útiles para mejorar la legibilidad del código, 
proporcionar documentación adicional y facilitar el uso de herramientas externas, como linters y sistemas de tipo estático (por ejemplo, MyPy). 
Sin embargo, estas anotaciones no introducen una verificación de tipo estricta en tiempo de ejecución en Python.

Si bien puedes especificar anotaciones de tipo, es común en Python confiar en la documentación y en la legibilidad del código, 
y no necesitas adherirte estrictamente a las anotaciones de tipo para que el código funcione correctamente. 
La convención y la comunicación clara en el código son fundamentales.
"""

# Recordar usar las anotaciones de tipado en todas las variables. Por ejemplo: def funcion(numero: int) ->bool:.
# En los ejercicios se pueden usar funciones matem´aticas como por ejemplo: sqrt, round, floor, ceil, %.
# https://docs.python.org/es/3/library/functions.html
# Revisar la especificaci´on de las operaciones comunes sobre secuencias: https://docs.python.org/es/3/library/stdtypes.html?highlight=list#typesseq


# Que aprendi?
"""
-La triple comilla es un 'docstring': sirve para documentar codigo. 
En una funcion se inserta dentro del bloque def y explica brevemente que hace, sus parámetros y su retorno. 

-usar snake_case en Python

-elemento in list:
se utiliza para verificar si un elemento está presente en una lista, ej:
def pertenece(lista: list[any], elem: any) -> bool:
    return elem in lista

-s.count(e): para contar las ocurrencias del elemento e en la lista s

-all: si todos los elementos de un generator son True, devuelve True

-any: si algun elemento de un generator es True, devuelve True

-generators: 
Una expresión generadora en Python es una forma concisa de crear secuencias iterables (como listas, tuplas, o conjuntos) 
utilizando una sintaxis más compacta que las list comprehensions. 
Mientras que una list comprehension crea una lista, una expresión generadora crea un objeto generador.
Ejemplo con any any(len(palabra) > 7 for palabra in palabras)

-def invertir_cadena(cadena):
    return cadena[::-1]

-ver 1.6) palindromo para manejo de textos e indices

-indices negativos:
En Python, los índices negativos se utilizan para contar desde el final de una secuencia, como una cadena o una lista. 
En lugar de comenzar desde el primer elemento (índice 0), comienzan desde el último elemento (índice -1), y así sucesivamente. 
 P  y  t  h  o  n
 0  1  2  3  4  5
-6 -5 -4 -3 -2 -1


-Funciones de Python: islower(), isupper(), isdigit()
-> Ejs
    #  def tieneMinuscula(password: str) -> bool:
    #   return any(c.islower() for c in password) (devuelve si alguno -"any"- es minuscula -"c.islower()"- en el generador -"for c in password"-)
    #  def tieneMayuscula(password: str) -> bool:
    #     return any(c.isupper() for c in password)
    # def tieneNumero(password: str) -> bool:
    #     return any(c.isdigit() for c in password)

    
1.8) funcion con tipo de tuplas:
def saldo(movimientos: list[tuple[str, int]]) -> int:
    
1.9)
-Conjuntos:
    Un conjunto (set) en Python es una colección no ordenada de elementos únicos.
    Puedes utilizar un conjunto para almacenar múltiples valores sin duplicados.  
    Puedes utilizar conjuntos (set) para almacenar (por ejemplo) las vocales distintas en lugar de una lista. 
    Los conjuntos no permiten elementos duplicados, por lo que automáticamente te aseguras de tener solo vocales únicas.
    Los conjuntos no mantienen un orden específico, por lo que el orden de impresión puede no ser el mismo que el orden en el que se agregaron los elementos. 
    La sintaxis básica:
    # Crear un conjunto vacío
    conjunto_vacio = set()
    # Crear un conjunto con elementos
    mi_conjunto = {1, 2, 3, 4, 5}
    # Agregar elementos a un conjunto
    mi_conjunto.add(6)
    mi_conjunto.add(7)

    set(...): Convierte el resultado en un conjunto (en el ejemplo eliminando duplicados y dejando solo vocales únicas).

-Funciones lamdba
    3) Expresiones lamdba: 
    Una expresión lambda en Python es una forma de crear funciones anónimas o sin nombre. 
    Son útiles cuando necesitas funciones pequeñas y temporales, generalmente para operaciones simples.
    La sintaxis básica de una expresión lambda es:
        lambda argumentos: expresion  
    Ej.:
    # Función lambda que suma dos números
    suma = lambda x, y: x + y   

-> Ejemplo con ambas 
    def tiene_al_menos_3_vocales_distintas_GPT(palabra: str) -> bool:
    # Verifica si una palabra tiene al menos 3 vocales distintas.

    # Filtrar las vocales utilizando un conjunto y una funcion anonima lambda
    vocales = set(filter(lambda letra: letra in "aeiou", palabra))
    return len(vocales) >= 3

2.5) Para dar vuelta un string, usar esto: string[::-1]
Puedes usar esta técnica no solo con cadenas de texto, sino también con listas y otras secuencias en Python.
    El primer : indica que estamos utilizando "slicing".
    El segundo : después del primer : indica el límite superior e inferior del slice, y está en blanco, lo que significa "toda la cadena".
    El -1 como tercer valor indica el paso. En este caso, -1 significa que estás tomando elementos en orden inverso.
-> la sintaxis indica que estás utilizando un "slice" con un paso de -1, lo que invierte el orden de los elementos.
Ejemplo: return palabra[::-1]

Otro ejemplo distinto de slicing:
original_numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
seleccionados = original_numeros[1:8:2]
resultado: [1, 3, 5, 7].
Como funciona?
Estamos seleccionando elementos desde el índice 1 hasta el índice 8 (sin incluirlo), con un paso de 2. 
Por lo tanto, estamos seleccionando los elementos en las posiciones 1, 3, 5, y 7.

3) Puedes utilizar la función sum para calcular la suma de los elementos de la lista y luego dividir por la longitud de la lista
(para obtener promedio)
-> forma más concisa y eficiente de calcular la suma de una lista en comparación con un bucle for explícito.
# def promedio_con_sum(notas: list[int]) -> int:
        # return sum(notas) // len(notas)

"""

# ------------
# Ejercicio 1
# ------------

# Nota: Cada problema puede tener mas de una implementacion. Probar utilizando distintas formas de recorrido sobre secuencias,
# y distintas funciones de Python. No te conformes con una solucion, recordar que siempre conviene consultar con tus docentes.

# problema pertenece (in s:seq<Z>, in e: Z) : Bool {
#   requiere: { T rue }
#   asegura: { (res = true) ↔(existe un i ∈ Z tal que 0 ≤ i < |s| ∧ s[i] = e)}
# }
# Implementar al menos de 3 formas distintas este problema.
# ¿Si la especificaramos e implementaramos con tipos genericos,
# se podrıa usar esta misma funcion para buscar un caracter dentro de un string?


# list[int]: POR QUE NO FUNCIONA ESTO? ME PIDE QUE AGREGUE COMILLAS (AL PROFESOR NO LE SUCEDE)
# RESPUESTA: depende el sistema operativo (al parecer) cual version compila: si list[int], o "list[int]", o [int]
# list[int]: POR QUE PUEDO MANDAR CUALQUIER TIPO AL LLAMAR LA FUNCION? DONDE DEBERIA MANIFESTARSE ESTO??
def pertenece1(lista: list, elemIn: str) -> bool:
    for numero in lista:
        if elemIn == numero:
            return True
    return False


# ESTUDIAR BIEN COMO FUNCIONA ESTE
# CLASE: dice si elemIn esta en lista
def pertenece1short(lista: list, elemIn: int) -> bool:
    return elemIn in lista


def pertenece2(lista: "list[int]", elemIn: int) -> bool:
    for i in range(len(lista)):
        if lista[i] == elemIn:
            return True
    return False


def pertenece3(lista: list, elemIn: int) -> bool:
    indice: int = 0
    while indice < len(lista):
        if lista[indice] == elemIn:
            return True
        indice += 1
    return False


# si aparece al menos 1 vez (count > 0), pertenece
def perteneceClase(s: "list[int]", e: int):
    return s.count(e) == 0


# print(pertenece1([1,2], 2))
# print(pertenece1short([1,2], 2))
# print(pertenece1([1,"a"], "a"))
# print(pertenece1short([1,"a"], "a"))
# print(pertenece1([1,"a"], "b"))
# print(pertenece1short([1,"a"], "b"))
# print(pertenece1("unodostres", "dos"))
# print(pertenece1("unodostres", "unodostres"))
# print(pertenece1(["unodostres", "dos"], "dos"))


# 1.2) problema divideATodos (in s:seq<Z>, in e: Z) : Bool {
#   requiere: {e != 0 }
#   asegura: { (res = true) ↔ (para todo i ∈ Z si 0 ≤ i < |s| → s[i] mod e = 0)}
# }
"""
Verifica si todos los elementos de la lista son divisibles por elem_in.

:param lista: Lista de enteros.
:param elem_in: Número por el cual se verifica la divisibilidad.
:return: True si todos los elementos son divisibles, False en caso contrario.
"""


def divide_a_todos(lista: list[int], elem_in: int) -> bool:
    for numero in lista:
        if numero % elem_in != 0:
            return False
    return True


def divide_a_todos_gpt(lista: list[int], elem_in: int) -> bool:
    return all(numero % elem_in == 0 for numero in lista)


# print(divide_a_todos([1, 2, 3], 1))  # True
# print(divide_a_todos([1, 2, 3], 2))  # False
# print(divide_a_todos([2, 8, 152], 2))  # True
# print(divide_a_todos([9, 15, 152], 3))  # False
# print(divide_a_todos([9, 15, 153], 3))  # True
# print(divide_a_todos_gpt([1, 2, 3], 1))  # True
# print(divide_a_todos_gpt([1, 2, 3], 2))  # False
# print(divide_a_todos_gpt([2, 8, 152], 2))  # True
# print(divide_a_todos_gpt([9, 15, 152], 3))  # False
# print(divide_a_todos_gpt([9, 15, 153], 3))  # True


# 1.3) problema sumaTotal (in s:seq<Z>) : Z {
#   requiere: { T rue }
#   asegura: { res es la suma de todos los elementos de s}
# }
# Nota: no utilizar la función sum() nativa


def suma_total(lista: list[int]) -> int:
    """
    Calcula la suma de todos los elementos en la lista.

    :param lista: Lista de enteros.
    :return: Suma de los elementos en la lista.
    """
    total: int = 0
    for numero in lista:
        total += numero
    return total


# print(suma_total([1, 2, 3])) # 6
# print(suma_total([10, 20, 30])) # 60
# print(suma_total([9, 15, 153])) # 177


# 1.4) problema ordenados (in s:seq<Z>) : Bool {
# requiere: { T rue }
# asegura: { res = true ↔(para todo i ∈ Z si 0 ≤ i < (|s| − 1) → s[i] < s[i + 1]}
# }
def ordenados(lista: list[int]) -> bool:
    for i in range(len(lista) - 1):
        if lista[i] >= lista[i + 1]:
            return False
    return True


def ordenados_con_all(lista: list[int]) -> bool:
    return all(lista[i] < lista[i + 1] for i in range(len(lista) - 1))


# print(ordenados([1, 2, 3])) # True
# print(ordenados([1, 3, 2])) # False
# print(ordenados([1, 1, 3])) # False
# print(ordenados([-1, 2, 3, 4, 5, 150, 1843])) # True

# print(ordenados_con_all([1, 2, 3])) # True
# print(ordenados_con_all([1, 3, 2])) # False
# print(ordenados_con_all([1, 1, 3])) # False
# print(ordenados_con_all([-1, 2, 3, 4, 5, 150, 1843])) # True


# 1.5) Dada una lista de palabras, devolver verdadero si alguna palabra tiene longitud mayor a 7.
def mas_largos_que_7(palabras: list[str]) -> bool:
    for palabra in palabras:
        if len(palabra) > 7:
            return True
    return False


def mas_largos_que_7_con_all(palabras: list[str]) -> bool:
    return any(len(palabra) > 7 for palabra in palabras)


# print(mas_largos_que_7(["hola", "como", "andas"]))  # False
# print(mas_largos_que_7(["hola", "como", "campeon"]))  # False
# print(mas_largos_que_7(["hola", "babasonico", "campeon"]))  # True

# print(mas_largos_que_7_con_all(["hola", "como", "andas"]))  # False
# print(mas_largos_que_7_con_all(["hola", "como", "campeon"]))  # False
# print(mas_largos_que_7_con_all(["hola", "babasonico", "campeon"]))  # True


# 1.6) Dado un texto en formato string, devolver verdadero si es palı́ndromo (se lee igual en ambos sentidos),
# falso en caso contrario
def es_par(numero: int):
    return numero % 2 == 0


def invertir_cadena(cadena):
    return cadena[::-1]


def palindromo(texto: str) -> bool:
    """
    Verifica si el texto es palı́ndromo (se lee igual en ambos sentidos).
    Divide la palabra a la mitad (de distinta manera si tiene longitud par o impar),
    la invierte y pregunta si ambas mitades son iguales.

    :param texto: Texto en formato string.
    :return: True si es palindromo, False en caso contrario.
    """

    # Separar la primera mitad del texto
    slice_mitad1 = slice(0, len(texto) // 2)
    mitad1 = texto[slice_mitad1]
    # podria usar directamente: mitad1 = texto[:len(texto) // 2]

    if es_par(
        len(texto)
    ):  # Si es par, la segunda aparte arranca desde la mitad de la palabra
        slice_mitad2 = slice(len(texto) // 2, len(texto))

    else:  # Si es impar, no contempla el caracter del medio
        slice_mitad2 = slice(len(texto) // 2 + 1, len(texto))

    # Invertir la segunda mitad
    mitad2_invertida = invertir_cadena(texto[slice_mitad2])

    # Comparar mitades
    return mitad1 == mitad2_invertida


def palindromo_gpt(texto: str) -> bool:
    """
    Verifica si el texto es palíndromo (se lee igual en ambos sentidos).

    :param texto: Texto en formato string.
    :return: True si es palíndromo, False en caso contrario.
    """

    # Separar las mitades del texto

    mitad1 = texto[: len(texto) // 2]
    # va desde el principio con ":", hasta la mitad con "len(texto) // 2"
    # print(mitad1)

    # ESTO VALE SOLO PARA IMPARES:
    # Arrancar en la mitad, sin la letra del medio
    t1 = texto[(len(texto) // 2 + 1) :]  # +1 corre para la derecha
    t2 = texto[-(len(texto) // 2) :]

    # Arrancar en la mitad, con la letra del medio
    t3 = texto[(len(texto) // 2) :]
    t4 = texto[
        -(len(texto) // 2 + 1) :
    ]  # al arrancar con indice negativo, +1 corre para la izquierda
    # print(t1, t2, t3, t4)

    t5 = texto[
        -(len(texto) // 2 + 10) :
    ]  # como +10 corre 10 para la izquierda, si la palabra tiene 20 caracteres o menos la imprime toda
    # print("t5:", t5)

    mitad2 = (
        texto[-(len(texto) // 2) :]
        if es_par(len(texto))
        else texto[(len(texto) // 2 + 1) :]
    )
    mitad2_indice_negativo = (
        texto[-(len(texto) // 2) :]
        if es_par(len(texto))
        else texto[-(len(texto) // 2) :]
    )
    # va desde la mitad con "-(len(texto) // 2)" (contando desde el final por el indice negativo), hasta el final con ":"
    # print(mitad2)

    # Comparar mitades directamente
    return mitad1 == mitad2_indice_negativo[::-1]


# print(palindromo("poop")) # True
# print(palindromo("acurruca")) # True
# print(palindromo("ojo")) # True
# print(palindromo("sometemos")) # True

# print(palindromo_gpt("poop"))  # True
# print(palindromo_gpt("acurruca"))  # True
# print(palindromo_gpt("ojo"))  # True
# print(palindromo_gpt("sometemos"))  # True

# 1.7) Analizar la fortaleza de una contraseña.
# El parametro de entrada de la funcion sera un string con la contrasena a analizar,
# y la salida otro string con tres posibles valores: VERDE, AMARILLA y ROJA.
# Nota: en python la “˜n/ ˜N” es considerado un caracter especial y no se comporta como cualquier otra letra.
# La contraseña sera VERDE si:
# a) la longitud es mayor a 8 caracteres
# b) tiene al menos 1 letra minuscula.
# c) tiene al menos 1 letra mayuscula.
# d ) tiene al menos 1 dıgito numerico (0..9)
# La contraseña sera ROJA si:
# a) la longitud es menor a 5 caracteres.
# En caso contrario sera AMARILLA.


def analizarPassword(password: str) -> str:
    def tieneMinuscula(password: str) -> bool:
        for caracter in password:
            if caracter >= "a" and caracter <= "z":
                return True
        return False

    def tieneMayuscula(password: str) -> bool:
        for caracter in password:
            if caracter >= "A" and caracter <= "Z":
                return True
        return False

    def tieneNumero(password: str) -> bool:
        for caracter in password:
            if caracter >= "0" and caracter <= "9":
                return True
        return False

    # Implementaciones con Python library
    #  def tieneMinuscula(password: str) -> bool:
    #   return any(c.islower() for c in password) (devuelve si alguno "any" es minuscula "c.islower()" en el generador "for c in password")
    #  def tieneMayuscula(password: str) -> bool:
    #     return any(c.isupper() for c in password)
    # def tieneNumero(password: str) -> bool:
    #     return any(c.isdigit() for c in password)

    condicionVerde: bool = (
        len(password) > 8
        and tieneMinuscula(password)
        and tieneMayuscula(password)
        and tieneNumero(password)
    )

    if len(password) < 5:
        return "ROJA"
    elif condicionVerde:
        return "VERDE"
    else:
        return "AMARILLA"


# P: Es mejor retornar en cada condicion o armar una variable "fortalezaPassword", modificarla en cada condicion y retonar esa variable?
"""
R:
Ambos enfoques son válidos y pueden depender en gran medida de tus preferencias personales y del estilo de programación que prefieras seguir. 
Sin embargo, hay algunas consideraciones que podrían influir en tu elección:

Retornar en Cada Condición:
Ventajas:
    Puede hacer que el código sea más claro y fácil de entender, ya que cada condición tiene su propio retorno y no hay una variable adicional que podría introducir complejidad.
    Menos propenso a errores, ya que no hay una variable que debe ser manejada y actualizada en cada condición.

Desventajas:
    Algunas personas pueden argumentar que múltiples retornos pueden hacer que el código sea menos estructurado y más difícil de seguir.

Utilizar una Variable y Retornar al Final:
Ventajas:
    Puede ser útil si necesitas realizar más operaciones o lógica antes de decidir el resultado final.
    Si deseas tener más control sobre el flujo del programa antes de realizar el retorno final.

Desventajas:
    Puede introducir complejidad innecesaria si la variable se actualiza en múltiples lugares y es difícil de rastrear.

Recomendación:
En este caso específico, dado que estás tomando decisiones simples basadas en condiciones específicas, 
la opción de "Retornar en Cada Condición" parece más apropiada. Hace que el código sea más claro y fácil de entender.

Si las operaciones o lógica entre las condiciones fueran más complejas y requirieran un manejo más avanzado de la variable, 
entonces la opción de "Utilizar una Variable y Retornar al Final" podría ser más adecuada.

Recuerda que la legibilidad y la claridad del código son muy importantes. 
En última instancia, elige el enfoque que encuentres más claro y que facilite la comprensión del código por parte de otros programadores (o de ti mismo en el futuro).
"""

# print(analizarPassword("hola")) # ROJA
# print(analizarPassword("Password1")) # VERDE
# print(analizarPassword("Password1")) # VERDE
# print(analizarPassword("Password1a")) # VERDE
# print(analizarPassword("passwordpassword")) # AMARILLA


# 1.8) Dada una lista de tuplas, que representa un historial de movimientos en una cuenta bancaria, devolver el saldo actual.
# Asumir que el saldo inicial es 0. Las tuplas tienen una letra que nos indica el tipo de movimiento “I” para ingreso de
# dinero y “R” para retiro de dinero, y adem´as el monto de cada operaci´on. Por ejemplo, si la lista de tuplas es [(‘‘I’’,
# 2000), (‘‘R’’, 20),(‘‘R’’, 1000),(‘‘I’’, 300)] entonces el saldo actual es 1280.


def saldo(movimientos: list[tuple[str, int]]) -> int:
    """
    Calcula el saldo actual a partir de un historial de movimientos en una cuenta bancaria.

    :param movimientos: Lista de tuplas representando movimientos. Cada tupla tiene una letra que indica el tipo de
                       movimiento ("I" para ingreso, "R" para retiro) y el monto de la operación.
    :type movimientos: list[tuple[str, int]]

    :return: El saldo actual después de procesar los movimientos.
    :rtype: int
    """

    saldo: int = 0

    def esIngreso(movimiento: str) -> bool:
        return movimiento[0] == "I"

    for movimiento in movimientos:
        if esIngreso(movimiento):
            saldo += movimiento[1]
        else:
            saldo -= movimiento[1]

    return saldo


# def saldo(movimiento:[(str), (int)]) -> int:
# print(saldo([("R", 100), ("I", 50), ("R", 75)])) # -125
# print(saldo([("R", 100), ("R", 100), ("R", 100)])) # -300
# print(saldo([("I", 2000), ("R", 20), ("R", 1000), ("I", 300)])) # 1280


# 1.9) Recorrer una palabra en formato string y devolver True si esta tiene al menos 3 vocales distintas y False en caso contrario.
def tiene_al_menos_3_vocales_distintas(palabra: str) -> bool:
    # Approach 1)
    # Filtrar vocales
    # Para la vocal actual:
    # Si no esta en una lista de vocales distintas, agregarla
    # Repetir
    # Fuera del loop, contar cantidad de vocales distintas

    def filtrar_vocales(letra: str) -> str:
        return letra in "aeiou"

    vocales = list(filter(filtrar_vocales, palabra))

    vocales_distintas: list[str] = []

    for vocal in vocales:
        if vocal not in vocales_distintas:
            vocales_distintas.append(vocal)

    return len(vocales_distintas) >= 3


def tiene_al_menos_3_vocales_distintas_GPT(palabra: str) -> bool:
    """
    Verifica si una palabra tiene al menos 3 vocales distintas.

    :param palabra: La palabra a verificar.
    :type palabra: str
    :return: True si hay al menos 3 vocales distintas, False en caso contrario.
    :rtype: bool

    Diferencias:
    1) Uso de conjuntos:
    Puedes utilizar conjuntos (set) para almacenar las vocales distintas en lugar de una lista.
    Los conjuntos no permiten elementos duplicados, por lo que automáticamente te aseguras de tener solo vocales únicas.

    2) Uso de funciones integradas:
    Puedes aprovechar funciones integradas de Python para simplificar tu código.

    3) Expresiones lamdba:
    Una expresión lambda en Python es una forma de crear funciones anónimas o sin nombre. Son útiles cuando necesitas funciones pequeñas y temporales, generalmente para operaciones simples.
    """

    # Filtrar las vocales utilizando un conjunto y una funcion anonima lambda
    vocales = set(filter(lambda letra: letra in "aeiou", palabra))
    return len(vocales) >= 3


# print(tiene_al_menos_3_vocales_distintas("qwrty")) # 0 -> False
# print(tiene_al_menos_3_vocales_distintas("banana")) # 1 -> False
# print(tiene_al_menos_3_vocales_distintas("falopero")) # 3 -> True
# print(tiene_al_menos_3_vocales_distintas("murcielago")) # 5 -> True


# ------------
# Ejercicio 2
# ------------
# Implementar las siguientes funciones sobre secuencias pasadas por parametro:

# 2.1) Dada una lista de numeros, en las posiciones pares borra el valor original y coloca un cero.
# Esta funcion modifica el parametro ingresado, es decir, la lista es un parametro de tipo inout.
# PARAMETRO INOUT: ingresa, se modifica y luego se utiliza con este nuevo valor (la funcion no retorna nada)


def borrarPosicionesParesInOut(lista: "list[int]") -> None:
    for i in range(0, len(lista), 2):
        lista[i] = 0


# a:[int]= [1, 2, 3, 4, 5]
# print(a)
# borrarPosicionesPares(a)
# print(a)

# 2.2) Lo mismo del punto anterior pero esta vez sin modificar la lista original, devolviendo una nueva lista, igual a la anterior
# pero con las posiciones pares en cero, es decir, la lista pasada como parametro es de tipo in


def borrarPosicionesParesIn(lista: "list[int]") -> [int]:
    nuevaLista = lista.copy()
    for i in range(0, len(lista), 2):
        # print(lista[i])
        nuevaLista[i] = 0
    return nuevaLista


# b:[int]= [1, 2, 3, 4, 5]
# print("b:", b)
# print("nueva lista a partir de b: ", borrarPosicionesParesIn(b))
# print("b:", b)


# 2.3) Dada una cadena de caracteres devuelva una cadena igual a la anterior, pero sin las vocales.
# No se agregan espacios, sino que borra la vocal y concatena a continuacion.
def borrarVocales(palabra: str) -> str:
    palabraSinVocales = ""
    vocales = ["a", "e", "i", "o", "u"]

    for i in range(len(palabra)):
        if palabra[i] not in vocales:
            palabraSinVocales = palabraSinVocales + (palabra[i])
    return palabraSinVocales


# print(borrarVocales("joaquin"))
# print(borrarVocales("lucas"))


# 2.4) problema reemplazaVocales (in s:seq<Char>) : seq<Char> {
#   requiere: { T rue }
#   asegura: {Para todo i ∈ Z, si 0 ≤ i < |res| → (pertenece(<‘a’,‘e’,‘i’,‘o’,‘u’>, s[i]) ∧ res[i] = ‘ ’)
#             ∨ #   (¬ pertenece(<‘a’,‘e’,‘i’,‘o’,‘u’>, s[i]) ∧ res[i] = s[i] ) ) }
#   }
# Reemplaza cada vocal por un guion bajo, y deja el resto de los caracteres intactos


def reemplazar_vocales(palabra: list[str]) -> list[str]:
    palabraNueva: str = ""
    vocales: str = "aeiou"

    for letra in palabra:
        if letra in vocales:
            palabraNueva += "_"
        else:
            palabraNueva += letra

    return palabraNueva


# print(reemplazar_vocales("joaquin"))
# print(reemplazar_vocales("lucas"))


# 2.5) problema daVueltaStr (in s:seq<Char>) : seq<Char> {
#   requiere: { T rue }
#   asegura: { Para todo i ∈ Z si 0 ≤ i < |res| → res[i] = s[|s| − i − 1]}
# }
def dar_vuelta_string(palabra: list[str]) -> list[str]:
    return palabra[::-1]


# print(dar_vuelta_string("hola"))

# 6. problema eliminarRepetidos (in s:seq<Char>) : seq<Char> {
# requiere: { T rue }
# asegura: {(|res| ≤ |s|) ∧ (para todo i ∈ Z si 0 ≤ i < |s| → pertenece(s[i], res)) ∧ (para todo i, j ∈ Z si
# (0 ≤ i, j < |res| ∧ i != j) → res[i] != res[j])}
# }


def eliminar_repetidos(texto: list[str]) -> list[str]:
    nuevoTexto: str = ""

    for letra in texto:
        if not pertenece1(nuevoTexto, letra):
            print(letra)
            nuevoTexto += letra
    return nuevoTexto

# print(eliminar_repetidos("hola")) # hola
# print(eliminar_repetidos("carlitox")) # carlitox
# print(eliminar_repetidos("merengue")) # merngu
# print(eliminar_repetidos("lucas parma")) # lucas prm
# print(eliminar_repetidos("neuquen")) # neuq


# -----------
# Ejercicio 3
# -----------
# Implementar una función para conocer el estado de aprobación de una materia
# a partir de las notas obtenidas por un/a alumno/a cumpliendo con la siguiente especificación:
# problema aprobado (in notas: seq<Z>) : Z {
# requiere: {|notas| > 0}
# requiere: {Para todo i ∈ Z si 0 ≤ i < |notas| → 0 ≤ notas[i] ≤ 10)}
# asegura: {res = 1 ↔ todos los elementos de notas son mayores o iguales a 4 y el promedio es mayor o igual a 7}
# asegura: {res = 2 ↔ todos los elementos de notas son mayores o iguales a 4 y el promedio está entre 4 (inclusive) y 7}
# asegura: {res = 3 ↔ alguno de los elementos de notas es menor a 4 o el promedio es menor a 4}
# }


def aprobado(notas: list[int]) -> int:
    print(notas)

    def son_mayores_a_4(notas: list[int]) -> bool:
        return all(nota >= 4 for nota in notas)

    def promedio(notas: list[int]) -> int:
        total_notas: int = 0
        for nota in notas:
            total_notas += nota
        return total_notas // len(notas)
    
    # def promedio_con_sum(notas: list[int]) -> int:
        # return sum(notas) // len(notas)

    if son_mayores_a_4(notas) and promedio(notas) >= 7:
        return 1
    elif son_mayores_a_4(notas) and promedio(notas) < 7 and promedio(notas) >= 4:
        return 2
    else:
        return 3
    
print(aprobado([3, 5, 6])) # 3: no aprueba
print(aprobado([4, 5, 6])) # 2: aprueba
print(aprobado([7, 7, 6])) # 2: aprueba
print(aprobado([7, 7, 7])) # 1: promociona



# -----------
# Ejercicio 4
# -----------

# -----------
# Ejercicio 5
# -----------
# Implementar las siguientes funciones sobre listas de listas:


# 5.1) problema perteneceACadaUno (in s:seq<seq<Z>>, in e:Z, out res: seq<Bool>) {
#   requiere: { True }
#   asegura: { Para todo i ∈ Z si 0 ≤ i < |res| → (res[i] = true ↔ pertenece(s[i], e))}
# }


def perteneceACadaUno(listas: [[int]], numero: int) -> [bool]:
    listaDePerteneces: [bool] = []
    # si pertenece a la lista, devolver True en esa posicion
    for lista in listas:
        if pertenece1(lista, numero):
            print("pertenece el numero", numero, "a la lista", lista)
            listaDePerteneces.append(True)
        else:
            listaDePerteneces.append(False)

    return listaDePerteneces


# ESTE ES MAS LINDO! pero son iguales en comportamiento
def perteneceACadaUnoClase(listas: [[int]], numero: int) -> [bool]:
    listaDePerteneces: [bool] = []
    for lista in listas:
        listaDePerteneces.append(pertenece1(lista, numero))

    return listaDePerteneces


# Nota: Reutilizar la funcion pertenece() implementada previamente para listas
# Ej: [[1, 2], [3, 4], [1, 4]] -> [True, False, True]
# print(perteneceACadaUno([[1, 2], [3, 4], [1, 4]], 1))
# print(perteneceACadaUno([[1, 2], [3, 4], [7, 9], [1, 122]], 122))
# print(perteneceACadaUnoClase([[1, 2], [3, 4], [7, 9], [1, 122]], 122))
