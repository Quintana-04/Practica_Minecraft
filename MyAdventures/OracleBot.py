from bot_framework import BotBase
class OracleBot(BotBase):
    def __init__(self, mc):
        super().__init__(mc, "OracleBot")
        # Preguntas y respuestas predefinidas
        self.respuestas = {
            "hola": "¡Hola! ¿En qué puedo ayudarte?",
            "como estas": "¡Estoy aquí para responder tus preguntas!",
            "cual es tu nombre": f"Me llamo {self.nombre}.",
            "cuanto es 2 + 2": "El resultado es 4",
            "chao": "¡Hasta luego! Espero haberte ayudado."
        }

    def ejecutar_comando(self, comando, *args):
        if comando == "responder":
            if not args:
                self.mc.postToChat(f"{self.nombre}: No entiendo la pregunta.")
            else:
                self.responder(" ".join(args))
        else:
            self.mc.postToChat(f"{self.nombre}: Comando '{comando}' no reconocido.")

    def responder(self, pregunta):
        pregunta = pregunta.lower()  # Convertir la pregunta a minúsculas
        respuesta = self.respuestas.get(pregunta.strip(), "No estoy seguro de cómo responder eso.")
        self.mc.postToChat(f"{self.nombre}: {respuesta}")

    def detener(self):
        self.mc.postToChat(f"{self.nombre}: Detenido.")