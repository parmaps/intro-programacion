import Distribution.Simple.Utils (xargs)
-------------
--Ejercicio 1
-------------

-- SOLUCION CHAT GPT
-- 1.1) longitud :: [t] -> Integer, que dada una lista devuelve su cantidad de elementos
longitud :: [t] -> Integer
longitud [] = 0
longitud (_:xs) = 1 + longitud xs
{-
    Este patrón se aplica cuando la lista tiene al menos un elemento. 
    Utilizamos _ para indicar que no nos importa el primer elemento de la lista (lo estamos descartando).

    xs es el resto de la lista, es decir, la lista sin su primer elemento.

    La función se define de manera recursiva. 
    Se suma 1 al resultado de aplicar longitud a la lista xs. 
    Esto significa que estamos contando un elemento más en la lista.
-}


{-
SOLUCION MIA
1.2
ultimo :: [t] -> t segun la siguiente especificacion:
problema ultimo (s: seq⟨T ⟩) : T {
    requiere: { |s| > 0 }
    asegura: { resultado = s[|s| − 1] }

-}

ultimo :: [t] -> t
ultimo [x] = x
ultimo (_:xs) = ultimo xs

{-
    En el primer patrón, ultimo [x] = x, se especifica que si la lista tiene solo un elemento ([x]), 
    entonces ese elemento es el último, y se devuelve.

    En el segundo patrón, ultimo (_:xs) = ultimo xs, se utiliza la desestructuración de la lista. 
    Ignoramos el primer elemento (_) y tomamos el resto de la lista (xs). 
    Luego, llamamos recursivamente a ultimo con la lista restante.
-}


{-
SOLUCION CHAT GPT
1.3
principio :: [t] -> [t] segun la siguiente especificacion:
problema principio (s: seq⟨T ⟩) : seq⟨T ⟩ {
    requiere: { |s| > 0 }
    asegura: { resultado = subseq(s, 0, |s| − 1) }
}

-} 

principio :: [t] -> [t]
principio [_] = [] --si hay un solo elemento, la lista es vacia
principio (x:xs) = x:principio xs --desestructuramos en primer elemento x y resto de lista xs, y armamos nueva lista con x y (eventualmnte) la lista menos el ultimo elemento

{-
    En el primer patrón principio [_] = [], especificamos que si la lista tiene solo un elemento (representado como [_]), 
    entonces el resultado es una lista vacía [], ya que no hay elementos restantes después del primero.

    En el segundo patrón principio (x:xs) = x : principio xs, 
    descomponemos la lista en un primer elemento x y el resto de la lista xs. 
    Construimos una nueva lista que comienza con x y luego llamamos recursivamente a principio con xs para obtener el principio del resto de la lista.
-}

{-
PLANTEO GENERAL MIO, MIRE SOLUCION RECURSIVA PORQUE NO UBICABA SINTAXIS (concatenacion de listas)
1.4
reverso :: [t] -> [t] segun la siguiente especificacion:
problema reverso (s: seq⟨T ⟩) : seq⟨T ⟩ {
    requiere: { True }
    asegura: { resultado tiene los mismos elementos que s pero en orden inverso.}
-}

reverso :: [t] -> [t] 
reverso [] = [] --lista vacia devuelve lista vacia
reverso (x:xs) = reverso xs ++ [x] --lista tiene al menos un elemento, construyo una nueva lista agregando x al final

--En este caso, se toma el primer elemento x y el resto de la lista xs. 
--Luego, se aplica recursivamente reverso a xs. 
--El resultado de esta recursión será la lista xs invertida. 
--Después, se concatena [x] al final, lo que coloca x al final de la lista invertida.



-- TEORIA concatenacion ++:
-- La operación de concatenación en Haskell se realiza utilizando el operador ++. 
-- Este operador toma dos listas y las une para formar una nueva lista 
-- que contiene todos los elementos de la primera lista seguidos de todos los elementos de la segunda lista.


-------------
--Ejercicio 2
-------------

{-
MIRE SOLUCION CLASE 7/9
2.1) pertenece :: (Eq t) => t -> [t] -> Bool segun la siguiente especificacion:
problema pertenece (e: T , s: seq⟨T ⟩) : B {
    requiere: { True }
    asegura: { resultado = true ↔ e ∈ s }

-}  

-- TEORIA  Eq
-- (Eq t) => es una restricción de tipo en Haskell que significa que el tipo t debe tener una instancia de la clase de tipo Eq. En otras palabras, t debe ser un tipo para el cual se puede definir la igualdad (mediante el uso del operador ==).
-- En resumen, (Eq t) => t -> [t] -> Bool especifica que t debe ser un tipo comparable (es decir, debe tener una instancia de Eq) y la función pertenece puede operar con elementos de este tipo y listas de elementos de este tipo

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False -- ningun elemento pertenece a una lista vacia
pertenece x (y:ys) = x == y || pertenece x ys -- compara el parametro con el primer elemento, si no son iguales sigue comparando recursivamente

-- con guardas:
-- pertenece x (y:ys) | x == y = True
            -- | otherwise = pertenece x ys


{-
OK SOLO
2.2) todosIguales :: (Eq t) => [t] -> Bool, 
que dada una lista devuelve verdadero sı y solamente si todos sus elementos son iguales
    
-}  

todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = False
todosIguales [_] = True
todosIguales (x:y:ys) =  x == y && todosIguales (x:ys)

{-
2.3) todosDistintos :: (Eq t) => [t] -> Bool segun la siguiente especificacion:
    problema todosDistintos (s: seq⟨T ⟩) : B {
        requiere: { True }
        asegura: { resultado = false ↔ existen dos posiciones distintas de s con igual valor }
    }
-} 

todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True -- porque no hay posiciones distintas de s
todosDistintos [_] = True -- porque hay una sola posicion en s (no hay posiciones distintas de s)
todosDistintos (x:y:ys) = x /= y && todosDistintos(x:ys) && todosDistintos(y:ys) -- comparo el primer elemento de la lista con el segundo, si en algun caso son iguales, todosDistintos es False; si no, sigo comparando el primer y el segundo elemento con el resto de la lista
--comparo el primer elemento de la lista con el segundo, si en algun caso son iguales, todosDistintos es False:
--todosDistintosMAL (x:y:ys) = x /= y && todosDistintos(x:ys) 

{-
2.4) hayRepetidos :: (Eq t) => [t] -> Bool segun la siguiente especificacion:
    problema hayRepetidos (s: seq⟨T ⟩) : B {
        requiere: { T rue }
        asegura: { resultado = true ↔ existen dos posiciones distintas de s con igual valor }
    }
-}

hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False -- no hay posiciones distintas de s
hayRepetidos [_] = False -- no hay posiciones distintas de s
hayRepetidos (x:y:ys) = x == y || (hayRepetidos(x:ys) || hayRepetidos(y:ys)) --misma logica que todosDistintos pero alreves

hayRepetidosPorNegacion :: (Eq t) => [t] -> Bool
hayRepetidosPorNegacion lista = not (todosDistintos lista)


{-
2.5) quitar :: (Eq t) => t -> [t] -> [t], que dados un entero x y una lista xs, elimina la primera aparicion de x en
la lista xs (de haberla).

-}
quitar :: (Eq t) => t -> [t] -> [t]
quitar x [] = [] --si la lista original es vacia devolver la lista vacia
quitar x (y:ys) | x == y = ys--si x coincide con el primer elemento, devolver la lista sin este
                | otherwise = y : quitar x ys --si no, volver a preguntar manteniendo el primer elemento de la lista

--Yo lo pense asi originalmente: 
-- | otherwise = quitar x ys 
-- el problema con esto era que faltaba mantener el elemento original
--LA IDEA CLAVE ES QUE COMPARA ELEMENTO A ELEMENTO, Y CADA COMPARACION PODES GUARDAR O NO EL ELEMENTO ORIGINAL
--QUE VA A SER LA HEAD (y) DE ESA LISTA (ys)


{-
2.6) quitarTodos :: (Eq t ) => t -> [t] -> [t], que dados un entero x y una lista xs, elimina todas las apariciones
de x en la lista xs (de haberlas). Es decir:
    problema quitarTodos (e: T , s: seq⟨T ⟩) : seq⟨T ⟩ {
        requiere: { T rue }
        asegura: { resultado es igual a s pero sin el elemento e
    }
-}

