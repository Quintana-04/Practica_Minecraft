import mcpi.minecraft as minecraft
import mcpi.block as block

# Obtener la posición actual del jugador
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
print(f"El jugador está en x: {pos.x}, y: {pos.y}, z: {pos.z}")


# Colocar un bloque de piedra frente al jugador
mc.setBlock(pos.x + 1, pos.y, pos.z, block.STONE.id)