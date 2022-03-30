from types import MemberDescriptorType
import discord
from discord.ext import commands
from discord.utils import get

class ModCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Kick
    @commands.command()
    async def kick(self, message, user : discord.Member, reason = ""):
        await user.kick(reason = reason)
        embed = discord.Embed(title=f"Kicked!", color=discord.Color.green())
        await message.channel.send(embed=embed)


    # Ban
    @commands.command()
    async def ban(self, message, user : discord.Member, reason = ""):
        await user.ban(reason = reason)
        embed = discord.Embed(title=f"Banned!", color=discord.Color.green())
        await message.channel.send(embed=embed)

def setup(client):
    client.add_cog(ModCommands(client))