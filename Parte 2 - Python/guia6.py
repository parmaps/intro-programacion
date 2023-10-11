import math
#############
# Ejercicio 1
#############

# 1.1
# problema imprimir hola mundo () {
# requiere: { T rue }
# asegura: { imprime “¡Hola mundo!”por consola}
# }

def imprimir_hola_mundo ():
    print("¡Hola mundo!")


# 1.2
# imprimir un verso(): que imprima un verso de una cancion que vos elijas, respetando los saltos de lınea mediante el caracter ‘\n´

def imprimir_verso():
    print("no tengo ganas de seguir \npero tampoco tengo ganas de parar \ntendria que pensar que me esta pasando \npero es que estoy cansado de pensar")

# 1.3
# raizDe2(): que devuelva la raız cuadrada de 2 con 4 decimales. Ver funcion round
def raiz_de_2() -> float:
    return round(math.sqrt(2),4)

# 1.4
# factorial de dos()
# problema factorial 2 () : Z {
# requiere: { T rue }
# asegura: {res = 2!}
# }

def factorial_de_dos():
    return 2 * 1

# 1.5
# perimetro: que devuelva el perımetro de la circunferencia de radio 1. Utilizar la biblioteca math mediante el comando
# import math y la constante math.pi
# problema perimetro () : R {
# requiere: { T rue }
# asegura: {res = 2 × π }
# }

def perimetro():
    return 2*math.pi


#############
# Ejercicio 2
#############

# 2.1 
# problema imprimir saludo (in nombre: String) {
# requiere: { T rue }
# asegura: {imprime “Hola < nombre >”por pantalla}
# }

def imprimir_saludo(nombre: str):
    print("Hola " + nombre)


# 2.2 raiz cuadrada de(numero): que devuelva la ra´ız cuadrada del n´umero
def raiz_cuadrada(num: int):
    return math.sqrt(num)

# 2.3 fahrenheit a celsius(temp far): que convierta una temperatura en grados Fahrenheit a grados Celcius.
# problema fahrenheit a celsius (in t: R) : R {
# requiere: { T rue }
# asegura: {res = ((t − 32) × 5)/9}
# }
def fahrenheit_a_celsius(temperatura: int):
    return ((temperatura - 32) * 5)/9


# 2.4 
# imprimir dos veces(estribillo): que imprima dos veces el estribillo de una canci´on. 
# Nota: Analizar el comportamiento del operador (*) con strings
def imprimir_dos_veces(estribillo: str):
    print(estribillo *2)


# 2.5 
# problema es multiplo de (in n: Z, in m:Z) : Bool {
# requiere: {m̸ = 0}
# asegura: {(res = true) ↔ (existe un k ∈ Z tal que n = m × k)}
# }

def es_multiplo_de(n: int, m: int) -> bool:
    # (res = true) ↔ (existe un k ∈ Z tal que n = m × k)
    if (n/m).is_integer():
        return True
    return False

# 2.6
# es par(numero): que indique si numero es par (usar la funci´on es multiplo de())
def es_par(numero: int) -> bool:
    if es_multiplo_de(numero,2):
        return True
    return False

# 2.7
# cantidad de pizzas(comensales, min cant de porciones) que devuelva la cantidad de pizzas que necesitamos para
# que cada comensal coma como mınimo min cant de porciones porciones de pizza. Considere que cada pizza tiene 8
# porciones y que se prefiere que sobren porciones

# Ejemplos
# cantidad_de_pizzas(1, 9) = 2
# cantidad_de_pizzas(9, 1) = 2
# cantidad_de_pizzas(2, 4) = 2
# cantidad_de_pizzas(4, 2) = 2
# cantidad_de_pizzas(6, 3) = 3
# cantidad_de_pizzas(4, 5) = 3

def cantidad_de_pizzas(comensales:int , min_cant_de_porciones: int) -> int:
    
    porciones_por_pizza = 8
    cantidad_porciones = min_cant_de_porciones * comensales
    cantidad_pizzas  = math.ceil(cantidad_porciones / porciones_por_pizza)
    return cantidad_pizzas


