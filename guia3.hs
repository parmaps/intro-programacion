--------------
-- Ejercicio 1
--------------
-- a

partialFunctionFTwo x | x == 1 = 8
                      | x == 4 = 131
                      | x == 16 = 16

-- b
f 1 = 8
f 4 = 131
f 16 = 16

--b)
g 8 = 16
g 16 = 4
g 131 = 1 

--c)
-- f o g
h x = f (g x)
-- h 8 = f (g 8)


--------------
-- Ejercicio 2
--------------

{-
a)
    problema absoluto (n: Z) : Z {
        requiere: {True}
        asegura:  {res es > 0}
        asegura:  {res es |n|}
    }
-}
absoluto :: Integer -> Integer
--absoluto x = abs x
absoluto x | x > 0 = x
           | x < 0 = -x
           | x == 0 = 0

absoluto2 :: Integer -> Integer
absoluto2 x | x >= 0 = x
            | x < 0 = -x

absoluto3 :: Integer -> Integer
absoluto3 x | x > 0 = x
            | x < 0 = -x
            | otherwise = 0

{- 
b) 
    problema maximoabsoluto (n, m: Z) : Z {
        requiere: {True}
        asegura: {res es igual a n o m} => {(res = n) ∨ (res = m)}
        asegura: {res es mayor o igual a n o a m} => {(res >= n) ∧ (res >= m)}
    }
-}
maximoabsoluto :: Integer -> Integer -> Integer
maximoabsoluto x y = if absoluto x > absoluto y 
                        then absoluto x
                        else absoluto y

-- pattern matching:
maximoabsolutoDos :: Integer -> Integer -> Integer 
maximoabsolutoDos x y | absoluto2 x > absoluto2 y = absoluto2 x
                      | absoluto2 x < absoluto2 y = absoluto2 y       

maximoabsolutoDos2 :: Integer -> Integer -> Integer 
maximoabsolutoDos2 x y | absoluto x > absoluto y = absoluto x
                       | otherwise = absoluto y               

{- 

c) 
    problema maximo3 (x, y, z: Z) : Z {
        requiere: {True}
        asegura: {res es igual a x, a y o a z} => {(res = x) ∨ (res = y) ∨ (res = z)}
        asegura: {res es mayor o igual a x, a y & a z} => {(res >= x) ∧ (res >= y) ∧ (res >= y)}
    }
-}
--maximo3:: Integer -> Integer


maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 x y z | x >= y && x >= z = x
              | y >= x && y >= z = y
              | otherwise = z


{-

d)
!!! ver como expresar rationals en signatura, y como hacerlo para pattern matching
    problema algunoEs0 (x/a, y/b: Q) : Bool {
        requiere: {a != 0 ∧ b != 0}
        asegura: { res es True si x = 0 v y = 0}
    }
    algunoEs0Guardas :: (Integral a) => Ratio a -> (Integral a) => Ratio a -> (Integral a) => Ratio a

-}

algunoEs0Guardas  x a y b | x/a == 0 || y/b == 0 = True
                    | otherwise = False

algunoEs0Pattern 0 x = True
algunoEs0Pattern x 0 = True
algunoEs0Pattern x y = False

{-

e) 
!!! ver como expresar rationals
problema ambosSon0 (x/a, y/b: Q) : Bool {
    requiere: {a != 0 ∧ b != 0}
    asegura { res es True si x = 0 ∧ y = 0}
}
-} 
ambosSon0Guardas x a y b | x/a == 0 && y/b == 0 = True
                    | otherwise = False

ambosSon0Pattern 0 0 = True
ambosSon0Pattern x y = False

ambosSon0Pattern2 x y = x == 0 && y == 0


{- 
f) 
!!! refactor this
problema mismoIntervalo (x, y: R) : True {
    requiere: {True}
    asegura: {res es True si (x <= 3 ∧ y <= 3) ∨ ((3 < x <= 7) ∧ (3 < y <= 7)) ∨ (x > 7 ∧ y > 7 )   }
    (vale decirlo asi? ->) 
    asegura: {res es True si (x,y <= 3) ∨ (3 < x,y <= 7) ∨ (x,y > 7)}
}

-}

