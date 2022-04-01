# from asyncio.windows_events import NULL
from tkinter.tix import INTEGER
from types import MemberDescriptorType
import discord
from discord.ext import commands
from discord.utils import get
import emoji 
from collections import defaultdict

class RolePicker(commands.Cog):
    def __init__(self, client):
        self.client = client

    # We need a database instead of a dictionary here.
    messages = defaultdict(dict)

    # Command to set an action (role giving) on emoji click on specific message  
    @commands.command()
    async def setEmojiRole(self, message, id : int, emojis, role : discord.Role):
        try:
            RolePicker.messages[id][emoji.demojize(emojis)] = role.id
            embed = discord.Embed(title=f"Added role {role} to emoji {emojis} in message {id}!", color=discord.Color.green())
            await message.channel.send(embed=embed)
        except Exception:
            embed = discord.Embed(title="ERROR", description="Role syntax: `$setEmojiRole <message id> <emoji> <role>`", color=discord.Color.red())
            await message.channel.send(embed=embed)
        
        
    # Adding the role
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id in RolePicker.messages and RolePicker.messages[payload.message_id].get(emoji.demojize(payload.emoji.name)) != None:
            role = get(self.client.get_guild(payload.guild_id).roles, id=RolePicker.messages[payload.message_id][emoji.demojize(payload.emoji.name)])
            await payload.member.add_roles(role)
    
    # Removing the role
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id in RolePicker.messages and RolePicker.messages[payload.message_id].get(emoji.demojize(payload.emoji.name)) != None:
            role = get(self.client.get_guild(payload.guild_id).roles, id=RolePicker.messages[payload.message_id][emoji.demojize(payload.emoji.name)])
            await self.client.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(role)

def setup(client):
    client.add_cog(RolePicker(client))