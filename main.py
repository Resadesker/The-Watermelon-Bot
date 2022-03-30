import discord
import os
from discord.ext import commands
import config

client = commands.Bot(command_prefix="$")

@client.event
async def on_ready():
    print("Bot is ready")

# Loading cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        print(filename)
        print(filename[:-3])
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(config.TOKEN)