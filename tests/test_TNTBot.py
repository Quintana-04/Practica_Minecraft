import unittest
from unittest.mock import MagicMock
import sys
import os

# Agregar el directorio raíz al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importar TNTBot
from MyAdventures.TNTBot import TNTBot
import MyAdventures.mcpi.block as block

class TestTNTBot(unittest.TestCase):
    def setUp(self):
        self.mc = MagicMock()
        self.bot = TNTBot(self.mc)

    def test_calcular_posicion_frente(self):
        pos = MagicMock(x=10, y=5, z=10)
        test_cases = [
            (0, (10, 5, 11)),  # Norte
            (90, (9, 5, 10)),  # Este
            (180, (10, 5, 9)),  # Sur
            (270, (11, 5, 10))  # Oeste
        ]

        for yaw, expected in test_cases:
            with self.subTest(yaw=yaw):
                self.assertEqual(self.bot.calcular_posicion_frente(pos, yaw), expected)

    def test_colocar_tnt(self):
        self.mc.player.getTilePos.return_value = MagicMock(x=10, y=5, z=10)
        self.mc.player.getRotation.return_value = 90

        self.bot.colocar_tnt()
        self.mc.setBlock.assert_called_with(9, 5, 10, block.TNT.id)
        self.mc.postToChat.assert_called_with("TNTBot: TNT colocada en (9, 5, 10)!")

    def test_detonar_tnt(self):
        self.mc.player.getTilePos.return_value = MagicMock(x=10, y=5, z=10)
        self.mc.player.getRotation.return_value = 0

        self.bot.detonar_tnt()
        self.mc.setBlock.assert_any_call(10, 5, 11, block.TNT.id)
        self.mc.setBlock.assert_any_call(10, 6, 11, block.FIRE.id)
        self.mc.postToChat.assert_called_with("TNTBot: TNT activada en (10, 5, 11)!")

    def test_listar_metodos(self):
        self.bot.listar_metodos()
        self.mc.postToChat.assert_called()

    def test_ejecutar_comando_restringido(self):
        self.bot.ejecutar_comando("calcular_posicion_frente")
        self.mc.postToChat.assert_called_with("TNTBot: No tienes permiso para usar el comando 'calcular_posicion_frente'.")

    def test_ejecutar_comando_invalido(self):
        self.bot.ejecutar_comando("comando_invalido")
        self.mc.postToChat.assert_called_with("TNTBot: Comando 'comando_invalido' no reconocido.")


if __name__ == '__main__':
    unittest.main()
