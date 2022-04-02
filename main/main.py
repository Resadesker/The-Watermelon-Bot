import discord
from discord.ext import commands
from discord.utils import get
from datetime import datetime
import asyncio
import psycopg2
from psycopg2.sql import SQL
from psycopg2.sql import Identifier
import config

token = config.token
defaultPrefix = config.defaultPrefix
embedColor = discord.Colour.green()

dbConfigs = config.configDB
dbHost = dbConfigs["host"] #Change
db = dbConfigs["database"] #Change
dbUser = dbConfigs["user"] #Change
dbPassword = dbConfigs["password"] #Change
dbPort = dbConfigs["port"] #Change
con = psycopg2.connect(database=db, user=dbUser, password=dbPassword, host=dbHost, port=dbPort)
con.autocommit = True
cur = con.cursor()
#cur.execute(SQL().format(Identifier()), (, )) #USE THIS TO PREVENT SQL INJECTION
print("--DATABASE OPENED--")

#---------Database Functions---------
def selectAllTable(table : str):
    cur.execute(SQL("SELECT * FROM {};").format(Identifier(table)))
    data = cur.fetchall()

    return data

def selectDbByUserid(table : str, userid : str):
    cur.execute(SQL("SELECT * FROM {} WHERE userid = %s;").format(Identifier(table)), (userid, ))
    data = cur.fetchall()

    if (data == []):
        return None

    return data[0]

def selectDbByName(table : str, name : str):
    cur.execute(SQL("SELECT * FROM {} WHERE name = %s;").format(Identifier(table)), (name, ))
    data = cur.fetchall()

    if (data == []):
        return None

    return data[0]

def selectDbByGuildid(table : str, guildid : str):
    cur.execute(SQL("SELECT * FROM {} WHERE guildid = %s;").format(Identifier(table)), (guildid, ))
    data = cur.fetchall()

    if (data == []):
        return None

    return data[0]

def selectDbByMsgid(table : str, msgid : str):
    cur.execute(SQL("SELECT * FROM {} WHERE msgid = %s;").format(Identifier(table)), (msgid, ))
    data = cur.fetchall()

    if (data == []):
        return None

    return data[0]

def deleteDbByGuildid(table : str, guildid : str):
    cur.execute(SQL("DELETE FROM {} WHERE guildid = %s;").format(Identifier(table)), (guildid, ))
    con.commit()

def deleteDbByMsgid(table : str, msgid : str):
    cur.execute(SQL("DELETE FROM {} WHERE msgid = '%s;").format(Identifier(table)), (msgid, ))
    con.commit()

def deleteDbByName(table : str, name : str):
    cur.execute(SQL("DELETE FROM {} WHERE name = %s;").format(Identifier(table)), (name, ))
    con.commit()

def insertDbPrefixes(guildid : str, prefix : str = defaultPrefix):
    cur.execute("INSERT INTO prefixes (guildid, prefix) VALUES (%s, %s);", (guildid, prefix))
    con.commit()

def updateDbPrefixes(guildid : str, prefix : str = defaultPrefix):
    cur.execute("UPDATE prefixes SET prefix = %s WHERE guildid = %s;", (prefix, guildid))
    con.commit()


#------------------------------------------------------------

def getPrefix(client, message):
    prefix = selectDbByGuildid("prefixes", str(message.guild.id))
    pfx = prefix[1]
    return [pfx, str.upper(pfx), str.lower(pfx)]

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=getPrefix, intents=intents, case_insensitive=True, help_command=None)

@client.event
async def on_guild_join(guild):  #When joins a guild
    insertDbPrefixes(str(guild.id))


@client.event
async def on_guild_remove(guild):  #When removes from a guild
    deleteDbByGuildid("prefixes", str(guild.id))

def GetAvatarLink(link):
    return link[0:(len(link)-15)]

@client.command()
#@commands.has_permissions(administrator=True) #User must have administrator permission
async def changePrefix(ctx, prefix=None): #changes prefix
    guild = ctx.guild
    data = selectDbByGuildid("prefixes", str(guild.id))

    if(data != None):
        oldPrefix = data[1]
        if(prefix):
            updateDbPrefixes(str(guild.id), str(prefix))
            prefix = str(prefix)
        else:
            updateDbPrefixes(str(guild.id), defaultPrefix)
            prefix = defaultPrefix

        embed = discord.Embed(
            colour=embedColor
        )
        avatarUrl = GetAvatarLink(str(ctx.author.avatar_url))
        embed.set_author(name=ctx.author.name,
                         icon_url=avatarUrl)
        embed.add_field(name="Prefix Changed", value=f"Prefix has been changed \"{oldPrefix}\" to \"{prefix}\".",
                        inline=False)

    await ctx.send(embed=embed)



#-------------------------------------------------------------
client.run(token)

"""#EMBED TEMPLATE
    embed = discord.Embed(
        title="Title",
        description="This is a description",
        colour=embedColor
    )
    embed.set_footer(text="This is a footer.")
    embed.set_image(url="https://cdn.discordapp.com/attachments/520265639680671747/533389224913797122/rtgang.jpeg")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/520265639680671747/533389224913797122/rtgang.jpeg")
    embed.set_author(name="Author Name",
                     icon_url="https://cdn.discordapp.com/attachments/520265639680671747/533389224913797122/rtgang.jpeg")
    embed.add_field(name="Field Name", value="Field Value", inline=False)
    embed.add_field(name="Field Name", value="Field Value", inline=True)
    embed.add_field(name="Field Name", value="Field Value", inline=True)
    await ctx.send(embed=embed)
"""
