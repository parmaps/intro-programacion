----------------------------------
-- Guia 4: Recursion sobre enteros
----------------------------------
--------------
{- Consejos clase
Pensar ejemplos primero para darme una idea de que esta pasando, una tabla con valores funciona bien
-}
--------------


--------------
-- Ejercicio 1
--------------
fibonacci :: Integer -> Integer 
-- fibonacci (0) = 1
-- fibonacci (1) = 1
-- fibonacci (2) = 2
-- fibonacci (3) = 3
-- fibonacci (4) = 5
-- fibonacci (5) = 8
-- fibonacci (6) = 13
fibonacci 0 = 1
fibonacci 1 = 1
fibonacci n = fibonacci (n-1) + fibonacci (n-2)


--------------
-- Ejercicio 2
--------------
parteEntera :: Float -> Integer
-- asegura: { resultado ≤ x < resultado + 1 }
--parteEntera (0) = 0 ≤ 0 < 1
--parteEntera (1.1) = 1 ≤ 1.1 <2
--parteEntera (-1.1) = -2 ≤ -1.1 < -1
parteEntera x | 0 <= x && x < 1 = 0
              | x >= 1 = 1 + parteEntera (x-1)
              | otherwise = (-1) + parteEntera (x+1)


--------------
-- Ejercicio 3
--------------
esDivisible :: Integer -> Integer -> Bool 
-- dados dos numeros naturales determinar si el primero es divisible por el segundo
--esDivisible 4 2 = True
--esDivisible 2 4 = False
esDivisible x y | (x - y) == 0 = True
                | x < y = False
                | otherwise = esDivisible (x-y) y


--------------
-- Ejercicio 4
--------------
--  dado n ∈ N sume los primeros n numeros impares
-- sumaImpares 3 ; 1+3+5=9
-- sumaImpares 4 ; 1+3+5+7=16
-- sumaImpares 5 ; 1+3+5+7+9=25
-- sumaImpares :: Integer -> Integer

--sumaImpares n = sumaImpares(n-1) + sumaImpares(n-2)

-- Idea previa: sumar numeros hasta N
-- sumaHastaNum 0 = 0
-- sumaHastaNum 1 = 1
-- sumaHastaNum n = sumaHastaNum (n-1) + n

sumaImpares :: Integer -> Integer
sumaImpares 0 = 0
sumaImpares 1 = 1
sumaImpares n = sumaImpares (n-1) + 2*n-1


--------------
-- Ejercicio 5
--------------

{-Implementar la función medioFact :: Integer ->Integer que dado n ∈ N calcula n!! 
Por ejemplo:
medioFact 10 ; 10 ∗ 8 ∗ 6 ∗ 4 ∗ 2 ; 3840.
medioFact 9 ; 9 ∗ 7 ∗ 5 ∗ 3 ∗ 1 ; 945.
medioFact 5 ; 5 ∗ 3 ∗ 1 ; 15.
medioFact 0 ; 1.
-}
medioFac :: Integer -> Integer
medioFac 0 = 1
medioFac 1 = 1
medioFac n = n * medioFac (n - 2)

--------------
-- Ejercicio 6
--------------

{-Especificar e implementar la función sumaDigitos :: Integer ->Integer que calcula la suma de dı́gitos de
un número natural. Para esta función pueden utilizar div y mod.

problema sumaDigitos (n: Z) : Z {
    requiere : {n > 0}
    asegura: {res es la suma de cada digito de n}

}

Por ejemplo:
sumaDigitos 10 = 1+0 = 1
sumaDigitos 123 = 1+2+3 = 6
sumaDigitos 2367 = 2+3+6+7 = 18
-}

sumaDigitos :: Integer -> Integer 
-- sumaDigitos 0 = 0
-- sumaDigitos 1 = 1
sumaDigitos n | n < 10 = n 
              | otherwise = n `mod` 10  + sumaDigitos (n `div` 10)

obtenerDigitos :: Integer -> Integer
obtenerDigitos n | n < 10 = n 
            --   | otherwise = n `mod` 10  + sumaDigitos (n `div` 10)
                --  | n < 100 = n (devuelve dos digitos)
                 | otherwise = obtenerDigitos (n `div` 10)


