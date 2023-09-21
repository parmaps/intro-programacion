------------------------------
--Simulacro Parcial 1: Haskell
------------------------------
-- Ejercicio 1

{-
    problema relacionesValidas (relaciones: seq〈StringxString〉) : Bool {
        requiere: { True }
        asegura: { res = T rue ←→ relaciones no contiene ni tuplas repetidas1,
        ni tuplas con ambas componentes iguales}
    }
1 A los fines de este problema consideraremos que dos tuplas son iguales si el
par de elementos que las componen (sin importar el orden) son iguales

--Ejemplos:
--relacionesValidas [("ana","bob"), ("ana","ana")] = False
--relacionesValidas [("ana","bob"), ("ana","bob")] = False
--relacionesValidas [("ana","bob"), ("bob","ana")] = False
--relacionesValidas [("ana","bob"), ("ana","charly")] = True
--relacionesValidas [("ana","bob"), ("bob","charly"), ("ana","charly")] = True
--relacionesValidas [("ana","bob"), ("ana","charly"), ("bob","charly"), ("charly","bob")] = False
--relacionesValidas [("ana","bob"), ("ana","charly"), ("bob","charly"), ("bob","charly")] = False
--relacionesValidas [("ana","bob"), ("ana","charly"), ("bob","charly"), ("charly","ana")] = False
--relacionesValidas [("ana","bob"), ("ana","charly"), ("bob","charly"), ("charly","charly")] = False

-}

relacionesValidas :: [(String, String)] -> Bool
relacionesValidas [] = True
relacionesValidas ((a,b):xs) 
    | a == b = False
    | pertenece (a,b) xs || pertenece (b,a) xs = False
    | otherwise = relacionesValidas xs



pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece x (y:ys) = x == y || pertenece x ys


-- Ejercicio 2

{-
    problema personas (relaciones: seq〈StringxString〉) : seq〈String〉 {
        requiere: { relacionesValidas(relaciones) }
        asegura: { res no tiene elementos repetidos }
        asegura: { res tiene exactamente los elementos que figuran en alguna
        tupla de relaciones, en cualquiera de sus posiciones}
    }

--Ejemplos:
--personas [("ana","bob")] = ["ana", "bob"]
--personas [("ana","bob"), ("ana","charly")] = ["ana", "bob", "charly"]
--personas [("ana","bob"), ("bob","charly"), ("ana","charly")] = ["ana", "bob", "charly"]
--personas [("ana","bob"), ("bob","charly"), ("ana","charly"), ("dylan","charly")] = ["ana", "bob", "charly", "dylan"]
--personas [("ana","bob"), ("bob","charly"), ("ana","charly"), ("dylan","charly"), ("bob","dylan")] = ["ana", "bob", "charly", "dylan"]
-}

personas ::  [(String, String)] -> [String]
personas [] = []
personas xs = personasAux (sacarDeTuplas xs) [] --llamo la funcion auxiliar de personas con una lista con todas las personas y otra lista vacia como argumentos

sacarDeTuplas ::  [(String, String)] -> [String]
sacarDeTuplas [] = []
sacarDeTuplas ((a,b):xs) = a:b:sacarDeTuplas xs

personasAux ::  [String] -> [String] -> [String]
personasAux [] listaAux = [] 
personasAux (x:xs) listaAux
   | pertenece x listaAux = personasAux xs listaAux --si el primer elemento pertenece a la lista auxiliar, pasar al siguiente
   | otherwise = x : personasAux xs (listaAux ++ [x])


{-
    problema amigosDe (persona: String, relaciones: seq〈StringxString〉) :    seq〈String〉 {
        requiere: { relacionesValidas(relaciones) }
        asegura: { res tiene exactamente los elementos que figuran en las tuplas
        de relaciones en las que una de sus componentes es persona}
    }
-}

amigosDe :: String -> [(String, String)] -> [String]
amigosDe _ [] = []
amigosDe persona ((a, b): xs) = 