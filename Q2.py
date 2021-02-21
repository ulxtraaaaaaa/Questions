import discord
import os 
import asyncio

client = discord.Client()

@client.event
async def on_ready():
  print(f"Username: {client.user.name}\nServers: {len(client.guilds)}\nUsers: {len(client.users)}")

client.run(os.environ.get("token"))