mismoIntervalo :: Float -> Float -> Bool
mismoIntervalo x y | x <= 3 && y <= 3 = True
                   | x > 3 && x <= 7 && y > 3 && y <= 7 = True 
                   | x > 7 && y > 7 = True
                    | otherwise = False

{-
g) 
sumaDistintos: que dados tres números enteros calcule la suma sin sumar repetidos (si los hubiera).

Esto tiene (al menos) dos interpretaciones posibles:
1) ▶ Cuando hay algún número repetido no lo sumo
▶ sumaDistintos(1,1,2) = 2
2) ▶ Cuando hay algún número repetido lo sumo una sola vez
▶ sumaDistintos(1,1,2) = 3

Una especificación semi-formal de la primera opcion
problema sumaDistintos (x,y,z: Z) : Z {
requiere: { - }
asegura: {si los 3 paŕametros son distintos entonces res = x + y + z}
asegura: {si 2 parámetros son iguales, res es igual al no repetido}
asegura: {si los 3 parámetros son iguales, res = 0}
}

Una especificación formal de la primera opcion
problema sumaDistintos (x, y, z: Z) : Z {
    requiere: {True}   
    asegura: {(x /= y) ∧ (x /= z) ∧ (y /= z)) -> res = x + y + z}
    asegura: {(x /= y) ∧ (x == z) -> res = y }
    asegura: {(x == y) ∧ (x /= z) -> res = z }
    asegura: {(x /= y) ∧ (y == z) -> res = x }
    asegura: {(x == y) ∧ (x == z) -> res = 0}

}
-}

sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos x y z | x /= y && x /= z && y /= z = x + y + z
                    | x /= y && x == z = y
                    | x /= z && x == y = z
                    | x /= y && y == z = x
                    | otherwise = 0    


{-
h)
esMultiploDe: dados dos números naturales, decidir si el primero es múltiplo del segundo

problema esMultiploDe (x, y: Z) : Bool {
    requiere {True}
    asegura {y mod x == 0 -> True}
    asegura {otherwise False}
}
-}
esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe x y | (x `mod` y) == 0 = True
                 | otherwise = False

{-
i) digitoUnidades: dado un número natural, extrae su dı́gito de las unidades.

problema digitoUnidades (x: Z) : Z {
    requiere {True}
    asegura {x < 10 -> res = x}
    asegura: { result es el último dı́gito de x}
    asegura {otherwise -> res = x `mod` 10}
}

Ejemplos
digitoUnidades 1 = 1
digitoUnidades 10 = 0
digitoUnidades 123 = 3

-}
digitoUnidades :: Integer -> Integer
digitoUnidades x | x < 10 = x
                 | otherwise =  x `mod` 10 


{-
j) digitoDecenas: dado un número natural, extrae su dı́gito de las decenas.
problema digitoDecenas (x: Z) : Z {
    requiere {x >= 10}
    asegura: { result es el dı́gito de x correspondiente a las decenas}
    asegura { res es el resto de la division entera entre 10 y el cociente de la division entera de x y 10 }
    asegura { res = (x `div` 10) `mod` 10 }

}

-}

digitoDecenas :: Integer -> Integer
digitoDecenas x = (x `div` 10) `mod` 10



{-
REPASO 4/9
TODO! VER LOS ERRORES DE HASKELL EN CHATGPT PARA ENTENDERLOS
Errores: resolver de arriba para abajo
GHCI: puedo usar :r en la linea de comando para recargar el programa
Consejo: armar un par de ejemplos antes de programar una solucion (como para Testing)

Tuplas: se puede usar fst y snd para obtener el primer y el segundo elemento respectivamente
-> tuplas x y | fst x < snd y = True
              | otherwise = False

Tipos genericos/arbitrarios: se suele usar a, b, c...por convencion
crearPar :: a -> b -> (a, b)
crearPar x y = (x, y)

-}

--------------
-- Ejercicio 3
--------------

{-
Implementar una función estanRelacionados :: Integer ->Integer ->Bool
problema estanRelacionados (a:Z, b:Z) : Bool {
    requiere: {a /= 0 ∧ b /= 0}
    asegura: {(res = true) ↔ a ∗ a + a ∗ b ∗ k = 0 para algún k ∈ Z con k /= 0)}
}

