"""
Modulo de pruebas unitarias para programa.py
Fecha: 09/09/2024
"""
import unittest
from test_programa import suma, es_mayor
class testprograma(unittest.testcase):
    #metodos de pruea
    def texte_suma_positivos(self):
        self.asserEqual(suma(1,4),5)

        def test_suma_negativos(self):
            self.assertequal(suma( 2,4), 6)

        def test_suma_detro_de_un_rango(self):
            self.assertin(suma(2,9),[1,2,4,6,7])
            # Desarrollar puebas para la funcion "es_mayor"
            #Desarrollar puebas para a division de 2 numero

            if __name__ == "_main_":
                unittest.main()