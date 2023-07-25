import os
import json
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

with open("config.json", "r") as f:
    config = json.load(f)

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix=config["Prefix"], intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

client.run(os.getenv("DISCORD_TOKEN"))