#############
# Ejercicio 3
#############

# Resuelva los siguientes ejercicios utilizando los operadores logicos and, or, not. Resolverlos sin utilizar alternativa condicional (if).
# 1. alguno es 0(numero1, numero2): dados dos n´umeros racionales, decide si alguno de los dos es igual a 0.
def alguno_es_0(numero1: float, numero2: float) -> bool:
    return numero1 == 0 or numero2 == 0


# 2. ambos son 0(numero1, numero2): dados dos n´umeros racionales, decide si ambos son iguales a 0.
def ambos_son_0(numero1: float, numero2: float) -> bool:
    return numero1 == 0 and numero2 == 0

# 3. problema es nombre largo (in nombre: String) : Bool {
# requiere: { True }
# asegura: {(res = true) ↔ (3 ≤ |nombre| ≤ 8)}
# }

def es_nombre_largo(nombre: str) -> bool:
    return len(nombre) >= 3 and len(nombre) <= 8  

# 4. es bisiesto(a~no): que indica si un a˜no tiene 366 d´ıas. Recordar que un a˜no es bisiesto si es m´ultiplo de 400, 
# o bien es m´ultiplo de 4 pero no de 100.
def es_bisiesto(anio: int) -> bool:
    return (anio/400).is_integer() or ((anio/4).is_integer() and not (anio/100).is_integer())



#############
# Ejercicio 4
#############
# Usando las funciones de python min y max resolver:
# En una plantacion de pinos, de cada arbol se conoce la altura expresada en metros. 
# El peso de un pino se puede estimar a partir de la altura de la siguiente manera:
# 3 kg por cada centımetro hasta 3 metros,
# 2 kg por cada centımetro arriba de los 3 metros.

# Por ejemplo:
# 2 metros pesan 600 kg, porque 200 * 3 = 600
# 5 metros pesan 1300 kg, porque los primeros 3 metros pesan 900 kg y los siguientes 2 pesan los 400 restantes.

# Definir las siguientes funciones, deducir qu´e par´ametros tendr´an a partir del enunciado. 
# Se pueden usar funciones auxiliares si fuese necesario para aumentar la legibilidad.

# 1. Definir la funcion peso pino (recibe una altura en metros)
def peso_pino(altura_arbol: int) -> int:

    altura_arbol_cm = altura_arbol*100
    altura_limite_arbol_cm = 300
    peso_pino_hasta_3_metros = 3 * altura_arbol_cm
    peso_pino_desde_3_metros = 2 * (altura_arbol_cm - 300)


    if (altura_arbol_cm < altura_limite_arbol_cm):
        print("peso pino:", peso_pino_hasta_3_metros)
        return peso_pino_hasta_3_metros
    else:
        peso_pino_hasta_3_metros = 3 * altura_limite_arbol_cm 
        # print("peso hasta 3 metros: ", peso_pino_hasta_3_metros)
        # print("peso desde 2 metros: ", peso_pino_desde_3_metros)
        print("peso pino:", peso_pino_hasta_3_metros + peso_pino_desde_3_metros)
        return peso_pino_hasta_3_metros + peso_pino_desde_3_metros


# 2. Definir la funcion es peso util, recibe un peso en kg y responde si un pino de ese peso le sirve a la fabrica.
# Los pinos se usan para llevarlos a una fabrica de muebles, a la que le sirven arboles de entre 400 y 1000 kilos, 
# un pino fuera de este rango no le sirve a la fabrica.
def es_peso_util(peso_pino: int) -> bool:
    peso_minimo = 400
    peso_maximo = 1000

    # print(peso_pino >= peso_minimo and peso_pino <= peso_maximo)
    return(peso_pino >= peso_minimo and peso_pino <= peso_maximo)

es_peso_util(300)
es_peso_util(700)
es_peso_util(1100)

