import os
from main import categoria

#Para testear esta funcion usaremos unos archivos creados por el equipo donde uno contendra 4 personas
#de las cuales dos seran mayores de edad y dos seran menores. El otro sera un archivo vacio.
def test_categoria():
    jugadores_join = os.path.join(os.path.dirname(os.path.abspath(__file__)), "jugadores_test.txt")
    jugadoresV2_join = os.path.join(os.path.dirname(os.path.abspath(__file__)), "jugadoresV2_test.txt")
    assert categoria(jugadores_join, '+') == ["GASTON MORICONI,23,Cruz Alta", "LORENZO RE,21,Rosario"]
    assert categoria(jugadores_join, '-') == ["AGUSTINA LOPEZ,17,Rosario","CAMILA GARCIA,16,CABA"]
    assert categoria(jugadoresV2_join, '+') == []
    assert categoria(jugadoresV2_join, '-') == []