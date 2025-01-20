from bot_framework import BotBase
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
        """Ejecuta comandos específicos del bot."""
        if comando == "random_insult":
            self.random_insult()
        elif comando == "custom_insult" and args:
            self.custom_insult(args[0])
        else:
            self.mc.postToChat(f"{self.nombre}: Comando '{comando}' no reconocido.")

    def random_insult(self):
        """Envía un insulto aleatorio al chat de Minecraft."""
        insult = random.choice(self.insults)
        self.mc.postToChat(f"{self.nombre}: {insult}")

    def custom_insult(self, name):
        """Envía un insulto personalizado al chat de Minecraft."""
        insult = f"{name}, eres un genio... en hacer tonterías."
        self.mc.postToChat(f"{self.nombre}: {insult}")

    def detener(self):
        """Detiene el bot."""
        self.mc.postToChat(f"{self.nombre}: Detenido.")
