import unittest
from unittest.mock import MagicMock, patch
import sys
import os

# Ajustar el sys.path para importar InsultBot
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importar InsultBot
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
            self.mc.postToChat.assert_called_with("InsultBot: Eres más inútil que un pico de madera en el Nether.")

    def test_custom_insult(self):
        # Probar que se envía un insulto personalizado
        self.bot.custom_insult("Steve")
        self.mc.postToChat.assert_called_with("InsultBot: Steve, eres un genio... en hacer tonterías.")

    def test_custom_insult_no_name(self):
        # Probar que se maneja la ausencia de un nombre
        self.bot.custom_insult()
        self.mc.postToChat.assert_called_with("InsultBot: Necesitas especificar un nombre para insultar.")

    def test_execute_action_known(self):
        # Probar la ejecución de un comando conocido
        with patch.object(self.bot, 'random_insult') as mock_random_insult:
            self.bot.ejecutar_comando("random_insult")
            mock_random_insult.assert_called_once()

    def test_execute_action_unknown(self):
        # Probar la ejecución de un comando desconocido
        self.bot.ejecutar_comando("unknown_command")
        self.mc.postToChat.assert_called_with("InsultBot: Comando 'unknown_command' no reconocido.")

    def test_execute_action_with_args(self):
        # Probar la ejecución de un comando conocido con argumentos
        with patch.object(self.bot, 'custom_insult') as mock_custom_insult:
            self.bot.ejecutar_comando("custom_insult", "Alex")
            mock_custom_insult.assert_called_once_with("Alex")

    def test_list_methods(self):
        # Probar que se listan los métodos correctamente
        with patch.object(self.mc, 'postToChat') as mock_post_to_chat:
            self.bot.listar_metodos()
            mock_post_to_chat.assert_called()

if __name__ == '__main__':
    unittest.main()
