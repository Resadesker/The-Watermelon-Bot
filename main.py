import discord
import os
from discord.ext import commands
import config


intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="$", intents=intents, case_insensitive=True, help_command=None)
# client = commands.Bot(command_prefix="$")

@client.event
async def on_ready():
    print("Bot is ready")


# @client.event
# async def on_member_join(self, member):
#     # Channel's id is now general in the test server
#     print(member)
#     await self.client.get_channel(958435074846654466).send(f"{member.name} has joined")

# Loading cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        print(filename)
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(config.TOKEN)