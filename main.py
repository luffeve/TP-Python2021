import os
from posixpath import abspath                                  # Para manejar archivos en distintos sistemas operativos.
import sys                                 # Por si hay que cortar la ejecucion del programa.

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


    
#enfrentar: String Strint Integer-> [[String]] 
#Definicion: Esta funcion recibe las direcciones de los archivos de jugadors y distancias,
#y tambien el N que representa la distancia maxima para el enfrentamiento de dos jugadores, 
#retorna una lista de listas con los enfrentamientos correspondientes a una ronda. 
def enfrentar(jugadores_join, distancias_join, N):
    jugadores_mayores= categoria(jugadores_join, '+')
    jugadores_menores= categoria(jugadores_join, '-')

    




