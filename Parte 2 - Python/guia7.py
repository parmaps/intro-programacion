"""
P: en mi caso habia especificado el tipo de dato como list[int], y luego llame a la funcion con palabras, pero en ninguno momento tuve un error. 
por que es esto? como deberia funcionar?

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

# ------------
# Ejercicio 1
# ------------
"""
Que aprendi?
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


"""


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
    
    if es_par(len(texto)): # Si es par, la segunda aparte arranca desde la mitad de la palabra
        slice_mitad2 = slice(len(texto) // 2, len(texto))

    else: # Si es impar, no contempla el caracter del medio
        slice_mitad2 = slice(len(texto) // 2 + 1 , len(texto))
    
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

    mitad1 = texto[:len(texto) // 2] 
    # va desde el principio con ":", hasta la mitad con "len(texto) // 2"
    # print(mitad1)

    # ESTO VALE SOLO PARA IMPARES:
    # Arrancar en la mitad, sin la letra del medio
    t1 = texto[(len(texto) // 2 + 1):] # +1 corre para la derecha
    t2 = texto[-(len(texto) // 2):]

    # Arrancar en la mitad, con la letra del medio
    t3 = texto[(len(texto) // 2):]
    t4 = texto[-(len(texto) // 2 + 1):] # al arrancar con indice negativo, +1 corre para la izquierda
    # print(t1, t2, t3, t4)

    t5 = texto[-(len(texto) // 2 + 10):] # como +10 corre 10 para la izquierda, si la palabra tiene 20 caracteres o menos la imprime toda
    # print("t5:", t5)


    mitad2 = texto[-(len(texto) // 2):] if es_par(len(texto)) else texto[(len(texto) // 2 + 1):]
    mitad2_indice_negativo = texto[-(len(texto) // 2):] if es_par(len(texto)) else texto[-(len(texto) // 2):]
    # va desde la mitad con "-(len(texto) // 2)" (contando desde el final por el indice negativo), hasta el final con ":"
    # print(mitad2)

    # Comparar mitades directamente
    return mitad1 == mitad2_indice_negativo[::-1] 

# print(palindromo("poop")) # True
# print(palindromo("acurruca")) # True
# print(palindromo("ojo")) # True
# print(palindromo("sometemos")) # True

print(palindromo_gpt("poop")) # True
print(palindromo_gpt("acurruca")) # True
print(palindromo_gpt("ojo")) # True
print(palindromo_gpt("sometemos")) # True

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

    fortalezaPassword: str = ""
    if len(password) < 5:
        fortalezaPassword = "ROJA"
    elif (
        len(password) > 8
        and tieneMinuscula(password)
        and tieneMayuscula(password)
        and tieneNumero(password)
    ):
        fortalezaPassword = "VERDE"
    else:
        fortalezaPassword = "AMARILLA"

    return fortalezaPassword


# print(analizarPassword("hola")) # ROJA
# print(analizarPassword("Password1")) # VERDE
# print(analizarPassword("Password1")) # VERDE
# print(analizarPassword("Password1a")) # VERDE
# print(analizarPassword("passwordpassword")) # AMARILLA


# 1.8) Dada una lista de tuplas, que representa un historial de movimientos en una cuenta bancaria, devolver el saldo actual.
# Asumir que el saldo inicial es 0. Las tuplas tienen una letra que nos indica el tipo de movimiento “I” para ingreso de
# dinero y “R” para retiro de dinero, y adem´as el monto de cada operaci´on. Por ejemplo, si la lista de tuplas es [(‘‘I’’,
# 2000), (‘‘R’’, 20),(‘‘R’’, 1000),(‘‘I’’, 300)] entonces el saldo actual es 1280.

# def saldo(movimiento:[(str), (int)]) -> int:


# Ejercicio 2.
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

# 1.2) Lo mismo del punto anterior pero esta vez sin modificar la lista original, devolviendo una nueva lista, igual a la anterior
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


# 3. Dada una cadena de caracteres devuelva una cadena igual a la anterior, pero sin las vocales.
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


# 3.4) problema reemplazaVocales (in s:seq<Char>) : seq<Char> {
#   requiere: { T rue }
#   asegura: {Para todo i ∈ Z, si 0 ≤ i < |res| → (pertenece(<‘a’,‘e’,‘i’,‘o’,‘u’>, s[i]) ∧ res[i] = ‘ ’)
#             ∨ #   (¬ pertenece(<‘a’,‘e’,‘i’,‘o’,‘u’>, s[i]) ∧ res[i] = s[i] ) ) }
#   }


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