quitarTodos :: (Eq t ) => t -> [t] -> [t]
quitarTodos x [] = []
quitarTodos x (y:ys) | x == y = quitarTodos x ys --si x coincide con el primer elemento de la lista, sacarlo y volver a chequear
                     | otherwise = y : quitarTodos x ys --si no, volver a preguntar manteniendo el primer elemento de la lista


{-
2.7) eliminarRepetidos :: (Eq t) => [t] -> [t] 
que deja en la lista una única aparición de cada elemento, eliminando
las repeticiones adicionales.

-}
-- NOTA:-> ESTA IMPLEMENTACION DEJA LA ULTIMA APARICION DEL ELEMENTO -> BORRA DESDE EL PRINCIPIO
eliminarRepetidosBot :: (Eq t) => [t] -> [t]
eliminarRepetidosBot [] = [] 
eliminarRepetidosBot [x] = [x] --si hay un unico elementos, no hay repetidos -> lista permanece igual
eliminarRepetidosBot (x:xs) 
    | pertenece x xs = eliminarRepetidosBot xs --si x pertenece, sacarlo y volver a preguntar
    -- " Si x está en xs, significa que x es un elemento repetido, por lo que se omite en el resultado 
    -- y se llama recursivamente la función eliminarRepetidos con la lista xs restante para continuar la búsqueda de elementos repetidos."
    | otherwise = x : eliminarRepetidosBot xs --si x no pertenece, dejarlo y volver a preguntar
    -- no es un elemento repetido, por lo que se agrega a la lista resultante. 
    -- y se llama recursivamente la función eliminarRepetidos con la lista xs para continuar la búsqueda de elementos repetidos.




-- NOTA:-> ESTA IMPLEMENTACION APUNTA A BORRAR DESDE LA REPETICION, ES DECIR DEJANDO LA PRIMERA APARICION DEL ELEMENTO Y BORRANDO LAS SUBSIGUIENTES, 
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = [] 
eliminarRepetidos [x] = [x] --si hay un unico elementos, no hay repetidos -> lista permanece igual
eliminarRepetidos (x:y:ys)
    | x == y = eliminarRepetidos (y:ys) --si x igual y, saco x y vuelvo a preguntar
    | otherwise = x : eliminarRepetidos (y:ys)
    -- | otherwise = x : y : eliminarRepetidos ys -- si son distintos, conservar x (1ro) e y (2do) y volver a preguntar desde ys (lista sin 1er y 2do)
    -- | otherwise = x : eliminarRepetidos (y:ys)
                        --    | otherwise = x: eliminarRepetidos (x:ys)
                        --    | otherwise = x : eliminarRepetidos (y:ys) --si no son iguales, conservo x y vuelvo a preguntar desde y

{-
    -- pertenece x (y:ys) | x == y = True           --si x es igual a y (es decir, si el primer elemento es igual al segundo elemento) pertenece (porque existe x en ys)
    -- | otherwise = pertenece x ys     --si x no es igual a y, volver a preguntar pero sin y (o sea desde el segundo elemento de la lista)
-}

{-
2.8) mismosElementos :: (Eq t) => [t] -> [t] -> Bool, 
que dadas dos listas devuelve verdadero sı́ y solamente sı́
ambas listas contienen los mismos elementos, sin tener en cuenta repeticiones, es decir:

    problema mismosElementos (s: seq⟨T ⟩, r: seq⟨T ⟩) : B {
        requiere: { T rue }
        asegura: { resultado = true ↔ todo elemento de s pertenece r y viceversa}
    }

-}

-- lista1 :: (Eq t) => [t] -> [t]
-- let listaSinReps = eliminarRepetidos lista

mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos lista1 lista2 = elementosListaUnoEstanEnListaDos lista1 lista2 && elementosListaUnoEstanEnListaDos lista2 lista1 
-- mismosElementos [] [] = True
-- mismosElementos [] _ = False
-- mismosElementos _ [] = False
-- mismosElementos [x] list2 = pertenece x list2
-- mismosElementos (x:rest1) list2 
--     | pertenece x list2 && mismosElementos rest1 list2 = True
--     | otherwise = False


