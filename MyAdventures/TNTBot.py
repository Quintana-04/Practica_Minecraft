import math
import mcpi.block as block

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from MyAdventures.bot_framework import BotBase



class TNTBot(BotBase):
    def __init__(self, mc):
        super().__init__(mc, "TNTBot")
        self.metodos_restringidos = ["calcular_posicion_frente"]

    def ejecutar_comando(self, comando, *args):
        if comando in self.metodos_restringidos:
            self.mc.postToChat(f"{self.nombre}: No tienes permiso para usar el comando '{comando}'.")
            return

        if hasattr(self, comando):
            metodo = getattr(self, comando)
            if callable(metodo):
                try:
                    metodo(*args)
                except TypeError:
                    self.mc.postToChat(f"{self.nombre}: Argumentos incorrectos para el comando '{comando}'.")
            else:
                self.mc.postToChat(f"{self.nombre}: '{comando}' no es ejecutable.")
        else:
            self.mc.postToChat(f"{self.nombre}: Comando '{comando}' no reconocido.")

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

    def listar_metodos(self):
        metodos = [name for name in dir(self) if callable(getattr(self, name)) and not name.startswith("_") and name != "ejecutar_comando"]
        self.mc.postToChat(f"{self.nombre}: Metodos disponibles: {', '.join(metodos)}")

    def detener(self):
        self.escuchando = False
        self.mc.postToChat(f"{self.nombre}: Dejando de escuchar comandos del chat.")
