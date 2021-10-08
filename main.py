import os              # Para manejar archivos en distintos sistemas operativos.
import sys             # Por si hay que cortar la ejecucion del programa.

#categoria: String Char -> [String]
#Descripcion: Esta funcion recibe la direccion de un archivo cuyo contenido
#va a ser una lista de jugadores, y un caracter('+' para MAYORES DE EDAD o '-' PARA MENORES DE EDAD).
#Luego retorna una lista con aquellos jugadores pertenecientes a la categoria deseada.

def categoria (jugadores_join, categoria):
    jugadores=open(jugadores_join, "r") #Abro la lista de jugadores en modo lectura
    
    jugadores_categoria=[] #Lista de jugadores a retornar

    if categoria == '+': #Si deseo lista de mayores
        for linea in jugadores.readlines(): #Recorro el archivo 
            edad_jugador = (linea.split(','))[1] #Para saber la edad del jugador
            if edad_jugador >= '18': #Entonces es mayor de edad y lo agrego a la lista
                jugadores_categoria.append(linea[0:-1] if linea[-1] == "\n" else linea) #Al leer linea por linea todas menos la ultima
                                                                                        #tienen un salto de linea("\n") que hay que sacar.
    else: #Entonces deseo los menores de edad
        for linea in jugadores.readlines():
            edad_jugador = (linea.split(','))[1]
            if edad_jugador < '18':
                jugadores_categoria.append(linea[0:-1] if linea[-1]=="\n" else linea)

    jugadores.close() #Cierro el archivo 
    return jugadores_categoria #Y retorno la lista de jugadores pertenecientes a la categoria deseada        

#Para testear esta funcion usaremos unos archivos creados por el equipo donde uno contendra 4 personas
#de las cuales dos seran mayores de edad y dos seran menores. El otro sera un archivo vacio.
def test_categoria():
    jugadores_join = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tests", "jugadores_test.txt")
    jugadoresV2_join = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tests", "jugadoresV2_test.txt")
    assert categoria(jugadores_join, '+') == ["GASTON MORICONI,23,Cruz Alta", "LORENZO RE,21,Rosario"]
    assert categoria(jugadores_join, '-') == ["AGUSTINA LOPEZ,17,Rosario","CAMILA GARCIA,16,CABA"]
    assert categoria(jugadoresV2_join, '+') == []
    assert categoria(jugadoresV2_join, '-') == []



#distancia: String String String-> String
#definicion: Recibe dos jugadores y un archivo de distancias, luego devuelve la distancia entre los jugadores
#ingresados
def distancia(jugador1, jugador2, distancias_join):
    distancias=open(distancias_join, "r")   #Abro el archivo de distancias en modo lectura
    ciudadJ1=(jugador1.split(','))[2]       #Del jugador 1, me quedo con su ciudad
    ciudadJ2=(jugador2.split(','))[2]       #Del jugador 2, me quedo con su ciudad

    for linea in distancias.readlines():    #Por cada linea
        linea=linea[0:-1] if linea[-1]=="\n" else linea #Para sacar el salto de linea cuando sea necesario
        if (ciudadJ1 in linea) and (ciudadJ2 in linea): #Si en la linea leida estan las ciudades de ambos jugadores
            distancia=linea.split(',')[2]   #Entonces me quedo con su distancia
            
    distancias.close() #Luego cierro el archivo 
    return distancia   #Y retorno la distancia


#Test para la funcion distancia donde distancias_join toma un archivo creado por el equipo
#donde se encuentran algunas distancias.
def test_distancia():
    distancias_join = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tests", "distancias_test.txt")
    assert distancia("GASTON MORICONI,23,Cordoba","LORENZO RE,21,Rosario", distancias_join) == " 400.9"
    assert distancia("JOSE LOPEZ,40,CABA","JUAN GARCIA,45,Rosario", distancias_join) == " 299.9"

#pueden_enfrentarse: String String String Integer --> Boolean
#recibe dos jugadores y un numero que representara la distancia maxima permitida
#para que dos jugadores se puedan enfrentar
def pueden_enfrentarse(jugador1, jugador2, distancias_join, distancia_maxima):
    ciudadJ1 = jugador1.split(',')[2]
    ciudadJ2 = jugador2.split(',')[2]

    distancia_entre_jugadores = distancia(jugador1, jugador2, distancias_join)

    return ((ciudadJ1==ciudadJ2) or (float(distancia_entre_jugadores)<=distancia_maxima))

def test_pueden_enfrentarse():
    distancias_join = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tests", "distancias_test.txt")
    assert pueden_enfrentarse("GASTON MORICONI,23,Cordoba","LORENZO RE,21,Rosario", distancias_join,300) == False
    assert pueden_enfrentarse("GASTON MORICONI,23,Cordoba","LORENZO RE,21,Rosario", distancias_join,500) == True
    assert pueden_enfrentarse("JOSE LOPEZ,40,CABA","JUAN GARAY,43,CABA", distancias_join,100) == True
    assert pueden_enfrentarse("MARIA GONZALEZ,50,CABA","LUCIA SANCHEZ,26,Rosario", distancias_join,200) == False

#es_numero: char -> Boolean
#Descripcion: Recibe una cadena de caracteres y devuelve True si es numerico o si lo puede convertir a numerico,
#sino retornara False
def es_numero(char):
    try:
        float(char)
        return True
    except ValueError:
        return False

def test_es_numero():
    assert es_numero("hola") == False
    assert es_numero("245j") == False
    assert es_numero("245") == True
    assert es_numero(455) == True       

# comenzar_juego: None -> None
# esta funcion es la que llevara adelante el juego
#
def comenzar_juego():
    
    #--------------PIDO LOS DATOS DE ENTRADA------------------
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))          # Para mantener una compatibilidad entre S.O.
    while True:                                                       # Hasta que ingrese un archivo de jugadores valido
        jugadores_nombre = input("Ingrese el nombre del archivo de jugadores: ")
        jugadores_join = os.path.join(THIS_FOLDER, jugadores_nombre)
        if os.path.isfile(jugadores_join):
            break                                                     
    while True:                                                       # Hasta que ingrese un archivo de distancias valido 
        distancias_nombre = input("Ingrese el nombre del archivo de distancias: ")
        distancias_join = os.path.join(THIS_FOLDER, distancias_nombre)
        if os.path.isfile(distancias_join):
            break

    while True:
        distancia_permitida = input("Ingrese la distancia maxima permitida: ")
        if es_numero(distancia_permitida):
            break

    #-----------------------------------------------------------

    #-----------------------------------------------------------
    resultados = open("resultado.txt", "w") #El archivo de resultados no existe y va a ser creado.
    #Lista de jugadores
    jugadores_mayores = categoria(jugadores_join, '+')
    jugadores_menores = categoria(jugadores_join, '-')



    




