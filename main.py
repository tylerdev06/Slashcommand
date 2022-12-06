import discord 
from discord.ext import commands
import random
from botconfig import TOKEN
from discord import app_commands

bot = commands.Bot(command_prefix='!', intents = discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot ist Online!")
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} Commands synchronisiert")
    except Exception as e:
        print(e)


@bot.tree.command(name="würfel")
@app_commands.describe(seiten = "Wie viele Seiten soll ich haben?")
async def Würfel(ctx, seiten:int=6):
    await ctx.response.send_message(f"Du hast eine {random.randint(1, seiten)} gewürfelt.")



bot.run(TOKEN)