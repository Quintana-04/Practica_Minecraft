import mcpi.minecraft as minecraft
import mcpi.block as block

# Conectar al servidor
mc = minecraft.Minecraft.create()

# Obtener la posición inicial del jugador
pos = mc.player.getTilePos()

# Construir una torre de piedra
for i in range(10):
    mc.setBlock(pos.x, pos.y + i, pos.z, block.STONE.id)

mc.postToChat("¡Torre construida!")
