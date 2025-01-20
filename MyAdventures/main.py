from bot_framework import BotManager
import TNTBot
import InsultBot
import OracleBot

import mcpi.minecraft as minecraft


mc = minecraft.Minecraft.create()
manager = BotManager(mc)

# Registrar bots
manager.registrar_bot("insult", InsultBot(mc))
manager.registrar_bot("oracle", OracleBot(mc))
manager.registrar_bot("tnt", TNTBot(mc))

mc.postToChat("Bots registrados. Usa el comando '<bot> <comando>' para interactuar.")

while True:
    messages = mc.events.pollChatPosts()
    for message in messages:
        manager.procesar_comando(message.message)
