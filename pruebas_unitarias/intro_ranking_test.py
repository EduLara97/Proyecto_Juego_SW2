import unittest
import intro_ranking

class TestEvents(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_salir_juego(self):
        tecla = "q"
        presionar = "si"
        request_code = 200
        output = intro_ranking.intro_ranking(tecla, presionar, request_code)
        self.assertEqual(output, "salir del juego", "Error al salir del juego")
    def test_continuar_juego(self):
        tecla = "c"
        presionar = "si"
        request_code = 200
        output = intro_ranking.intro_ranking(tecla, presionar, request_code)
        self.assertEqual(output, "volver al menú", "Error al volver al menú")
    def test_mostrar_ranking(self):
        tecla = " "
        presionar = "no"
        request_code = 200
        output = intro_ranking.intro_ranking(tecla, presionar, request_code)
        self.assertEqual(output, "se pinto score en pantalla",
                         "Error al mostrar score en la pantalla")
    
