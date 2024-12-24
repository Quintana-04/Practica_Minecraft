import mcpi.minecraft as minecraft
import mcpi.block as block
import math
import inspect

mc = minecraft.Minecraft.create()

class TNTBot:
    def __init__(self, nombre):
        self.nombre = nombre
        self.escuchando = True  # Variable para controlar si escucha o no

    # Función para calcular la posición frente al jugador según la rotación
    def calcular_posicion_frente(self, pos, yaw):
        # Convertir la rotación a radianes
        rad = math.radians(yaw)
        # Calcular las coordenadas frente al jugador
        x = pos.x + round(-math.sin(rad))  # Invertimos el eje X
        z = pos.z + round(math.cos(rad))   # Z permanece igual
        return x, pos.y, z

    # Colocar TNT en la dirección hacia donde está mirando el jugador
    def colocar_tnt(self):
        pos = mc.player.getTilePos()
        yaw = mc.player.getRotation()
        x, y, z = self.calcular_posicion_frente(pos, yaw)
        mc.setBlock(x, y, z, block.TNT.id)
        mc.postToChat(f"{self.nombre}: TNT colocada en ({x}, {y}, {z})!")

    # Detonar TNT en la dirección hacia donde está mirando el jugador
    def detonar_tnt(self):
        pos = mc.player.getTilePos()
        yaw = mc.player.getRotation()
        x, y, z = self.calcular_posicion_frente(pos, yaw)
        mc.setBlock(x, y, z, block.TNT.id)
        mc.setBlock(x, y + 1, z, block.FIRE.id)  # Activar el TNT con fuego
        mc.postToChat(f"{self.nombre}: TNT activada en ({x}, {y}, {z})!")

    # Mostrar un listado de las acciones que se pueden hacer
    def listar_acciones(self):
        mc.postToChat(f"{self.nombre}: Acciones disponibles: -colocar_tnt || -detonar_tnt || -detener")

    # Detener el bot
    def detener(self):
        self.escuchando = False
        mc.postToChat(f"{self.nombre}: Dejando de escuchar comandos del chat.")

# Crear el bot
bot = TNTBot("ExplosiveBot")

# Reflexión: Ejecutar acción dinámica
def ejecutar_accion(bot, accion):
    if hasattr(bot, accion):
        metodo = getattr(bot, accion)
        if callable(metodo):
            metodo()
        else:
            mc.postToChat(f"{bot.nombre}: '{accion}' no es ejecutable.")
    else:
        mc.postToChat(f"{bot.nombre}: Acción '{accion}' no encontrada.")

# Escuchar comandos desde el chat
def escuchar_chat():
    mc.postToChat("[Bot]: Escribe un comando en el chat para interactuar! Usa 'detener' para detener el bot.")
    while bot.escuchando:
        for chat_post in mc.events.pollChatPosts():
            comando = chat_post.message.lower().replace(" ", "_")
            ejecutar_accion(bot, comando)

# Iniciar escucha del chat
if __name__ == "__main__":
    try:
        escuchar_chat()
    except KeyboardInterrupt:
        mc.postToChat("[Bot]: Deteniendo el script.")
        print("Script detenido manualmente.")