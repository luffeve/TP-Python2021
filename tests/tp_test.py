import os
from main import categoria

#Para testear esta funcion usaremos unos archivos creados por el equipo donde uno contendra 4 personas
#de las cuales dos seran mayores de edad y dos seran menores. El otro sera un archivo vacio.
def test_categoria():
    jugadores_join = os.path.join(os.path.dirname(os.path.abspath(__file__)), "jugadores_test.txt")
    jugadoresV2_join = os.path.join(os.path.dirname(os.path.abspath(__file__)), "jugadoresV2_test.txt")
#    jugadoresV3_join = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.pardir,"jugadores.txt")
    assert categoria(jugadores_join, '+') == ["GASTON MORICONI,23,Cruz Alta", "LORENZO RE,21,Rosario"]
    assert categoria(jugadores_join, '5') == ["AGUSTINA LOPEZ,17,Rosario","CAMILA GARCIA,16,CABA"]
    assert categoria(jugadoresV2_join, '+') == []
    assert categoria(jugadoresV2_join, '5') == []
#    assert categoria(jugadoresV3_join, '+') == ["JOSE DELGADO,51,Rosario","CARMEN CORRALES,75,Santa Fe"]
#    assert categoria(jugadoresV3_join, '-') == ["RECAREDO MURILLO,17,Villa Constitucion","LILLY MONGE,16,Rosario"]