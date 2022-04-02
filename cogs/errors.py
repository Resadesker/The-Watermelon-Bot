from types import MemberDescriptorType
import discord
from discord.ext import commands
from discord.utils import get

class Errors(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        title = ""
        text = ""
        
        if isinstance(error, commands.BadArgument) or isinstance(error, commands.MissingRequiredArgument):
            usage = f'{self.client.command_prefix}{ctx.command.name} {ctx.command.signature}'
            text = f'Correct usage: {usage}'
            title = "Wrong command usage :no_entry:"
        elif isinstance(error, commands.MissingPermissions):
            title = "No right to use this command"
            text = "This command is for a higher role :exclamation:"
        else:
            text = error

        embed = discord.Embed(title="ERROR: " + title, description=text, color=discord.Color.red())
        print(error)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Errors(client))