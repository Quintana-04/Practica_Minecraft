import unittest
from unittest.mock import MagicMock, patch
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importar InsultBot
from MyAdventures.mcpi.minecraft import Minecraft
from MyAdventures.InsultBOT import InsultBot


class TestInsultBot(unittest.TestCase):
    def setUp(self):
        # Crear el mock para Minecraft y asignarlo al bot
        self.mc = MagicMock()
        self.bot = InsultBot(self.mc)

    def test_random_insult(self):
        # Probar que se envía un insulto aleatorio al chat
        with patch('random.choice', return_value="Eres más inútil que un pico de madera en el Nether.") as mock_choice:
            self.bot.random_insult()
            self.mc.postToChat.assert_called_with("Eres más inútil que un pico de madera en el Nether.")

    def test_custom_insult(self):
        # Probar que se envía un insulto personalizado
        self.bot.custom_insult("Steve")
        self.mc.postToChat.assert_called_with("Steve, eres un genio... en hacer tonterías.")

    def test_execute_action_known(self):
        # Probar la ejecución de un comando conocido
        with patch.object(self.bot, 'random_insult') as mock_random_insult:
            self.bot.execute_action("random_insult")
            mock_random_insult.assert_called_once()

    def test_execute_action_unknown(self):
        # Probar la ejecución de un comando desconocido
        self.bot.execute_action("unknown_command")
        self.mc.postToChat.assert_called_with("No entiendo ese comando.")

    def test_execute_action_with_args(self):
        # Probar la ejecución de un comando conocido con argumentos
        with patch.object(self.bot, 'custom_insult') as mock_custom_insult:
            self.bot.execute_action("custom_insult", "Alex")
            mock_custom_insult.assert_called_once_with("Alex")

if __name__ == '__main__':
    unittest.main()
