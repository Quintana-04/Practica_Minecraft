import unittest
from unittest.mock import MagicMock, patch
import sys
import os

# Agregar el directorio raíz al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importar OracleBot y Minecraft
from MyAdventures.OracleBot import OracleBot
from MyAdventures.mcpi.minecraft import Minecraft


class TestOracleBot(unittest.TestCase):
    def setUp(self):
        # Crear el mock para Minecraft y asignarlo al bot
        self.mc = MagicMock()
        self.bot = OracleBot("TestBot")
        # Inyectar el mock en lugar del cliente de Minecraft real
        self.bot.mc = self.mc

    def test_responder_conocido(self):
        # Probar una pregunta con respuesta predefinida
        with patch('MyAdventures.OracleBot.mc.postToChat') as mock_post_to_chat:
            self.bot.responder("hola")
            mock_post_to_chat.assert_called_with("TestBot: ¡Hola! ¿En que puedo ayudarte?")

    def test_responder_desconocido(self):
        # Probar una pregunta desconocida
        with patch('MyAdventures.OracleBot.mc.postToChat') as mock_post_to_chat:
            with patch('random.choice', return_value="Respuesta simulada."):
                self.bot.responder("pregunta desconocida")
                mock_post_to_chat.assert_called_with("TestBot: Respuesta simulada.")

    def test_nombre_bot(self):
        # Verificar el nombre del bot
        self.assertEqual(self.bot.nombre, "TestBot")

    def test_detener_bot(self):
        # Probar el método detener
        with patch('MyAdventures.OracleBot.mc.postToChat') as mock_post_to_chat:
            self.bot.detener()
            mock_post_to_chat.assert_called_with("TestBot: Dejando de escuchar preguntas.")
            self.assertFalse(self.bot.escuchando)

if __name__ == '__main__':
    unittest.main()
