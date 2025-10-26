import os
import logging
import discord
from dotenv import load_dotenv

# Configure logging early so discord.py logs are visible
logging.basicConfig(level=logging.INFO)

# Load environment variables
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID", "1431350380129812643"))
CUSTOM_EMOJI_ID = int(os.getenv("CUSTOM_EMOJI_ID", "1353062179158626337"))

print("Environment variables loaded:")
print(f"TOKEN exists: {'Yes' if TOKEN else 'No'}")
print(f"CHANNEL_ID: {CHANNEL_ID}")
print(f"CUSTOM_EMOJI_ID: {CUSTOM_EMOJI_ID}")

# Validate required environment variables
if not TOKEN:
    raise ValueError("DISCORD_TOKEN environment variable is required")

# Intents
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Required to read message text
intents.guilds = True           # Required to access guild information
intents.reactions = True        # Not strictly needed to add reactions, but fine

# Client
client = discord.Client(intents=intents)

last_user_id = None

@client.event
async def on_ready():
    print(f"Logged in as {client.user} (ID: {client.user.id})")
    print(f"Bot is in {len(client.guilds)} guilds")
    print("------")
    print("Bot is ready and listening for messages!")

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

if __name__ == "__main__":
    print("Starting bot...")
    print(f"Monitoring channel ID: {CHANNEL_ID}")
    print(f"Using custom emoji ID: {CUSTOM_EMOJI_ID}")
    try:
        client.run(TOKEN, log_level=logging.INFO)
    except Exception as e:
        logging.exception("Failed to start bot: %r", e)
        raise