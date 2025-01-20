from bot_framework import BotBase
import math
import mcpi.block as block

class TNTBot(BotBase):
    def __init__(self, mc):
        super().__init__(mc, "TNTBot")

    def ejecutar_comando(self, comando, *args):
        if comando == "colocar_tnt":
            self.colocar_tnt()
        elif comando == "detonar_tnt":
            self.detonar_tnt()
        else:
            self.mc.postToChat("Comando no reconocido.")

    def calcular_posicion_frente(self, pos, yaw):
        rad = math.radians(yaw)
        x = pos.x + round(-math.sin(rad))
        z = pos.z + round(math.cos(rad))
        return x, pos.y, z

    def colocar_tnt(self):
        pos = self.mc.player.getTilePos()
        yaw = self.mc.player.getRotation()
        x, y, z = self.calcular_posicion_frente(pos, yaw)
        self.mc.setBlock(x, y, z, block.TNT.id)
        self.mc.postToChat(f"{self.nombre}: TNT colocada en ({x}, {y}, {z})!")

    def detonar_tnt(self):
        pos = self.mc.player.getTilePos()
        yaw = self.mc.player.getRotation()
        x, y, z = self.calcular_posicion_frente(pos, yaw)
        self.mc.setBlock(x, y, z, block.TNT.id)
        self.mc.setBlock(x, y + 1, z, block.FIRE.id)
        self.mc.postToChat(f"{self.nombre}: TNT activada en ({x}, {y}, {z})!")

    def detener(self):
        self.mc.postToChat(f"{self.nombre}: Detenido.")
