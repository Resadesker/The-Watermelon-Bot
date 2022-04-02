# from asyncio.windows_events import NULL
from types import MemberDescriptorType
import discord
from discord.ext import commands
from discord.utils import get

class Cleaner(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def clear(self, ctx, limit : int):
        if limit <= 0: 
            embed = discord.Embed(title="ERROR: limit must be bigger than 0", color=discord.Color.red())
            await ctx.send(embed=embed)
            return

        await ctx.channel.purge(limit=limit+1)
        embed = discord.Embed(title=f"{limit} messages cleared!", color=discord.Color.green())
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Cleaner(client))