# 3. Definir la funcion sirve pino, recibe la altura de un pino y responde si un pino de ese peso le sirve a la fabrica.
def sirve_pino(altura_arbol: int) -> bool:
    print("sirve pino?", es_peso_util(peso_pino(altura_arbol)))
    return(es_peso_util(peso_pino(altura_arbol)))


# 4. Definir sirve pino usando composicion de funciones (hecho en 4.3)


#############
# Ejercicio 5
#############

# Implementar los siguientes problemas de alternativa condicional (if). 
# Intenta especificarlos alguno de ellos (todos los que te salgan) en lenguaje semiformal y formal sin utilizar IfThenElseIf.

# 5.1 devolver el doble si es par(numero) que devuelve el doble del numero en caso de ser par y el mismo numero en caso contrario

def devolver_doble_o_mismo(numero: int) -> int:
    if es_multiplo_de(numero, 2):
        print (numero*2)
        return numero*2
    
    print (numero)
    return numero

# 5.2 devolver valor si es par sino el que sigue(numero). que devuelve el mismo n´umero si es par y sino el siguiente.
# Analizar distintas formas de implementaci´on (usando un if-then-else, y 2 if), ¿todas funcionan?

def devolver_valor_si_es_par_sino_el_que_sigue(numero: int) -> int:
    if es_multiplo_de(numero, 2):
        print (numero*2)
        return numero*2
    
    print (numero+1)
    return numero+1

# 5.3 devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9 (numero). 
# En otro caso devolver el n´umero original. 
# Analizar distintas formas de implementaci´on (usando un if-then-else, y 2 if, usando alguna opci´on de operaci´on logica), ¿todas funcionan?

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9_v1(numero: int) -> int:
    if es_multiplo_de(numero, 9):
        print (numero*3)
        return numero*3
    
    if es_multiplo_de(numero, 3):
        print (numero*2)
        return numero*2


    print (numero)
    return numero



def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9_v2(numero: int) -> int:
    if es_multiplo_de(numero, 9):
        print (numero*3)
        return numero*3
    
    if es_multiplo_de(numero, 3):
        print (numero*2)
        return numero*2


    print (numero)
    return numero


# 5.4 lindo nombre(nombre) que dado un nombre, si la longitud es igual o mayor a 5 devolver una frase que diga “Tu
# nombre tiene muchas letras!” y sino, “Tu nombre tiene menos de 5 caracteres”.

def lindo_nombre(nombre: str) -> str:
    limite_cantidad_letras = 5
    frase_nombre_largo = "Tu nombre tiene muchas letras!"
    frase_nombre_corto = "Tu nombre tiene menos de 5 caracteres"

    if (len(nombre) >= limite_cantidad_letras):
        print(frase_nombre_largo)
        return(frase_nombre_largo)
    
    print(frase_nombre_corto)
    return(frase_nombre_corto)

# 5.5 elRango(numero) que imprime por pantalla “Menor a 5” si el n´umero es menor a 5, “Entre 10 y 20” si el n´umero est´a
# en ese rango y “Mayor a 20” si el n´umero es mayor a 20

def el_rango(numero: int) -> int:
    rango_1 = 5
    rango_2 = 20

    if (numero < rango_1):
        print("Tu numero es menor a 5")
    if (numero < rango_2):
        print("Entre 10 y 20")
    else:
        print("Mayor a 20")


# 5.6 En Argentina una persona del sexo femenino se jubila a los 60 anos, mientras que aquellas del sexo masculino se jubilan
# a los 65 anos. Quienes son menores de 18 anos se deben ir de vacaciones junto al grupo que se jubila. Al resto de
# las personas se les ordena ir a trabajar. Implemente una funci´on que, dados los par´ametros de sexo (F o M) y edad,
# imprima la frase que corresponda seg´un el caso: “And´a de vacaciones” o “Te toca trabajar”.