Despejo k 
 a ∗ a + a ∗ b ∗ k = 0 ↔ k = (-a*a)/(a*b) ↔ k = (-a/b)
 Debo usar `div` para especificar que a/b refiere a division entera -> a `div` b
 y `mod` para asegurarme que sea una division entera de resto 0 (es decir que a es divisible por b)

Por ejemplo:
estanRelacionados 8 2 -> True (porque existe un k = −4 tal que 82 + 8 × 2 × (−4) = 0)
estanRelacionados 7 3 -> False (porque no existe un k entero tal que 72 + 7 × 3 × k = 0)
-}

estanRelacionados :: Integer -> Integer -> Bool
-- estanRelacionados a b | a ∗ a + a ∗ b ∗ k = 0
estanRelacionados a b | a * a + a * b * ((-a) `div` b) == 0 && ((-a) `mod` b == 0) = True
                      | otherwise = False


--------------
-- Ejercicio 4
--------------

{-
a) prodInt: calcula el producto interno entre dos tuplas R × R.
Def producto interno
(a, b) · (c, d) = (a * c) + (b * d)
Ejemplos
prodInt (1, 2) (3, 4) = (1 * 3) + (2 * 4) = 3 + 8 = 11 
prodInt (7, 5) (2, 6) = (7 * 2) + (5 * 6) = 14 + 30 = 44 

problema prodInt (t1, t2: R × R) : R {
    requiere = {}
    asegura = {}

} 

-}

prodInt :: (Float, Float) -> (Float, Float) -> Float
prodInt t s = fst t * fst s + snd t * snd s

{-
b) todoMenor: dadas dos tuplas R × R, decide si es cierto que cada coordenada de la primera tupla es menor a la coordenada
correspondiente de la segunda tupla.

problema todoMenor (t1, t2: R) : Bool {
    requiere {True}
    asegura { -> res = True ↔ (primer elemento de t1 < primer elemento de t2) && 
              (segundo elemento de t1 < segundo elemento de t2)}

    /// solucion:
    asegura: { result = true ↔ la primera componente de t1 es
            menor que la primera componente de t2, y la segunda
            componente de t1 es menor que la segunda componente
            de t2}
}

Ejs.
todoMenor (1, 2) (3, 4) -> True
todoMenor (3, 4) (1, 2) -> False
todoMenor (1, 4) (3, 2) -> False

-}

todoMenor :: (Float, Float) -> (Float, Float) -> Bool
todoMenor t1 t2 = fst t1 < fst t2 && snd t1 < snd t2

{-
    c) distanciaPuntos: calcula la distancia entre dos puntos de R2 .

    problema distanciaPuntos (t1, t2: R) : R {
        asegura: {True}
        requiere: {res = √((fst t2 - fst t1)^2 + (snd t2 - snd t1)^2)}
    }
-}

distanciaPuntos :: (Float, Float) -> (Float, Float) -> Float
distanciaPuntos t1 t2 = sqrt ((fst t2 - fst t1)^2 + (snd t2 - snd t1)^2)

{-
d) sumaTerna: dada una terna de enteros, calcula la suma de sus tres elementos.

problema sumaTerna(t: Z×Z×Z) : Z {
    requiere: {True}
    asegura: {res = a + b + c}
}
-}

sumaTerna :: (Integer, Integer, Integer) -> Integer
sumaTerna (a, b, c) = a + b + c 

{-
e) sumarSoloMultiplos: dada una terna de números enteros y un natural, calcula la suma de los elementos de la terna que
son múltiplos del número natural. Por ejemplo:
sumarSoloMultiplos (10,-8,-5) 2 ->2
sumarSoloMultiplos (66,21,4) 5  ->0
sumarSoloMultiplos (-30,2,12) 3 ->-18

problema sumarSoloMultiplos ((t: Z×Z×Z) n: N) : Z {
    requiere: {n > 0}
    asegura: {cada componente de t se suma a resultado ↔ es multiplo de n}
    asegura: {resultado es la suma de los parametros x que cumplen (x `mod` n == 0)}
}
-}

