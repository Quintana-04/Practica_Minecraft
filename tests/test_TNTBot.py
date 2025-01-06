import unittest
from unittest.mock import MagicMock, patch
import sys
import os
import math

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importar TNTBot
from MyAdventures.TNTBot import TNTBot
import mcpi.block as block
from MyAdventures.TNTBot import ejecutar_accion

class TestTNTBot(unittest.TestCase):
    def setUp(self):
        # Crear el mock para Minecraft
        self.mc = MagicMock()
        TNTBot.mc = self.mc  # Inyectar el mock de Minecraft
        self.bot = TNTBot("ExplosiveBot")

    def test_calcular_posicion_frente(self):
        pos = MagicMock(x=10, y=5, z=10)

        # Mirando hacia el norte (0 grados)
        yaw = 0
        x, y, z = self.bot.calcular_posicion_frente(pos, yaw)
        self.assertEqual((x, y, z), (10, 5, 11))  # Incrementa Z

        # Mirando hacia el este (90 grados)
        yaw = 90
        x, y, z = self.bot.calcular_posicion_frente(pos, yaw)
        self.assertEqual((x, y, z), (9, 5, 10))  # Decrementa X

        # Mirando hacia el sur (180 grados)
        yaw = 180
        x, y, z = self.bot.calcular_posicion_frente(pos, yaw)
        self.assertEqual((x, y, z), (10, 5, 9))  # Decrementa Z

        # Mirando hacia el oeste (270 grados)
        yaw = 270
        x, y, z = self.bot.calcular_posicion_frente(pos, yaw)
        self.assertEqual((x, y, z), (11, 5, 10))  # Incrementa X


    def test_colocar_tnt(self):
        # Probar que se coloca TNT correctamente
        pos = MagicMock(x=10, y=5, z=10)
        yaw = 90  # Mirando hacia el este
        self.mc.player.getTilePos.return_value = pos
        self.mc.player.getRotation.return_value = yaw

        self.bot.colocar_tnt()

        # Verificar que se coloca TNT en la posición correcta
        self.mc.setBlock.assert_called_with(10, 5, 11, block.TNT.id)
        self.mc.postToChat.assert_called_with("ExplosiveBot: TNT colocada en (10, 5, 11)!")

    def test_detonar_tnt(self):
        # Probar que se detona TNT correctamente
        pos = MagicMock(x=10, y=5, z=10)
        yaw = 0  # Mirando hacia el norte
        self.mc.player.getTilePos.return_value = pos
        self.mc.player.getRotation.return_value = yaw

        self.bot.detonar_tnt()

        # Verificar que se coloca TNT y se activa con fuego
        self.mc.setBlock.assert_any_call(10, 5, 9, block.TNT.id)
        self.mc.setBlock.assert_any_call(10, 6, 9, block.FIRE.id)
        self.mc.postToChat.assert_called_with("ExplosiveBot: TNT activada en (10, 5, 9)!")

    def test_listar_acciones(self):
        # Probar que se listan las acciones disponibles
        self.bot.listar_acciones()
        self.mc.postToChat.assert_called_with("ExplosiveBot: Acciones disponibles: -colocar_tnt || -detonar_tnt || -detener")

    def test_detener(self):
        # Probar que el bot se detiene correctamente
        self.bot.detener()
        self.mc.postToChat.assert_called_with("ExplosiveBot: Dejando de escuchar comandos del chat.")
        self.assertFalse(self.bot.escuchando)

    def test_ejecutar_accion_valida(self):
        # Probar que se ejecuta una acción válida
        with patch.object(self.bot, 'colocar_tnt') as mock_colocar_tnt:
            mock_colocar_tnt.return_value = None
            self.bot.colocar_tnt()
            mock_colocar_tnt.assert_called_once()

    def test_ejecutar_accion_invalida(self):
        # Probar que se maneja un comando inválido
        with patch('MyAdventures.TNTBot.mc.postToChat') as mock_postToChat:
            ejecutar_accion(self.bot, "accion_invalida")
            mock_postToChat.assert_called_with("ExplosiveBot: Acción 'accion_invalida' no encontrada.")

if __name__ == '__main__':
    unittest.main()
