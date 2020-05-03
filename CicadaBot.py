import discord
from discord import Member
from discord.ext import commands 
import json
import platform
from datetime import datetime as dt
import os 
from pathlib import Path

DISCORDPY = f"v{discord.__version__}"
CICADABOT = "v1.0"
PYTHON = platform.python_version()
CREATOR = "pyrrh0"
COLOR = discord.Color(0x000000)
PRE = "/"


bot = commands.Bot(command_prefix=PRE)
bot.remove_command('help')

with open("src/auth.json") as auth:
    auth_token = json.load(auth)
    AUTH_TOKEN = auth_token["token"]

with open("src/commands.json") as cmd_file:
    command_list = json.load(cmd_file)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('Liber Primus'))
    print("####################")
    print("CicadaBot is online!")
    print("####################")

# @bot.event
# async def on_command_error(ctx, error):
#     if isinstance(error, commands.CommandNotFound):
#         embed = discord.Embed(title="Error", color=discord.Color(0xff0000), description="The command you entered is invalid or doesn't exist")
#         await ctx.send(embed=embed)
#     elif isinstance(error, commands.CommandInvokeError):
#         embed = discord.Embed(title="Error", color=discord.Color(0xff0000), description="The command can't be used here")
#         await ctx.send(embed=embed)
@bot.command()
async def noob(ctx):
    embed = discord.Embed(title="Noob Guide",color=COLOR, description="Here are a few questions you might have that we're all very exhausted with answering")
    embed.add_field(name="Q: I'm new, where should I ...", value="A: read the wiki. Read The Wiki. [READ THE WIKI!](https://uncovering-cicada.fandom.com/wiki/Uncovering_Cicada_Wiki)", inline=False)
    embed.add_field(name="Q: Is this post I found from Cicada?", value="A: Most probably not. But if you're sure, verify it with this [tool](https://isitcicada.challenge.pt/)", inline=False)
    embed.add_field(name="Q: I have an idea, what should I do?", value="A: Check if it's been done. If not, go ahead and try it out, also don't forget to report on your findings", inline=False)
    embed.add_field(name="Q: Where are you with solving the liber primus?", value="A: \"Somewhere between the beiginning and end\" ~ Puck", inline=False)
    embed.add_field(name="Q: I have no programming experience?", value="A: That's okay. Maybe try learn one like Python, C/C++ or Ruby", inline=False)
    embed.add_field(name="Q: I have no knowledge on cryptography?", value="A: Go check out #important-links. There you'll find excellent resources on getting started", inline=False)
    await ctx.send(embed=embed)

# [HELP]
@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="Help Menu", color=COLOR)
    embed.add_field(name=f"  `{PRE}about`  ", value="Returns some basic information about the bot and the server", inline=False)
    # embed.add_field(name=f"  `{PRE}fandom` ", value="Gives the link to the Uncovering Cicada Fandom", inline=False)
    embed.add_field(name=f"  `{PRE}help`   ", value="Returns the help menu", inline=False)
    embed.add_field(name=f"  `{PRE}lp <p>` ", value="Shows an image of the unmodified page <p> of the Liber Primus (Pg 00-74). If no page is given the first page is shown", inline=False)
    embed.add_field(name=f"  `{PRE}noob` ", value="Shows common questions that new members might have", inline=False)
    embed.add_field(name=f"  `{PRE}profile` ", value="Shows basic information about the member who invoked the command", inline=False)
    embed.add_field(name=f"  `{PRE}reddit` ", value="Gives the link to the subreddit: r/CicadaSolvers. Old subreddit is just a no no", inline=False)
    embed.add_field(name=f"  `{PRE}report` ", value="Allows user to report abuse of the bot or its feautres", inline=False)
    embed.add_field(name=f"  `{PRE}suggest`   ", value="Allows user to suggest feature or functionality to the bot creator", inline=False)
    embed.add_field(name=f"  `{PRE}wekan`  ", value="Gives the link of the Cicada WeKan Board", inline=False)
    embed.add_field(name=f"  `{PRE}wiki`   ", value="Gives the link to the Uncovering Cicada Fandom, the main wiki", inline=False)
    await ctx.send(embed=embed)

# [ABOUT] - Busy
###########################################
@bot.command()
async def about(ctx):
    embed = discord.Embed(title="CicadaBot", color=COLOR)
    embed.set_thumbnail(url=f"{bot.user.avatar_url}")
    embed.add_field(name="Creator:", value=CREATOR)
    embed.add_field(name="Discord.py:", value=DISCORDPY)
    embed.add_field(name="Python:", value=PYTHON)
    embed.add_field(name="Bot:", value=CICADABOT)
    await ctx.send(embed=embed)

