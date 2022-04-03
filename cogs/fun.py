# from asyncio.windows_events import NULL
from types import MemberDescriptorType
import discord
from discord.ext import commands
from discord.utils import get
import random

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='ball')
    async def _8ball(self, ctx, question):
        responses = ['As I see it, yes :thumbsup:',
                'Yes :grinning:',
                'Positive :white_check_mark:',
                'From my point of view, yes :regional_indicator_y::regional_indicator_e::regional_indicator_s:',
                'Convinced :ok_hand:',
                'Chances High :clap:',
                'No :no_entry:',
                'Negative :name_badge:',
                'Not Convinced :face_with_raised_eyebrow:',
                'Perhaps :call_me:',
                'Not Sure :smile:',
                'Maybe :smirk_cat:']
        response = random.choice(responses)
        embed=discord.Embed(title=response, color=discord.Color.blue())
        await ctx.send(embed=embed)

    @commands.command()
    async def coin(self, ctx, headOrTail : str):
        if headOrTail.lower() != "head" and headOrTail.lower() != "tail":
            embed = discord.Embed(title="ERROR: wrong context", description='Please use `$coin <head or tail>` \n Use "head" or "tail" in <head or tail>', color=discord.Color.red())
            return await ctx.send(embed=embed)
        answers = ['Head',
                'Tail']
        response = random.choice(answers)

        result = ""
        if response.lower() == headOrTail.lower():
            result = ":thumbsup: Right! "
        else:
            result = ":no_entry: Wrong! "
        embed=discord.Embed(title=result + response, color=discord.Color.blue())
        await ctx.send(embed=embed)
    

def setup(client):
    client.add_cog(Fun(client))