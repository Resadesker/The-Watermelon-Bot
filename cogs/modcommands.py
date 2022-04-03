from types import MemberDescriptorType
import discord
from discord.ext import commands
from discord.utils import get
import datetime
import aiohttp

class ModCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Kick
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, message, user : discord.Member, reason = ""):
        await user.kick(reason = reason)
        embed = discord.Embed(title=f"Kicked!", color=discord.Color.green())
        await message.channel.send(embed=embed)


    # Ban
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, message, user : discord.Member, reason = ""):
        await user.ban(reason = reason)
        embed = discord.Embed(title=f"Banned!", color=discord.Color.green())
        await message.channel.send(embed=embed)

    # Artificial mute cause discord.py is no longer developed and doesn't support the ready one
    async def timeout_user(self, *, user_id: int, guild_id: int, until):
        headers = {"Authorization": f"Bot {self.client.http.token}"}
        url = f"https://discord.com/api/v9/guilds/{guild_id}/members/{user_id}"
        timeout = (datetime.datetime.utcnow() + datetime.timedelta(minutes=until)).isoformat()
        json = {'communication_disabled_until': timeout}
        self.client.session = aiohttp.ClientSession()
        async with self.client.session.patch(url, json=json, headers=headers) as session:
            if session.status in range(200, 299):
                await self.client.session.close()
                return True
            await self.client.session.close()
            return False


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx: commands.Context, member: discord.Member, minutes=10080):
        # Use artificial mute
        handshake = await self.timeout_user(user_id=member.id, guild_id=ctx.guild.id, until=minutes)
        if handshake:
            embed = discord.Embed(title=f"Successfully muted {member.name} for {minutes} minutes.", color=discord.Color.green())
            return await ctx.send(embed=embed)

        embed = discord.Embed(title=f"Something went wrong", color=discord.Color.red())
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx: commands.Context, member: discord.Member):
        # Use artificial mute
        handshake = await self.timeout_user(user_id=member.id, guild_id=ctx.guild.id, until=0)
        if handshake:
            embed = discord.Embed(title=f"Successfully unmuted {member.name}.", color=discord.Color.green())
            return await ctx.send(embed=embed)

        embed = discord.Embed(title=f"Something went wrong", color=discord.Color.red())
        await ctx.send(embed=embed)

    @commands.command(name='unban')
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, id: int):
        user = await self.client.fetch_user(id)
        await ctx.guild.unban(user)
        embed = discord.Embed(title=f"Successfully unbanned {user.name}.", color=discord.Color.green())
        return await ctx.send(embed=embed)

def setup(client):
    client.add_cog(ModCommands(client))