elementosListaUnoEstanEnListaDos :: (Eq t) => [t] -> [t] -> Bool
elementosListaUnoEstanEnListaDos [] [] = True
elementosListaUnoEstanEnListaDos [] _ = False
elementosListaUnoEstanEnListaDos _ [] = False
elementosListaUnoEstanEnListaDos [x] list2 = pertenece x list2
elementosListaUnoEstanEnListaDos (x:rest1) list2 
    | pertenece x list2 && elementosListaUnoEstanEnListaDos rest1 list2 = True
    | otherwise = False     

    -- | pertenece x (y:rest2) && pertenece y (x:rest) && mismosElementos rest1 (y:rest2) = True
-- mismosElementos (x:y:ys) ws | pertenece x ws && mismosElementos (y:ys) ws = True
-- mismosElementos (x:xs) ys | pertenece x ys && mismosElementos xs ys = True

-- mismosElementos (x:rest1) (y:rest2) | pertenece x (y:rest2) && pertenece y (x:rest1) && mismosElementos rest1 rest2 = True
 --no funca con [1,2] [2,1] porque 1 pertenece, y luego saca y (1er elem) que es 2 de la l2

-- mismosElementos (x:rest1) (y:rest2) | pertenece x (y:rest2) && pertenece y (x:rest1) && mismosElementos rest1 (y:rest2) = True
--corregi que DEVUELVA False con [1,2] [2,1] porque 1 pertenece, y luego saca y (1er elem) que es 2 de la l2; pero DEVUELVE INDEF
--call stack: pertenece 1 a [2,1] && pertenece 2 a [1,2] && mE [2] [2,1]

-- && mismosElementos xs ys = True

-- pertenece x ws: chequeo si el primer elemento (x) de la lista1 (ys) pertenece a la lista2 (ws)
-- si pertenece, vuelvo a preguntar (paso recursivo) desde el siguiente elemento (y) de la lista1 (ys) 



{-
2.9) capicua :: (Eq t) => [t] -> Bool según la siguiente especificación:
problema capicua (s: seq⟨T ⟩) : B {
requiere: { T rue }
asegura: { (resultado = true) ↔ (s = reverso(s)) }
}
Por ejemplo capicua [á’,’c’, ’b’, ’b’, ’c’, á’] es true , capicua [á’, ’c’, ’b’, ’d’, á’] es false


4. reverso :: [t] -> [t] según la siguiente especificación:
    problema reverso (s: seq⟨T ⟩) : seq⟨T ⟩ {
        requiere: { True }
        asegura: { resultado tiene los mismos elementos que s pero en orden inverso.}
    }

-}

capicua :: (Eq t) => [t] -> Bool
capicua [] = True
capicua [x] = True
capicua list = list == reversoAgain list



reversoAgain :: [t] -> [t] 
reversoAgain [] = []
reversoAgain [x] = [x]
reversoAgain (x:xs) = reversoAgain xs ++ [x]


------------------------------------------------------------------------
--Ejercicio 3: Definir las siguientes funciones sobre listas de enteros:
------------------------------------------------------------------------

{-
3.1) sumatoria :: [Integer] -> Integer según la siguiente especificación:
    problema sumatoria (s: seq⟨Z⟩) : Z {
        requiere: { T rue }
        asegura: { resultado = SUM d: i=0 h: |s|−1 s[i] }
        asegura: { resultado = es la sumatoria desde i=0 hasta h=cantidad de elementos de la lista -1 de cada elemento de la lista en la posicion i }
        }
-}

sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria [num] = num
sumatoria (num:rest) = num + sumatoria rest

{-
3.2) productoria :: [Integer] -> Integer según la siguiente especificación:
    problema productoria (s: seq⟨Z⟩) : Z {
        requiere: { T rue }
        asegura: { resultado = PROD d: i=0 h: |s|−1 s[i] }
        asegura: { resultado = es la productoria desde i=0 hasta h=cantidad de elementos de la lista -1 de cada elemento de la lista en la posicion i }
-}

productoria :: [Integer] -> Integer
productoria [] = 1
productoria [num] = num
productoria (num:rest) = num * productoria rest

{-
3.3)
maximo :: [Integer] -> Integer según la siguiente especificación:
    problema maximo (s: seq⟨Z⟩) : Z {
        requiere: { |s| > 0 }
        asegura: { resultado ∈ s ∧ todo elemento de s es menor o igual a resultado }
    }
-}

