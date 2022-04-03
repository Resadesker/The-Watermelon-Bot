# from asyncio.windows_events import NULL
from types import MemberDescriptorType
import discord
from discord.ext import commands
from discord.utils import get

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def getCommands(self, name):
        # x = []
        str = ""
        for y in self.client.commands:
            if y.cog and y.cog.qualified_name == name:
                # x.append({self.client.command_prefix} + y.name)
                str += "`" + self.client.command_prefix + y.name + "` "
        return str
    
    @commands.command()
    async def help(self, message):
        embed = discord.Embed(title=f":question: Commands availible:", description=f"These are all commands this bot can respond to", color=discord.Color.blue())
        embed.add_field(name=":shield: Administrator commands:", value=await self.getCommands("ModCommands") + await self.getCommands("Cleaner") + await self.getCommands("RolePicker"), inline=False)
        embed.add_field(name=":grinning: Fun:", value=await self.getCommands("Fun"), inline=False)
        await message.channel.send(embed=embed)

def setup(client):
    client.add_cog(Help(client))