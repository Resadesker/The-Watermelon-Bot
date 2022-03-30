from types import MemberDescriptorType
import discord
from discord.ext import commands
from discord.utils import get

class Errors(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        text = ""
        if isinstance(error, commands.MissingRequiredArgument):
            text = 'Please pass in all requirements :rolling_eyes:.'
        elif isinstance(error, commands.MissingPermissions):
            text = "You dont have all the requirements :angry: \n Please make sure the bot's role is higher than the role's"
        else:
            text = "An unknown error occured"
        embed = discord.Embed(title="ERROR", description=error, color=discord.Color.red())
        print(error)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Errors(client))