# # [WIKI] - Done
# @bot.command()
# async def wiki(ctx):
#     url = command_list.get("wiki")
#     description = f"The new wiki used to help both veterans and newcomers alike.\nStill a work in progress! Try `{PRE}fandom` instead"
#     embed = discord.Embed(title="Cicada Wiki", url=url, description=description, color=COLOR)
#     embed.set_thumbnail(url=f"{bot.user.avatar_url}")
#     # await ctx.send(embed=embed)

# [WEKAN] - Done
@bot.command()
async def wekan(ctx):
    url = command_list.get("wekan")
    description = "Read the wiki? Have some ideas? Come check out the WeKan board and find something to do."
    embed = discord.Embed(title="WeKan Board", url=url,
                          description=description, color=COLOR)
    embed.set_thumbnail(url=f"{bot.user.avatar_url}")
    await ctx.send(embed=embed)

# [REDDIT] - Done
###########################################
@bot.command()
async def reddit(ctx):
    description = "The new subreddit is for sharing ideas online. No shitposting here as the server is moderated *heavily*"
    url = command_list.get("reddit")
    embed = discord.Embed(title="r/CicadaSolvers", url=url, description=description, color=COLOR)
    embed.set_thumbnail(url=f"{bot.user.avatar_url}")
    await ctx.send(embed=embed)

# [WIKI] - Done
###########################################
@bot.command()
async def wiki(ctx):
    description = f"The original wiki. This is the main source of information on past solving attempts and should be read by all new members"
    url = command_list.get("wiki")
    embed = discord.Embed(title="Uncovering Cicada Fandom", url=url, description=description, color=COLOR)
    embed.set_thumbnail(url=f"{bot.user.avatar_url}")
    await ctx.send(embed=embed)

# [LP] - Done
###########################################
@bot.command()
# Thanks Taiiwo :p
async def lp(ctx, page="00"):
    page = str(page)
    root_dir = "src/lp_unmodified"
    if page.isnumeric() and len(page) == 2:
        path = os.path.join(root_dir,f"{page}.jpg")
        image = discord.File(path)
        await ctx.send(file=image)
    else:
        raise discord.errors.InvalidArgument

# Suggest
@bot.command()
async def suggest(ctx, *,user_suggestion):
    submit = bot.get_user(682582262184804363)
    user = ctx.author
    thumbnail = str(user.avatar_url)
    
    embed = discord.Embed(title="Suggestion:")
    embed.set_thumbnail(url=thumbnail)
    embed.add_field(name=f"Suggestion:", value=user_suggestion, inline=False)
    embed.add_field(name="From:", value=user, inline=False)

    embed2 = discord.Embed()
    embed2.set_thumbnail(url=thumbnail)
    embed2.add_field(name=f"Suggestion:", value=user_suggestion, inline=False)
    embed2.add_field(name="From:", value=user, inline=False)
    embed2.set_author(name="Your suggestion has been submitted")
    await submit.send(embed=embed)
    await ctx.send(embed=embed2)

# Report
@bot.command()
async def report(ctx, *,report):
    submit = bot.get_user(682582262184804363)
    user = ctx.author
    thumbnail = str(user.avatar_url)
    
    embed = discord.Embed(title="Report:")
    embed.set_thumbnail(url=thumbnail)
    embed.add_field(name=f"Report:", value=report, inline=False)
    embed.add_field(name="From:", value=user, inline=False)

    embed2 = discord.Embed()
    embed2.set_thumbnail(url=thumbnail)
    embed2.add_field(name=f"Report:", value=report, inline=False)
    embed2.add_field(name="From:", value=user, inline=False)
    embed2.set_author(name="Your report has been submitted")
    await submit.send(embed=embed)
    await ctx.send(embed=embed2)

# Profile
@bot.command()
async def profile(ctx):
    user = ctx.author
    pfp = user.avatar_url
    created = user.created_at
    joined = user.joined_at
    embed = discord.Embed()
    embed.set_thumbnail(url=pfp)
    embed.add_field(name="Account created on:", value=created.strftime("%B %d %Y, %H:%M "), inline=False) 
    embed.add_field(name="Joined on:", value=joined.strftime("%B %d %Y, %H:%M "), inline=False) 
    await ctx.send(embed=embed)
    
## Other Commands To Be Added ##

bot.run(AUTH_TOKEN)
