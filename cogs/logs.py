from types import MemberDescriptorType
import discord
from discord.ext import commands
from discord.utils import get
from collections import defaultdict

class Logs(commands.Cog):
    def __init__(self, client):
        self.client = client

    # We also need to make db instead of dictionary
    logChannel = defaultdict(dict)

    @commands.command()
    async def setLogsChannel(self, message):
        try:
            Logs.logChannel[message.guild.id] = message.channel.id
            embed = discord.Embed(title=f"Channel {message.channel} turned to log channel!", color=discord.Color.green())
            await message.channel.send(embed=embed)
        except Exception:
            embed = discord.Embed(title="ERROR", description="Role syntax: `$setLogsChannel`", color=discord.Color.red())
            await message.channel.send(embed=embed)
    
    async def getChannel(self, member):
        return self.client.get_channel(Logs.logChannel[member.guild.id])
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        embed = discord.Embed(title=f"{member.name} joined the server", color=discord.Color.blue())
        try:
            await self.getChannel(member).send(embed=embed)
        except Exception:
            pass
    
    @commands.Cog.listener()
    async def on_member_leave(self, member):
        embed = discord.Embed(title=f"{member.name} left", color=discord.Color.blue())
        try:
            await self.getChannel(member).send(embed=embed)
        except Exception:
            pass

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        embed = discord.Embed(title=f"A message was deleted by {message.author.name}:", description=f"```{message.content}``` \nChannel: {message.channel.mention}", color=discord.Color.blue())
        try:
            channel = await self.getChannel(message.author)
            await channel.send(embed=embed)
        except Exception as e:
            print(e)

    @commands.Cog.listener()
    async def on_message_edit(self, message_before, message_after):
        embed = discord.Embed(title=f"A message was edited by {message_after.author.name}:", description=f"Before:```{message_before.content}``` \nAfter:```{message_after.content}``` \nChannel: {message_after.channel.mention}", color=discord.Color.blue())
        try:
            channel = await self.getChannel(message_after.author)
            await channel.send(embed=embed)
        except Exception as e:
            print(e)

def setup(client):
    client.add_cog(Logs(client))