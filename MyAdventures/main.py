from bot_framework import BotManager
from InsultBOT import InsultBot
from OracleBot import OracleBot
from TNTBot import TNTBot
import mcpi.minecraft as minecraft

# Crear conexión a Minecraft
mc = minecraft.Minecraft.create()

# Crear el gestor de bots
manager = BotManager(mc)

# Registrar los bots en el gestor
manager.registrar_bot("insult", InsultBot(mc))
manager.registrar_bot("oracle", OracleBot(mc))
manager.registrar_bot("tnt", TNTBot(mc))

mc.postToChat("Bots registrados. Usa el comando '<bot> <comando> [args...]' para interactuar.")

# Función para filtrar mensajes que coincidan con el patrón <nombre_bot> <comando>
def filtrar_mensajes_validos(msg):
    parts = msg.message.split()
    if len(parts) < 2:
        return False  # Mensajes que no tienen al menos <nombre_bot> y <comando>

    bot_nombre = parts[0]
    return bot_nombre in manager.bots

# Procesar mensajes del chat
while True:
    messages = mc.events.pollChatPosts()

    # Aplicar filtrado funcional a los mensajes
    mensajes_validos = filter(filtrar_mensajes_validos, messages)

    for mensaje in mensajes_validos:
        # Pasar directamente el mensaje válido al gestor
        manager.procesar_comando(mensaje.message)