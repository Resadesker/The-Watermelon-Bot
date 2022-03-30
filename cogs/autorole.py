from types import MemberDescriptorType
import discord
from discord.ext import commands
from discord.utils import get

class Autorole(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.channel = self.client.get_channel(958435074846654466)

    # Autorole 
    @commands.Cog.listener()
    async def on_member_join(self, member):
        # Channel's id is now general in the test server
        embed = discord.Embed(title=f"Welcome, {member.name}!", color=discord.Color.blue())
        embed.set_image(url=member.avatar_url)
        await self.client.get_channel(958435074846654466).send(embed=embed)


        # Add role
        try:
            role = get(member.guild.roles, name="The Role")
            await member.add_roles(role)
        except Exception:
            await self.client.get_channel(958435074846654466).send("ERROR GIVING THE ROLE: Please check if it is lower than the bot's one")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        embed = discord.Embed(title=f"{member.name} has left", color=discord.Color.blue())
        await self.client.get_channel(958435074846654466).send(embed=embed)


    # @commands.Cog.listener()
    # async def on_member_join(ctx):
    #     # Channel's id is now general in the test server
    #     await commands.Cog.get_channel(958435074846654466).send(f"{ctx.member.name} has joined")
    #     try:
    #         # Try to add role
    #         role = get(ctx.member.guild.roles, name="The Role")
    #         await ctx.member.add_roles(role)
            
    #         embed = discord.Embed(title=f"Welcome, {ctx.member.name}!", color=discord.Color.blue())
    #         await ctx.send(embed=embed)
    #     except Exception:
    #         # Error if cannot add role
    #         embed = discord.Embed(title="ERROR", description="Please make sure the bot's role is higher than the role's", color=discord.Color.red())
    #         await ctx.send(embed=embed)


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