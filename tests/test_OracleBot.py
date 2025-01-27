import unittest
from unittest.mock import MagicMock, patch
import sys
import os

# Agregar el directorio raíz al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importar OracleBot
from MyAdventures.OracleBot import OracleBot


class TestOracleBot(unittest.TestCase):
    def setUp(self):
        # Crear el mock para Minecraft y asignarlo al bot
        self.mc = MagicMock()
        self.bot = OracleBot(self.mc)

    def test_responder_conocido(self):
        # Probar una pregunta con respuesta predefinida
        self.bot.responder("hola")
        self.mc.postToChat.assert_called_with("OracleBot: ¡Hola! ¿En qué puedo ayudarte?")

    def test_responder_desconocido(self):
        # Probar una pregunta desconocida
        with patch('random.choice', return_value="Respuesta simulada."):
            self.bot.responder("pregunta desconocida")
            self.mc.postToChat.assert_called_with("OracleBot: No estoy seguro de cómo responder eso.")

    def test_nombre_bot(self):
        # Verificar el nombre del bot
        self.assertEqual(self.bot.nombre, "OracleBot")

    def test_execute_known_command(self):
        # Probar la ejecución de un comando conocido
        with patch.object(self.bot, 'listar_metodos') as mock_listar_metodos:
            self.bot.ejecutar_comando("listar_metodos")
            mock_listar_metodos.assert_called_once()

    def test_execute_unknown_command(self):
        # Probar la ejecución de un comando desconocido
        self.bot.ejecutar_comando("comando_inexistente")
        self.mc.postToChat.assert_called_with("OracleBot: Comando 'comando_inexistente' no reconocido.")

    def test_list_methods(self):
        # Probar listar métodos
        self.bot.listar_metodos()
        self.mc.postToChat.assert_called()

if __name__ == '__main__':
    unittest.main()
