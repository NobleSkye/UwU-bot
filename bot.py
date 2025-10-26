import discord
# import asyncio
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID", "1376519136762658948"))
CUSTOM_EMOJI_ID = int(os.getenv("CUSTOM_EMOJI_ID", ":UwU:1353062179158626337"))

# Validate required environment variables
if not TOKEN:
    raise ValueError("DISCORD_TOKEN environment variable is required")

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Required to read message text

client = discord.Client(intents=intents)

last_user_id = None

@client.event
async def on_ready():
    print(f"Logged in as {client.user} (ID: {client.user.id})")
    print("------")

@client.event
async def on_message(message):
    global last_user_id

    # Ignore messages from bots or in other channels
    if message.author.bot or message.channel.id != CHANNEL_ID:
        return

    if message.content.strip().lower() == "uwu":
        if message.author.id == last_user_id:
            # User posted twice in a row
            await message.add_reaction("❌")
        else:
            # Correct message
            emoji = client.get_emoji(CUSTOM_EMOJI_ID)
            if emoji:
                await message.add_reaction(emoji)
            else:
                print("Custom emoji not found or not accessible")
            last_user_id = message.author.id
    else:
        # Not a valid "uwu" message
        await message.add_reaction("❌")

client.run(TOKEN)