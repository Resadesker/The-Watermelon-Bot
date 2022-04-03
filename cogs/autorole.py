from types import MemberDescriptorType
import discord
from discord.ext import commands
from discord.utils import get
from collections import defaultdict

class Autorole(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.channel = self.client.get_channel(958435074846654466)

    # We also need to make db instead of dictionary
    starterRoles = defaultdict(dict)
    welcomeChannel = defaultdict(dict)

    # Command to set an action (role giving) on emoji click on specific message  
    @commands.command()
    async def setStarterRole(self, message, role : discord.Role):
        try:
            Autorole.starterRoles[message.guild.id] = role.id
            embed = discord.Embed(title=f"Added role {role.name} as default!", color=discord.Color.green())
            await message.channel.send(embed=embed)
        except Exception:
            embed = discord.Embed(title="ERROR", description="Role syntax: `$setStarterRole <role>`", color=discord.Color.red())
            await message.channel.send(embed=embed)

    @commands.command()
    async def setWelcomeChannel(self, message):
        try:
            Autorole.welcomeChannel[message.guild.id] = message.channel.id
            embed = discord.Embed(title=f"Added channel {message.channel} as default!", color=discord.Color.green())
            await message.channel.send(embed=embed)
        except Exception:
            embed = discord.Embed(title="ERROR", description="Role syntax: `$setWelcomeChannel`", color=discord.Color.red())
            await message.channel.send(embed=embed)
    # Autorole 
    @commands.Cog.listener()
    async def on_member_join(self, member):
        # Channel's id is now general in the test server
        embed = discord.Embed(title=f"Welcome, {member.name}!", color=discord.Color.blue())
        embed.set_image(url=member.avatar_url)
        try:
            await self.client.get_channel(Autorole.welcomeChannel[member.guild.id]).send(embed=embed)
        except Exception:
            pass

        try:
            # Add role
            role = get(member.guild.roles, id=Autorole.starterRoles[member.guild.id])
            await member.add_roles(role)
        except Exception:
            pass

def setup(client):
    client.add_cog(Autorole(client))