maximoMal :: [Integer] -> Integer 
maximoMal [num] = num
maximoMal (num:siguiente:rest) 
    | num > siguiente = num 
    | otherwise = maximoMal (siguiente:rest) 

maximoBien :: [Integer] -> Integer 
maximoBien [num] = num
maximoBien (num:siguiente:rest) 
    | num > siguiente = maximoBien (num:rest)
    | otherwise = maximoBien (siguiente:rest) 


{-
3.4. sumarN :: Integer -> [Integer] -> [Integer] según la siguiente especificación:
    problema sumarN (n: Z, s: seq⟨Z⟩) : seq⟨Z⟩ {
        requiere: { True }
        asegura: {|resultado| = |s| ∧ cada posición de resultado contiene el valor que hay en esa posición en s sumado n}
        asegura: {resultado = cada elemento de s sumado n en esa posicion}
    }
-}

sumarN :: Integer -> [Integer] -> [Integer]
sumarN n [] = []
sumarN n [x] = [x+n]
sumarN n (x:xs) = x+n:sumarN n xs


{-
3.5. sumarElPrimero :: [Integer] -> [Integer] según la siguiente especificación:
    problema sumarElPrimero (s: seq⟨Z⟩) : seq⟨Z⟩ {
        requiere: { |s| > 0 }
        asegura: {resultado = sumarN (s[0], s) }
        asegura: {suma a cada elemento de s el primer numero usando sumarN }
    }
Por ejemplo sumarElPrimero [1,2,3] da [2,3,4]
-}

sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero [x] = sumarN x [x]
sumarElPrimero (x:xs) = sumarN x (x:xs)
-- sumarElPrimero (x:xs) = sumarN x xs ++ sumarElPrimero xs

{-
3.6sumarElUltimo :: [Integer] -> [Integer] según la siguiente especificación:
    problema sumarElUltimo (s: seq⟨Z⟩) : seq⟨Z⟩ {
        requiere: { |s| > 0 }
        asegura: {resultado = sumarN (s[|s| − 1], s) }
    }
Por ejemplo sumarElUltimo [1,2,3] da [4,5,6]
-}


sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo [x] = sumarN x [x]
sumarElUltimo (x:xs) = sumarN (head (reversoAgain (x:xs))) (x:xs) 
--llamo a sumarN con los siguientes parametros
-- n: el primer el elemento de la lista parametro (x:xs) revertida (para obtener el ultimo elemento de la lista original)
-- lista: la lista original


{-
3.7) pares :: [Integer] -> [Integer] según la siguiente especificación:
    problema pares (s: seq⟨Z⟩) : seq⟨Z⟩ {
        requiere: { T rue }
        asegura: {resultado sólo tiene los elementos pares de s en el orden dado, respetando las repeticiones}
    }
    Por ejemplo pares [1,2,3,5,8,2] da [2,8,2]
-}

pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs) 
    | even x = x: pares xs
    | otherwise = pares xs


{-
3.8) multiplosDeN :: Integer -> [Integer] -> [Integer] 
que dado un número n y una lista xs, devuelve una lista
con los elementos de xs múltiplos de n.
-}        

multiplosDeN :: Integer -> [Integer] -> [Integer] 
multiplosDeN _ [] = []
multiplosDeN 0 xs = [0]
multiplosDeN n (x:xs) 
    | x `mod` n == 0 = x: multiplosDeN n xs
    | otherwise = multiplosDeN n xs


{-
3.9) ordenar :: [Integer] -> [Integer] que ordena los elementos de la lista en forma creciente.
-}

-- ordenar :: [Integer] -> [Integer]
-- ordenar [] = []
-- ordenar [x] = [x]
-- ordenar (x:xs) = intercambiar x (ordenar xs)


-- -- ordenar [x,y] 
-- --     | x < y = [x,y]
-- --     | otherwise = intercambiar [x,y]
-- -- ordenar (x:y:ys)
-- --     | x < y = ordenar (x:y:ys) -- si x es menor que y, no intercambiar y preguntar por el siguiente elemento
-- --     | otherwise = ordenar (intercambiar ys)

-- ordenar :: [Integer] -> [Integer]
-- ordenar [] = []
-- ordenar [x] = [x]
-- ordenar (x:xs) = intercambiar x (ordenar xs) ++ xs

