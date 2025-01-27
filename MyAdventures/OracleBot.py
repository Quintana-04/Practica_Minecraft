import inspect

import sys
import os

if __name__ == "__main__":
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    
try:
    # Para cuando se ejecuta desde la raíz del proyecto
    from MyAdventures.bot_framework import BotBase
except ModuleNotFoundError:
    # Para cuando se ejecuta desde dentro de MyAdventures
    from bot_framework import BotBase



class OracleBot(BotBase):
    def __init__(self, mc):
        super().__init__(mc, "OracleBot")
        # Preguntas y respuestas predefinidas
        self.respuestas = {
            "hola": "¡Hola! ¿En qué puedo ayudarte?",
            "¿como estas?": "¡Estoy aquí para responder tus preguntas!",
            "¿cual es tu nombre?": f"Me llamo {self.nombre}.",
            "¿cuanto es 2 + 2?": "El resultado es 4",
            "chao": "¡Hasta luego! Espero haberte ayudado."
        }

    def ejecutar_comando(self, comando, *args):
        if hasattr(self, comando):
            metodo = getattr(self, comando)
            if callable(metodo):
                metodo(*args)
            else:
                self.mc.postToChat(f"{self.nombre}: '{comando}' no es ejecutable.")
        else:
            self.mc.postToChat(f"{self.nombre}: Comando '{comando}' no reconocido.")

    def responder(self, *args):
        pregunta = " ".join(args).lower().strip()
        respuesta = self.respuestas.get(pregunta, "No estoy seguro de cómo responder eso.")
        self.mc.postToChat(f"{self.nombre}: {respuesta}")

    def listar_metodos(self):
        metodos = [name for name in dir(self) if callable(getattr(self, name)) and not name.startswith("_") and name != "ejecutar_comando"]
        self.mc.postToChat(f"{self.nombre}: Metodos disponibles: {', '.join(metodos)}")

    def detener(self):
        """Detiene al bot, desactivando su capacidad de responder preguntas."""
        self.escuchando = False
        self.mc.postToChat(f"{self.nombre}: Dejando de escuchar preguntas.")