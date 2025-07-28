import discord
import os
from datetime import datetime

TOKEN = os.getenv('DISCORD_BOT_TOKEN')
CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("📅 Reminder: Daily meeting at 6:00 PM. Please be prepared.")
    await client.close()

client.run(TOKEN)
