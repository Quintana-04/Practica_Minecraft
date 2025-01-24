from bot_framework import BotBase
import random

from bot_framework import BotBase
import mcpi.minecraft as minecraft
import random

class InsultBot(BotBase):
    def __init__(self, mc):
        super().__init__(mc, "InsultBot")
        self.insults = [
            "Eres más inútil que un pico de madera en el Nether.",
            "Tu casa parece un cubo de tierra... oh espera, lo es.",
            "Tu skin debería estar prohibida por mal gusto.",
            "Construyes peor que un Creeper enfadado.",
            "Tu sentido de orientación es tan malo que te pierdes en el Overworld."
        ]

    def ejecutar_comando(self, comando, *args):
        if hasattr(self, comando):
            metodo = getattr(self, comando)
            if callable(metodo):
                try:
                    metodo(*args)
                except TypeError:
                    self.mc.postToChat(f"{self.nombre}: Faltan parámetros para el comando '{comando}'.")
            else:
                self.mc.postToChat(f"{self.nombre}: '{comando}' no es ejecutable.")
        else:
            self.mc.postToChat(f"{self.nombre}: Comando '{comando}' no reconocido.")

    def random_insult(self):
        insult = random.choice(self.insults)
        self.mc.postToChat(f"{self.nombre}: {insult}")

    def custom_insult(self, name=None):
        if not name:
            self.mc.postToChat(f"{self.nombre}: Necesitas especificar un nombre para insultar.")
            return
        insult = f"{name}, eres un genio... en hacer tonterías."
        self.mc.postToChat(f"{self.nombre}: {insult}")

    def listar_metodos(self):
        metodos = [name for name in dir(self) if callable(getattr(self, name)) and not name.startswith("_") and name != "ejecutar_comando"]
        self.mc.postToChat(f"{self.nombre}: Métodos disponibles: {', '.join(metodos)}")