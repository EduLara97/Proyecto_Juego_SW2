import unittest
import events

class TestEvents(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_salir_juego(self):
        tecla = "q"
        presionar = "si"
        output = events.events(tecla, presionar)
        self.assertEqual(output, "salir de", "Error al salir del juego")
    def test_pausa(self):
        tecla = "p"
        presionar = "si"
        output = events.events(tecla, presionar)
        self.assertEqual(output, "juego pausado", "Error al pausar juego")
    def test_saltar(self):
        tecla = "barra_espaciadora"
        presionar = "si"
        output = events.events(tecla, presionar)
        self.assertEqual(output, "saltar", "Error al saltar")
        
        
