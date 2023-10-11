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


-- Ejercicio 4
{-
    problema personaConMasAmigos (relaciones: seq〈StringxString〉) : String {
        requiere: { relaciones no vacıa }
        requiere: { relacionesValidas(relaciones) }
        asegura: { res es el String que aparece mas veces en las tuplas de relaciones (o alguno de ellos si hay empate)}
}


--personaConMasAmigosRecursiva ["ana", "bob", "charly", "dylan"] [("ana","bob")] = "ana"
--personaConMasAmigosRecursiva ["ana", "bob", "charly", "dylan"] [("ana","bob"), ("ana","charly")] = "ana"
--personaConMasAmigosRecursiva ["ana", "bob", "charly", "dylan"] [("ana","bob"), ("bob","charly"), ("ana","charly")] = "bob"
--personaConMasAmigosRecursiva ["ana", "bob", "charly", "dylan"] [("ana","bob"), ("bob","charly"), ("ana","charly"), ("dylan","charly")] = "bob"
--personaConMasAmigosRecursiva ["ana", "bob", "charly", "dylan"] [("ana","bob"), ("bob","charly"), ("ana","charly"), ("dylan","charly"), ("bob","dylan")] = "bob"

-}

--VERSION IMPERATIVA: armo una DS con personas y cantidad de amigos, y devuelvo la persona con mas amigos
--y luego comparar cantidad de amigos y devolver persona con mayor cantidad
personaConMasAmigosImperativo :: [(String, String)] -> String
personaConMasAmigosImperativo [] = []
personaConMasAmigosImperativo relaciones = maximo cantidadAmigosPersonas
    where
        listaPersonas = personas relaciones
        cantidadAmigosPersonas = cantidadDeAmigosTodosTuplas listaPersonas relaciones

--cantidad de amigos de una persona
cantidadDeAmigosPersona :: String -> [(String, String)] -> Integer
cantidadDeAmigosPersona [] _ = 0
cantidadDeAmigosPersona persona relaciones = longitud (amigosDe persona relaciones) 

--armar lista de cantidad de amigos de cada persona [amigos, amigos...]
cantidadDeAmigosTodos :: [String] -> [(String, String)] -> [Integer]
cantidadDeAmigosTodos [] _ = []
cantidadDeAmigosTodos (persona:ps) relaciones = cantidadDeAmigosPersona persona relaciones : cantidadDeAmigosTodos ps relaciones  

--armar lista de tuplas de cantidad de amigos de cada persona [(persona, amigos), (persona, amigos)...]
cantidadDeAmigosTodosTuplas :: [String] -> [(String, String)] -> [(String, Integer)]
cantidadDeAmigosTodosTuplas [] _ = []
cantidadDeAmigosTodosTuplas (persona:ps) relaciones 
    = (persona, cantidadDeAmigosPersona persona relaciones) : cantidadDeAmigosTodosTuplas ps relaciones  

--obtener el maximo de los valores b y devolver a
maximo :: [(String, Integer)] -> String
maximo [] = []
maximo [(persona1, amigos1)] = persona1
maximo ((persona1, amigos1):(persona2,amigos2):rs) 
    -- | amigos1 > amigos2  = persona1 
    | amigos1 >= amigos2 = maximo ((persona1,amigos1):rs)
    | otherwise = maximo ((persona2,amigos2):rs)

-- para no tener que armar tuplas -> pasa personas y cantidad de amigos por params
-- asume que se corresponden 1 a 1 y devuelve persona (en el caso base: cuando hay una sola persona, devuelve esta)
maximoSolucion :: [String] -> [Int] -> String
maximoSolucion [p] _ = p
maximoSolucion (p0:p1:ps) (c0:c1:cs)  | c0 > c1   = maximoSolucion (p0:ps) (c0:cs)
                              | otherwise = maximoSolucion (p1:ps) (c1:cs)    

longitud :: [t] -> Integer
longitud [] = 0
longitud (_:xs) = 1 + longitud xs


--VERSION FUNCIONAL: pregunto si la primer persona tiene mas amigos que la segunda, si es asi, pregunto por el resto; si no pregunto lo mismo desde la segunda
-- TODO 22/9 ME FALTARIA VER SI PUEDO HACERLO DIRECTO -> EN VEZ DE amigosPrimero y amigosSegundo, preguntar por amigosPrimero y amigosResto
-- Esta version es del mediodia del 22/9, esta bien (inspirada en maximo tmb del 22/9)
personaConMasAmigosFuncional :: [(String, String)] -> String
personaConMasAmigosFuncional relaciones = calcularPersonaConMasAmigosFuncional (personas relaciones) relaciones

calcularPersonaConMasAmigosFuncional :: [String] -> [(String, String)] -> String
calcularPersonaConMasAmigosFuncional [] _ = []
calcularPersonaConMasAmigosFuncional [p1] _ = p1 --ESTO ES CLAVE! DEFINO BIEN EL CASO BASE: si queda una sola persona, esta es la que mas amigos tiene
calcularPersonaConMasAmigosFuncional (p1:p2:ps) relaciones  
    | amigosPrimero >= amigosSegundo = calcularPersonaConMasAmigosFuncional (p1:ps) relaciones
    | otherwise = calcularPersonaConMasAmigosFuncional (p2:ps) relaciones
    where 
        amigosPrimero = longitud (amigosDe p1 relaciones)
        amigosSegundo = longitud (amigosDe p2 relaciones)


-- Esta version es de la tardenoche del 21/9, esta mal y no me daba cuenta por que
personaConMasAmigosFuncionalMal :: [String] -> [(String, String)] -> String
personaConMasAmigosFuncionalMal [] _ = []
personaConMasAmigosFuncionalMal [p] _ = p
personaConMasAmigosFuncionalMal (p:ps) relaciones 
    | amigosPrimero > longitud (personaConMasAmigosFuncionalMal ps relaciones) = p
    | otherwise = personaConMasAmigosFuncionalMal ps relaciones
     where 
        amigosPrimero = longitud (amigosDe p relaciones)


-- personaConMasAmigos relaciones 
--     -- | longitud amigosPrimerPersona >= longitud amigosSegundaPersona = "la primer persona tiene mas o igual cantidad de amigos que la segunda"
--     | longitud amigosPrimerPersona >= longitud amigosSegundaPersona  = primeraPersona
--     | otherwise = segundaPersona
--     where 
--         primeraPersona = head (personas relaciones)
--         amigosPrimerPersona = amigosDe primeraPersona relaciones
--         segundaPersona = head (sacarPrimero (personas relaciones))
--         amigosSegundaPersona = amigosDe segundaPersona relaciones
        -- amigosSegundaPersona = amigosDe (head (sacarPrimero (personas relaciones))) relaciones

--si el primero tiene mas amigos que el segundo





