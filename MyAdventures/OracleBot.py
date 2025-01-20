from bot_framework import BotBase

class OracleBot(BotBase):
    def __init__(self, mc):
        super().__init__(mc, "OracleBot")
        self.respuestas = {
            "hola": "¡Hola! ¿En que puedo ayudarte?",
            "¿como estas?": "¡Estoy aqui para responder tus preguntas!",
            "¿cual es tu nombre?": f"Me llamo {self.nombre}.",
            "¿cuanto es 2 + 2?": "El resultado es 4",
            "chao": "¡Hasta luego! Espero haberte ayudado."
        }

    def ejecutar_comando(self, comando, *args):
        if comando == "responder" and args:
            self.responder(args[0])
        else:
            self.mc.postToChat("Comando no reconocido.")

    def responder(self, pregunta):
        respuesta = self.respuestas.get(pregunta.lower(), "No estoy seguro de cómo responder eso.")
        self.mc.postToChat(f"{self.nombre}: {respuesta}")

    def detener(self):
        self.mc.postToChat(f"{self.nombre}: Detenido.")