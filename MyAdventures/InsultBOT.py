import mcpi.minecraft as minecraft
import random
import time
import subprocess
import os
import sys

class InsultBot:
    def __init__(self, mc):
        self.mc = mc
        self.insults = [
            "Eres más inútil que un pico de madera en el Nether.",
            "Tu casa parece un cubo de tierra... oh espera, lo es.",
            "Tu skin debería estar prohibida por mal gusto.",
            "Construyes peor que un Creeper enfadado.",
            "Tu sentido de orientación es tan malo que te pierdes en el Overworld."
        ]

    def random_insult(self):
        """Envía un insulto aleatorio al chat de Minecraft."""
        insult = random.choice(self.insults)
        self.mc.postToChat(insult)

    def custom_insult(self, name):
        """Envía un insulto personalizado al chat de Minecraft."""
        insult = f"{name}, eres un genio... en hacer tonterías."
        self.mc.postToChat(insult)

    def execute_action(self, action, *args):
        """Método reflexivo que ejecuta dinámicamente acciones según el comando."""
        if hasattr(self, action):
            method = getattr(self, action)
            method(*args)
        else:
            self.mc.postToChat("No entiendo ese comando.")

# Función para iniciar el InsultBot en otra terminal
def start_insult_bot():
    current_file = os.path.abspath(__file__)
    subprocess.Popen(["python", current_file, "--bot"], creationflags=subprocess.CREATE_NEW_CONSOLE if os.name == "nt" else 0)

# Crear conexión al servidor de Minecraft
mc = minecraft.Minecraft.create()

# Función para monitorear mensajes del chat
def monitor_chat():
    bot = InsultBot(mc)
    mc.postToChat("InsultBot activado. Escribe un comando:")
    mc.postToChat("Comandos disponibles: random_insult, custom_insult <nombre>")

    while True:
        time.sleep(1)  # Esperar un momento antes de leer nuevos mensajes
        messages = mc.events.pollChatPosts()  # Leer mensajes del chat

        for message in messages:
            user_message = message.message
            parts = user_message.split()
            command = parts[0]
            args = parts[1:]

            if command == "exit":
                mc.postToChat("¡Adiós, inútil!")
                exit()

            # Ejecuta la acción dinámicamente
            bot.execute_action(command, *args)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--bot":
        # Ejecuta el InsultBot directamente
        monitor_chat()
    else:
        print("Lanzando InsultBot en otra terminal...")
        start_insult_bot()