-- intercambiar :: Integer -> [Integer] -> [Integer]
-- intercambiar x [] = [x] -- caso: ultimo intercambio
-- intercambiar x (y:ys) 
--     | x < y = intercambiar x ys -- si x es menor que y, no intercambiar y volver a comparar x con el resto de la lista
--     | otherwise = intercambiar y (x:ys) -- si x > y, intercambiar y vuelvo a preguntar


-- -- intercambiar [x,y] 
-- --     | x < y = [x,y]
-- --     | otherwise = [y,x]
-- intercambiar x (y:ys) 
--     | x < y = intercambiar y ys -- si x es menor que y, no intercambiar y preguntar por el siguiente elemento
--     | otherwise = y:x:ys -- si x > y, intercambiar y preguntar por el siguiente elemento


--Ordenar:
--0) Inicializar lista vacia como lista ordenada
--A) Buscar el menor -> minimo
--B) Quitarlo de la lista original -> quitar
--C) Ponerlo al final de una nueva lista ordenada -> insertarUltimo
--D) Repetir con la lista original
--E) Devolver toda la lista ordenada


--A)
minimo :: [Integer] -> Integer 
minimo [num] = num
minimo (num:siguiente:rest) 
    | num < siguiente = minimo (num:rest)
    | otherwise = minimo (siguiente:rest) 

--B) quitar

--C)
insertarUltimo :: Integer -> [Integer] -> [Integer]
-- insertarUltimo x [] = [x]
insertarUltimo x listaOrdenada = listaOrdenada ++ [x]
-- insertar el elemento quitado (x) de la lista original (xs) al final de la lista ordenada

ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar [x] = [x]
ordenar (x:xs) = procesarLista (x:xs) []

procesarLista :: [Integer] -> [Integer] -> [Integer]
procesarLista [] listaOrdenada = listaOrdenada
procesarLista (x:xs) listaOrdenada = procesarLista (quitar (minimo (x:xs)) (x:xs)) (listaOrdenada ++ [minimo (x:xs)])

-- ordenar [x] = [x]
-- procesarLista (x:xs) 
    -- | longitud (procesarLista (quitar (minimo (x:xs)) (x:xs)) ) > 0 = insertarUltimo (minimo (x:xs)) listaOrdenada
    -- | otherwise = listaOrdenada

--procesar lista toma una lista de entrada
--en cada iteracion le saca el numero minimo, hasta que llega a []
--FALTARIA agregar ese minimo a la lista ordenada (cuando procesar lista es [], devolver listaOrdenada)

-- ordenar :: [Integer] -> [Integer]
-- ordenar [] = listaOrdenada
-- ordenar (x:xs) = procesarLista (x:xs)
-- ordenar [x] = [x]

-- ordenar (x:xs) = minimo (x:xs):xs
-- ordenar (x:xs) 
--     -- | longitud (ordenar (quitar (minimo xs) xs)) == 0 = listaOrdenada
--     | longitud xs > 0 = let minVal in ordenar (quitar (minimo xs) xs)
--     -- | otherwise = insertarUltimo (minimo xs) listaOrdenada
--     | longitud xs == 0 = listaOrdenada
    -- | otherwise = ordenar (quitar (minimo xs) xs)



--------------------------------------------------------------------------
--Ejercicio 4: Definir las siguientes funciones sobre listas de caracteres, 
-- interpretando una palabra como una secuencia de caracteres sin blancos
--------------------------------------------------------------------------
{-
4.1) sacarBlancosRepetidos :: [Char] -> [Char], que reemplaza cada subsecuencia de blancos contiguos de la primera
lista por un solo blanco en la lista resultado.
-}

sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos [x] = [x]
sacarBlancosRepetidos (x:y:ys) 
    | x == y && x == ' ' = sacarBlancosRepetidos (y:ys) -- si 1ro == 2do y es whitespace, volver a preguntar desde 2do (sacando primero)
    | otherwise = x: sacarBlancosRepetidos (y:ys) --si no, mantene primero y volve a preguntar desde 2do


{-
4.2) contarPalabras :: [Char] -> Integer, que dada una lista de caracteres devuelve la cantidad de palabras que tiene.

