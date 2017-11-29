import unittest
import pausa

class TestIntroModo(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_continuar_juego(self):
        tecla = "c"
        presionar = "si"
        output = pausa.pausa(tecla, presionar)
        self.assertEqual(output, "continuar", "Error al continuar juego")
    def test_salir_juego(self):
        tecla = "q"
        presionar = "si"
        output = pausa.pausa(tecla, presionar)
        self.assertEqual(output, "salir juego", "Error al salir del juego")
    def test_salir_al_menu(self):
        tecla = "x"
        presionar = "si"
        output = pausa.pausa(tecla, presionar)
        self.assertEqual(output, "salir al menu", "Error al salir al menu")
1