--------------
-- Ejercicio 7
--------------

{-Implementar la funcion todosDigitosIguales :: Integer -> Bool 
que determina si todos los dıgitos de un numero natural son iguales.

problema todosDigitosIguales (n: Z) : Bool {
    requiere : {n > 0}
    asegura: {res = True <-> todos los digitos de n son iguales }

-}

-- todosDigitosIguales :: Integer -> Bool
-- todosDigitosIguales n | n < 10 = True
                    --   | n `mod` 10  == c = True  

sonIguales :: Integer -> Integer -> Bool
sonIguales n digito | n < 10 = n == digito
                    | otherwise = (n `mod` 10  ==  digito)  && sonIguales (n `div` 10) digito

checkIguales :: Integer -> Integer -> Bool
checkIguales n digito
  | n < 10 = n == digito
  | otherwise = (n `mod` 10 == digito) && checkIguales (n `div` 10) digito 

todosDigitosIgualesBot :: Integer -> Bool
todosDigitosIgualesBot n = checkIguales n (n `mod` 10)                   

todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n | n < 10 = True
                      | n `mod` 10  ==  ((n `div` 10) `mod` 10) = todosDigitosIguales (n `div` 10)
                      | otherwise = False
                    --   | otherwise = n `mod` 10  ==  (n `div` 10) && todosDigitosIguales (n `div` 10)
-- todosDigitosIguales n = checkIguales n (n `mod` 10)
                    --   | n `mod` 10  ==  (n `div` 10) = n `div` 10
                    --   | n ==  n `div` 10 = n `div` 10 

{-
La expresión n `mod` 10  ==  ((n `div` 10) `mod` 10) se utiliza para verificar si el último dígito de un número (n) es igual al penúltimo dígito.

Explicación paso a paso:
    n mod 10: Esta parte de la expresión calcula el residuo de la división de n por 10. En otras palabras, extrae el último dígito del número n.

    n div 10: Esta parte de la expresión realiza la división entera de n entre 10. 
    Esto elimina el último dígito de n, ya que la división entera simplemente trunca el número.

    ((n div10)mod 10): Luego, se aplica el operador mod nuevamente a la división entera de n por 10. 
    Esto extrae el nuevo último dígito después de quitar el primer dígito.

    Finalmente, se compara si el último dígito original de n (calculado en el paso 1) es igual al nuevo último dígito (calculado en el paso 3).

En resumen, esta expresión verifica si el último dígito de n es igual al penúltimo dígito después de quitar el último dígito. 
Si ambos dígitos son iguales, entonces el número tiene dígitos repetidos al final.

Esta comparación es crucial en la implementación de la función todosDigitosIguales, 
ya que ayuda a determinar si los dígitos son iguales para continuar con la recursión.
-}

                    

--------------
-- Ejercicio 8
--------------
{-
Ejercicio 8. Implementar la funcion iesimoDigito :: Integer ->Integer ->Integer 
que dado un n ∈ N≥0 y un i ∈ N menor o igual a la cantidad de dıgitos de n, 
devuelve el i-´esimo dıgito de n.

problema iesimoDigito (n: Z, i: N) : Z {
requiere: { n ≥ 0 ∧ 1 ≤ i ≤ cantDigitos(n) }
asegura: { resultado = (n div 10cantDigitos(n)−i) mod 10 }
}
problema cantDigitos (n: Z) : N {
requiere: { n ≥ 0 }
asegura: { n = 0 → resultado = 1}
asegura: { n 6 = 0 → (n div 10resultado−1 > 0 ∧ n div 10resultado = 0) }
}
-}



--------------
-- Ejercicio 9
--------------
{-
Especificar e implementar una funcion esCapicua :: Integer -> Bool 
que dado n ∈ N≥0 determina si n es un numero capicua


problema esCapicua (n: Z) : Bool {
    requiere {n >= 0}
    asegura 
}

Ejemplos
esCapicua 1881 -> True
esCapicua 181  -> True
esCapicua 18   -> False 

-}

-- esCapicua :: Integer -> Bool