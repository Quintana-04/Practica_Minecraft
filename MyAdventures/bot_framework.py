import mcpi.minecraft as minecraft
import abc

class BotBase(abc.ABC):
    """Interfaz base para todos los bots."""

    def __init__(self, mc, nombre):
        self.mc = mc
        self.nombre = nombre

    @abc.abstractmethod
    def ejecutar_comando(self, comando, *args):
        """Método para ejecutar comandos específicos del bot."""
        pass


class BotManager:
    """Gestor para manejar múltiples bots."""

    def __init__(self, mc):
        self.mc = mc
        self.bots = {}

    def registrar_bot(self, nombre, bot):
        """Registrar un nuevo bot en el gestor."""
        if nombre in self.bots:
            self.mc.postToChat(f"Error: Ya existe un bot con el nombre {nombre}.")
        else:
            self.bots[nombre] = bot
            self.mc.postToChat(f"Bot {nombre} registrado correctamente.")

    def eliminar_bot(self, nombre):
        """Eliminar un bot del gestor."""
        if nombre in self.bots:
            del self.bots[nombre]
            self.mc.postToChat(f"Bot {nombre} eliminado.")
        else:
            self.mc.postToChat(f"No se encontró un bot con el nombre {nombre}.")

    def procesar_comando(self, mensaje):
        """Procesar comandos globales y específicos de bots."""
        parts = mensaje.split()
        if len(parts) < 2:
            self.mc.postToChat("Formato del comando: <bot> <comando> [args...]")
            return

        bot_nombre, comando = parts[0], parts[1]
        args = parts[2:]

        if bot_nombre in self.bots:
            bot = self.bots[bot_nombre]
            bot.ejecutar_comando(comando, *args)
        else:
            self.mc.postToChat(f"No se encontró un bot con el nombre {bot_nombre}.")