-> contar whitespaces
-}
contarPalabras :: [Char] -> Integer
contarPalabras [] = 0
contarPalabras xs = 1 + contarEspacios (quitarEspaciosEnExtremos (sacarBlancosRepetidos xs))


contarEspacios :: [Char] -> Integer
contarEspacios [] = 0
contarEspacios (x:xs) 
    | x == ' ' = 1 + contarEspacios xs
    | otherwise = contarEspacios xs 

testear :: [Char] -> [Char]
testear [] = []
testear xs = quitarEspaciosEnExtremos (sacarBlancosRepetidos xs)
    

quitarEspaciosEnExtremos :: [Char] -> [Char]
quitarEspaciosEnExtremos [] = []
quitarEspaciosEnExtremos [x] 
    | x == ' ' = []
    | otherwise = [x]
quitarEspaciosEnExtremos (x:xs)
    | x == ' ' && last xs == ' ' = quitarUltimo xs
    | x == ' ' = xs
    | last xs == ' ' = quitarUltimo (x:xs)
    | otherwise = x : xs


quitarUltimo :: [Char] -> [Char]
quitarUltimo [] = []
quitarUltimo [x] = []
quitarUltimo (x:xs) = x : quitarUltimo xs


{-
4.3) palabras :: [Char] -> [[Char]], que dada una lista arma una nueva lista con las palabras de la lista original.

-}

palabras :: [Char] -> [[Char]]
palabras xs = armarListaPalabras (quitarEspaciosEnExtremos (sacarBlancosRepetidos xs))


primerPalabra :: [Char] -> [Char]
primerPalabra [] = []
primerPalabra [' '] = []
primerPalabra [x] = [x]
primerPalabra (x:' ':ys) = [x] -- si el segundo elemento es WS, devolve una lista con el primer elemento
primerPalabra (x:y:ys) = x : primerPalabra (y:ys) --si hay al menos dos elementos, mantene el primero y pregunta el siguiente


armarListaPalabras :: [Char] -> [[Char]]
armarListaPalabras [] = []
armarListaPalabras xs = primerPalabra xs : armarListaPalabras (sacarPrefijo (primerPalabra xs) xs)
--en una nueva lista guardo la primera palabra, la saco de la lista original y repito (guardo la nueva primera, la saco, etc.)
--como?
--armar una nueva lista 
--primer elemento: primer palabra de xs
--resto: volver a aplicar funcion a la lista xs desde la segunda palabra (sin la primera palabra y el espacio)


-- arg 1: prefijo a sacar, arg 2: frase original
sacarPrefijo :: [Char] -> [Char] -> [Char]
sacarPrefijo [] [] = []
sacarPrefijo [] (y:ys) 
    | y == ' ' = ys --remover primer caracter por ser vacio
    | otherwise = y:ys --dejar palabra con primer caracter
sacarPrefijo (x:xs) (y:ys) 
    | x == y = sacarPrefijo xs ys --si coinciden los caracteres, removerlos de ambas y volver a preguntar
    | y == ' ' = ys --si y es vacio, devolver el resto de la lista
    | otherwise = y:ys --si no coinciden e y no es vacio, devolver la lista con y adelante



palabraMasLarga :: [Char] -> [Char]
palabraMasLarga [] = []
palabraMasLarga [x] = [x]
palabraMasLarga xs 
    | longitud (primerPalabra xs) >= longitud (palabraMasLarga listaSinPrimerPalabra) = primerPalabra palabraLimpia --si el largo de la primer palabra es mayor al largo de todas las otras palabras, devolver la primer palabra
    | otherwise = palabraMasLarga listaSinPrimerPalabra --si no, volver a preguntar desde la segunda palabra
    where
        palabraLimpia = quitarEspaciosEnExtremos (sacarBlancosRepetidos xs)
        listaSinPrimerPalabra = sacarPrefijo (primerPalabra xs) xs


-- palabraMasLarga "hola como andas" -> "andas"
-- palabraMasLarga "hola como andas lince" -> "andas"
-- palabraMasLarga "hola lince como andas" -> "lince"
-- palabraMasLarga "hola como andas linceh" -> "linceh"
-- palabraMasLarga "hola andas1 como andas2" -> "andas1"
-- palabraMasLarga "hola subacuaticass como  andas lince de las praderas subacuaticas" -> "praderas"