def vacacionas_o_trabajas(sexo: str, edad: int) -> str:
    mayoria_de_edad = 18
    condicion_menor = edad < mayoria_de_edad
    condicion_mujer = edad >= 60 and sexo == "F"
    condicion_varon = edad >= 65 and sexo == "M"

    if (condicion_menor or condicion_mujer or condicion_varon):
        print("Anda de vacaciones")
    else:
        print("Te toca trabajar")    


#############
# Ejercicio 6
#############
# Implementar las siguientes funciones usando repetici´on condicional while:

# 1. Escribir una funci´on que imprima los n´umeros del 1 al 10.
def imprimir_1_a_10():
    contador = 1
    limite = 10
    while (contador <= limite):
        print(contador)
        contador+=1


# 2. Escribir una funci´on que imprima los n´umeros pares entre el 10 y el 40.
def imprimir_1_a_40():
    contador = 10
    limite = 40
    while (contador <= limite):
        print(contador)
        contador+=1

# 3. Escribir una funci´on que imprima la palabra “eco” 10 veces.
def imprimir_eco_10_veces():
    contador = 0
    limite = 10
    while (contador < limite):
        print("eco", contador+1)
        contador+=1


# 4. Escribir una funci´on de cuenta regresiva para lanzar un cohete. Dicha funci´on ir´a imprimiendo desde el n´umero que
# me pasan por par´ametro (que sera positivo) hasta el 1, y por ´ultimo “Despegue”.
def cuenta_regresiva(contador: int) -> None:
    limite = 1

    while (contador >= limite):
        print(contador)
        contador-=1
        
        
    print("Despegue")


# 6.5 Hacer una funcion que monitoree un viaje en el tiempo. 
# Dicha funcion recibe dos parametros, “el anio de partida” y “algun anio de llegada”, 
# siendo este ultimo parametro siempre mas chico que el primero. 
# El viaje se realizara de a saltos de un anio y la funcion debe mostrar el texto: 
# “Viajo un anio al pasado, estamos en el anio: <anio>” cada vez que se realice un salto de anio.

def viaje_en_el_tiempo(anio_partida: int, anio_llegada: int) -> str:
    while (anio_partida < anio_llegada):
        anio_llegada-=1
        print(f"Viajo un anio al pasado, estamos en el anio: {anio_llegada}")

# viaje_en_el_tiempo(300,320)


# 6.6 Implementar de nuevo la funci´on de monitoreo de viaje en el tiempo, pero desde el a˜no de partida hasta lo m´as cercano
# al 384 a.C., donde conoceremos a Arist´oteles. Y para que sea m´as r´apido el viaje, ¡vamos a viajar de a 20 a˜nos en cada salto!

def viaje_en_el_tiempo_aristoteles(anio_llegada: int) -> str:
    anio_partida = -384
    while (anio_partida < anio_llegada):
        anio_llegada-=20
        print(f"Viajo un anio al pasado, estamos en el anio: {anio_llegada}")

    print("Ya pudiste conocer a Aristoteles!")



#############
# Ejercicio 7
#############

# Implementar las funciones del ejercicio 6 utilizando for num in range(i,f,p):. Recordar que la funci´on
# range para generar una secuencia de n´umeros en un rango dado, con un valor inicial i, un valor final f y un paso p. Ver
# documentaci´on: https://docs.python.org/es/3/library/stdtypes.html#typesseq-range


# 7.1 Escribir una funci´on que imprima los numeros del 1 al 10.
def imprimir_1_a_10_rango():
    for num in range(1,11,1):
        print(num)
    
# 7.2 Escribir una funci´on que imprima los n´umeros pares entre el 10 y el 40.
def imprimir_1_a_40_rango():
    for num in range(10,41,1):
        print(num)

# 7.3 Escribir una funci´on que imprima la palabra “eco” 10 veces.
def imprimir_eco_10_veces_rango():
    for num in range(1,11,1):
        print(f"eco {num}")