esMultiplo :: Integer -> Integer -> Bool
esMultiplo x y = x `mod` y == 0

sumarSoloMultiplos :: (Integer, Integer, Integer) -> Integer -> Integer 
-- sumarSoloMultiplos (a, b, c) n | (a `mod` n == 0) &&  (b `mod` n == 0) && (c `mod` n == 0) = a + b + c 
sumarSoloMultiplos (a, b, c) n | esMultiplo a n &&  esMultiplo b n && esMultiplo c n = a + b + c
                               | esMultiplo a n && esMultiplo b n = a + b
                               | esMultiplo a n && esMultiplo c n = a + c
                               | esMultiplo b n && esMultiplo c n = b + c
                               | otherwise = 0


{-
f) posPrimerPar: dada una terna de enteros, devuelve la posición del primer número par si es que hay alguno, y devuelve
4 si son todos impares

problema posPrimerPar (t: Z×Z×Z) : Z {
    requiere: {True}
    asegura: {res es la posicion del primer numero par ↔ existe un numero par}
    asegura: {otherwise -> res = 4 }

    -- solucion mas precisa:
    asegura: {si algun elemento es par, entonces res es un valor
        entre 1 y 3 (inclusive), y es la posición del primer elemento par}
    }
-}

posPrimerPar :: (Integer, Integer, Integer) -> Integer
posPrimerPar (a, b, c) | even a = 1
                       | even b = 2
                       | even c = 3
                       | otherwise = 4


{-
g) crearPar :: a ->b ->(a, b): crea un par a partir de sus dos componentes dadas por separado (debe funcionar para
elementos de cualquier tipo)

problema crearPar (a, b) : (a,b) {
    requiere: {True}
    asegura: {res es una tupla cuyo primer elemento es a y es de tipo a y su segundo elemento es b y es de tipo b}
    asegura: {res = t, con fst t = a y snd t = b}
}

-}

crearPar :: a -> b -> (a, b)
crearPar x y = (x, y)

{-
invertir :: (a, b) ->(b, a): invierte los elementos del par pasado como parámetro (debe funcionar para elementos
de cualquier tipo)

problema invertirPar (a, b) : (b,a) {
    requiere: {True}
     asegura: {res es una tupla cuyo primer elemento es b y es de tipo b y su segundo elemento es a y es de tipo a}
     asegura: {res = t, con fst t = b y snd t = a}
}
-}

invertirPar :: a -> b -> (b, a)
invertirPar x y = (y, x)


--------------
-- Ejercicio 5
--------------

{-
Implementar la función todosMenores :: (Integer, Integer, Integer) ->Bool
    problema todosMenores ((n1 ,n2 ,n3 ) : Z × Z × Z) : Bool {
        requiere: {T rue}
        asegura: {(res = true) ↔ ((f (n1 ) > g(n1 )) ∧ (f (n2 ) > g(n2 )) ∧ (f (n3 ) > g(n3 ))))}
    }

    problema tmF (n: Z) : Z {
        requiere: {T rue}
        asegura: {(n ≤ 7 → res = n2 ) ∧ (n > 7 → res = 2n − 1)}
    }

    problema tmG (n: Z) : Z {
        requiere: {T rue}
        asegura: {Si n es un número par, entonces res = n/2, en caso contrario, res = 3n + 1}
    }
-}

todosMenores :: (Integer, Integer, Integer) -> Bool
todosMenores (n1,n2,n3) 
    | tmF n1 > tmG n1 && tmF n2 > tmG n2 && tmF n3 > tmG n3 = True
    | otherwise = False


tmF :: Integer -> Integer
tmF n 
    | n <= 7 = n*n
    | otherwise = 2*n-1


tmG :: Integer -> Integer
tmG n 
    | even n = n `div` 2
    | otherwise = 3*n + 1


--------------
-- Ejercicio 6
--------------

{-
Programar una función bisiesto :: Integer ->Bool según la siguiente especificación:

    problema bisiesto (año: Z) : Bool {
        requiere: {T rue}
        asegura: {res = f alse ↔ año no es múltiplo de 4 o año es múltiplo de 100 pero no de 400}
    }

Por ejemplo:
bisiesto 1901 -> False
bisiesto 1900 -> False
bisiesto 1904 -> True
bisiesto 2000 -> True
-}

