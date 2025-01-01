import mcpi.minecraft as minecraft
import random

mc = minecraft.Minecraft.create()

class OracleBot:
    def __init__(self, nombre):
        self.nombre = nombre
        self.escuchando = True
        # Preguntas y respuestas predefinidas
        self.respuestas = {
            "hola": "¡Hola! ¿En que puedo ayudarte?",
            "¿como estas?": "¡Estoy aqui para responder tus preguntas!",
            "¿cual es tu nombre?": f"Me llamo {self.nombre}.",
            "¿cuanto es 2 + 2?": "El resultado es 4",
            "chao": "¡Hasta luego! Espero haberte ayudado."
        }

    # Responder preguntas del chat
    def responder(self, pregunta):
        pregunta = pregunta.lower()  # Convertir la pregunta a minúsculas
        if pregunta in self.respuestas:
            respuesta = self.respuestas[pregunta]
        else:
            respuesta = random.choice([
                "No estoy seguro de cómo responder eso.",
                "Hmmm... buena pregunta.",
                "¡Intenta preguntar algo más específico!"
            ])
        mc.postToChat(f"{self.nombre}: {respuesta}")

    # Detener el bot
    def detener(self):
        self.escuchando = False
        mc.postToChat(f"{self.nombre}: Dejando de escuchar preguntas.")

# Crear el bot
bot = OracleBot("OracleBot")

# Escuchar preguntas desde el chat
def escuchar_chat():
    mc.postToChat(f"[Bot]: Escribe una pregunta para {bot.nombre}, o usa 'detener' para detener el bot.")
    while bot.escuchando:
        for chat_post in mc.events.pollChatPosts():
            pregunta = chat_post.message
            if pregunta.lower() == "detener":
                bot.detener()
            else:
                bot.responder(pregunta)

# Iniciar escucha del chat
if __name__ == "__main__":
    try:
        escuchar_chat()
    except KeyboardInterrupt:
        mc.postToChat("[Bot]: Deteniendo el script.")
        print("Script detenido manualmente.")