# 7.4 Escribir una funci´on de cuenta regresiva para lanzar un cohete. Dicha funci´on ir´a imprimiendo desde el n´umero que
# me pasan por par´ametro (que sera positivo) hasta el 1, y por ´ultimo “Despegue”.
def cuenta_regresiva_rango(contador: int) -> None:
    for num in range(contador, 0, -1):
        print(num)

    print("Despegue")

# 7.5 Hacer una funcion que monitoree un viaje en el tiempo. 
# Dicha funcion recibe dos parametros, “el anio de partida” y “algun anio de llegada”, 
# siendo este ultimo parametro siempre mas chico que el primero. 
# El viaje se realizara de a saltos de un anio y la funcion debe mostrar el texto: 
# “Viajo un anio al pasado, estamos en el anio: <anio>” cada vez que se realice un salto de anio.

def viaje_en_el_tiempo_rango(anio_llegada: int, anio_partida: int, ) -> str:
    for num in range(anio_partida, anio_llegada, -1):
        print(f"Viajo un anio al pasado, estamos en el anio: {num-1}")

# viaje_en_el_tiempo_rango(-384, 0)


# 7.6 Implementar de nuevo la funci´on de monitoreo de viaje en el tiempo, pero desde el a˜no de partida hasta lo m´as cercano
# al 384 a.C., donde conoceremos a Arist´oteles. Y para que sea m´as r´apido el viaje, ¡vamos a viajar de a 20 a˜nos en cada salto!
def viaje_en_el_tiempo_aristoteles_rango(anio_partida: int) -> str:
    anio_llegada = -384
    step = -20
    for num in range(anio_partida, anio_llegada, step):
        print(f"Viajo un anio al pasado, estamos en el anio: {num}")

    print("Ya pudiste conocer a Aristoteles!")

# viaje_en_el_tiempo_aristoteles_rango(0)


#############
# Ejercicio 8
#############

# Ejercicio 8. Realizar la ejecucion simbolica de los siguientes codigos:
# 1. x=5 ; y=7; x = x + y
def uno():
    x=5
    y=7
    x = x + y # 12
    return x #12
# print(uno())


# 2. x=5 ; y=7 ; z=x+y; y = z * 2
def dos():
    x=5 
    y=7 
    z=x+y # 12
    y = z * 2 # 24
    return y # 24
# print(dos())

# 3. x=5 ; y=7 ; x="hora"; y = x * 2
def tres():
    x=5 
    y=7
    x="hora"
    y = x * 2 #"horahora"
    return y # horahora
# print(tres())

def tres_v2():
    x=5 
    y=7
    x="hora"
    # x *= 2 #"horahora"
    # x = x*2
    return x # horahora
# print(tres_v2())


# 4. x=False ; res=not(x)
def cuatro():
    x=False
    res=not(x)
    return res # True
# print(cuatro())

# 5. x=True ; y=False ; res=x and y; x = res and x
def cinco():
    x=False
    y=False
    res=x and y # False
    x = res and x #False
    return res # False
# print(cinco())




#############
# Ejercicio 9
#############

# Sea el siguiente codigo:
def rt(x: int, g: int) -> int:
    g = g + 1
    return x + g

g: int = 0

def ro(x: int) -> int:
    global g
    g = g + 1
    return x + g

# 1. ¿Cual es el resultado de evaluar tres veces seguidas ro(1)?
# ro(1) = 1 + 1 = 2
# ro(1) = 1 + 1 + 1 = 3
# ro(1) = 2 + 1 + 1 = 4

# 2. ¿Cu´al es el resultado de evaluar tres veces seguidas rt(1, 0)?
# rt(1,0) = 0 + 1 + 1 = 2
# rt(1,0) = 0 + 1 + 1 = 2
# rt(1,0) = 0 + 1 + 1 = 2

# 3. En cada funci´on, realizar la ejecuci´on simb´olica.
# 4. Dar la especificaci´on en lenguaje natural para cada funci´on, rt y ro.