bisiestoPorNegacion :: Integer -> Bool
bisiestoPorNegacion n 
    | n `mod` 4 /= 0 || (n `mod` 100 == 0 && n `mod` 400 /= 0) = False
    | otherwise = True

bisiesto :: Integer -> Bool
bisiesto n 
    | n `mod` 100 == 0 && n `mod` 400 /= 0 = False
    | n `mod` 4 == 0 = True
    | otherwise = False


--------------
-- Ejercicio 8
--------------

{-
Ejercicio 8. Implementar una función comparar :: Integer ->Integer ->Integer
    problema comparar (a:Z, b:Z) : Z {
        requiere: {T rue}
        asegura: {(res = 1 ↔ sumaU ltimosDosDigitos(a) < sumaU ltimosDosDigitos(b))}
        asegura: {(res = −1 ↔ sumaU ltimosDosDigitos(a) > sumaU ltimosDosDigitos(b))}
        asegura: {(res = 0 ↔ sumaU ltimosDosDigitos(a) = sumaU ltimosDosDigitos(b)))}
    }

    problema sumaUltimosDosDigitos (x: Z) : Z {
        requiere: {T rue}
        asegura: {res = (x mód 10) + (b(x/10)c mód 10)}
    }

Por ejemplo:
comparar 45 312: -1 porque 312 ≺ 45 y 1 + 2 < 4 + 5.
comparar 2312 7: 1 porque 2312 ≺ 7 y 1 + 2 < 0 + 7.
comparar 45 172: 0 porque no vale 45 ≺ 172 ni tampoco 172 ≺ 45.

-}

comparar :: Integer -> Integer -> Integer
comparar x y 
    | sumaUltimosDosDigitos x < sumaUltimosDosDigitos y = 1
    | sumaUltimosDosDigitos x > sumaUltimosDosDigitos y = -1
    | sumaUltimosDosDigitos x == sumaUltimosDosDigitos y = 0


sumaUltimosDosDigitos :: Integer -> Integer
sumaUltimosDosDigitos x = x `mod` 10 + (x `div` 10) `mod` 10


--------------
-- Ejercicio 9
--------------

{-
A partir de las siguientes implementaciones en Haskell, 
describir en lenguaje natural qué hacen y especificarlas semiformalmente.
-}

-- a) f1 :: Float -> Float
-- f1 n | n == 0 = 1
-- | otherwise = 0d) f4 :: Float -> Float -> Float
-- f4 x y = ( x + y )/2
-- Toma un numero n de tipo Float como argumento, si n es 0 devuelve 1, si no devuelve 0
--requiere {True}
--asegura {res = 1 <-> n es 0, si no res = 0 }


-- b) f2 :: Float -> Float
-- f2 n | n == 1 = 15
-- | n == -1 = -15e) f5 :: ( Float , Float ) -> Float
-- f5 (x , y ) = ( x + y )/2
-- Toma un numero n de tipo Float como argumento: 
--  si n es 1 devuelve 15
--  si n es -1 devuelve -15
--requiere {True}
--asegura {res = 15 <-> n es 1 y  res = -15 <-> n es -1}


-- c) 
f3 :: Float -> Float
f3 n 
    | n <= 9 = 7
    | n >= 3 = 5
-- Toma un numero n de tipo Float como argumento 
-- si n es 0 menor o igual a 9 devuelve 7
-- si n es 0 mayor o igual a 3 devuelve 5
-- > entre 0 si 9 devuelve 7, de 10 a +oo devuelve 5
--requiere {True}
--asegura {res = 7 <-> n es menor que 9, si no res = 5 }

f6 :: Float -> Int -> Bool
f6 a b = truncate a == b
-- In Haskell, the truncate function is used to truncate a floating-point number to an integral value, 
-- effectively removing the decimal part of the number. 
-- It takes a floating-point number as input and returns an integral number of the same type.
{-
The function f6 takes a Float value a and an Int value b as arguments and checks whether truncating the Float value a results in the Int value b. If the truncation of a is equal to b, the function returns True, indicating that a and b are equivalent after truncation; otherwise, it returns False.
-}