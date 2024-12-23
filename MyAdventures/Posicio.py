import mcpi.minecraft as minecraft

# Obtener la posición actual del jugador
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
print(f"El jugador está en x: {pos.x}, y: {pos.y}, z: {pos.z}")