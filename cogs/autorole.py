from types import MemberDescriptorType
import discord
from discord.ext import commands
from discord.utils import get

class Autorole(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Autorole 
    @commands.Cog.listener()
    async def on_member_join(member):
        try:
            # Try to add role
            role = get(member.guild.roles, name="The Role")
            await member.add_roles(role)
            embed = discord.Embed(title=f"Welcome, {member.name}!", color=discord.Color.blue())
            await message.channel.send(embed=embed)
        except Exception:
            # Error if cannot add role
            embed = discord.Embed(title="ERROR", description="Please make sure the bot's role is higher than the role's", color=discord.Color.red())
            await message.channel.send(embed=embed)


    # A test command to add a role to the user, so that we could use it on join
    @commands.command()
    async def addrole(self, message):
        try:
            # Try to add role
            role = get(message.author.guild.roles, name="The Role")
            await message.author.add_roles(role)
            embed = discord.Embed(title="Role successfully added!", description="You are cool lol", color=discord.Color.blue())
            await message.channel.send(embed=embed)
        except Exception:
            # Error if cannot add role
            embed = discord.Embed(title="ERROR", description="Please make sure the bot's role is higher than the role's", color=discord.Color.red())
            await message.channel.send(embed=embed)

def setup(client):
    client.add_cog(Autorole(client))