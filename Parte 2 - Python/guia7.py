# Recordar usar las anotaciones de tipado en todas las variables. Por ejemplo: def funcion(numero: int) ->bool:.
# En los ejercicios se pueden usar funciones matem´aticas como por ejemplo: sqrt, round, floor, ceil, %.
# https://docs.python.org/es/3/library/functions.html
# Revisar la especificaci´on de las operaciones comunes sobre secuencias: https://docs.python.org/es/3/library/stdtypes.html?highlight=list#typesseq

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


# problema divideATodos (in s:seq<Z>, in e: Z) : Bool {
# requiere: {e 6 = 0 }
# asegura: { (res = true) ↔ (para todo i ∈ Z si 0 ≤ i < |s| → s[i] mod e = 0)}
# }


# 1.7 Analizar la fortaleza de una contraseña.
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
