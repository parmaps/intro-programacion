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
relacionesValidas ((a,b):rs) 
    | a == b = False
    | pertenece (a,b) rs || pertenece (b,a) rs = False
    | otherwise = relacionesValidas rs



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
personas rs = personasAux (personasRepetidas rs) [] --llamo la funcion auxiliar de personas con una lista con todas las personas y otra lista vacia como argumentos

personasRepetidas ::  [(String, String)] -> [String]
personasRepetidas [] = []
personasRepetidas ((p1,p2):rs) = p1 : p2 : personasRepetidas rs

personasAux ::  [String] -> [String] -> [String]
personasAux [] listaAux = [] 
personasAux (persona:rs) listaAux
   | pertenece persona listaAux = personasAux rs listaAux --si el primer elemento pertenece a la lista auxiliar, pasar al siguiente
   | otherwise = persona : personasAux rs (listaAux ++ [persona])

-- idea de la solucion del parcial (la lista quedara con la ultima aparicion de cada elemento, porque saca el primero)
personasSolucion :: [(String,String)] -> [String]
personasSolucion rs = sacarRepes (personasRepetidas rs)

sacarRepes :: (Eq t) => [t] -> [t]
sacarRepes [] = []
sacarRepes (x:xs)
 | pertenece x xs = pasoRecursivo
 | otherwise = x : pasoRecursivo
 where pasoRecursivo = sacarRepes xs




-- Ejercicio 3
{-
    problema amigosDe (persona: String, relaciones: seq〈StringxString〉) :    seq〈String〉 {
        requiere: { relacionesValidas(relaciones) }
        asegura: { res tiene exactamente los elementos que figuran en las tuplas
        de relaciones en las que una de sus componentes es persona}
    }

--amigosDe "ana" [("ana","bob")] = ["bob"]
--amigosDe "ana" [("ana","bob"), ("ana","charly")] = ["bob", "charly"]
--amigosDe "bob" [("ana","bob"), ("bob","charly"), ("ana","charly")] = ["ana", "charly"]
--amigosDe "charly" [("ana","bob"), ("bob","charly"), ("ana","charly"), ("dylan","charly")] = ["bob", "ana", "dylan"]
--amigosDe "dylan" [("ana","bob"), ("bob","charly"), ("ana","charly"), ("dylan","charly"), ("bob","dylan")] = ["dylan"]
-}

amigosDe :: String -> [(String, String)] -> [String]
amigosDe _ [] = []
amigosDe persona ((a, b): rs) 
    | persona == a = b: pasoRecursivo
    | persona == b = a: pasoRecursivo
    | otherwise = pasoRecursivo
    where pasoRecursivo = amigosDe persona rs


