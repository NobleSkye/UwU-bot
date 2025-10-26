# UwU Bot Docker Setup

A Discord bot that reacts to "uwu" messages, now containerized with Docker Compose.

## Setup

1. **Copy environment file:**
   ```bash
   cp .env.example .env
   ```

2. **Edit the `.env` file with your actual Discord bot token:**
   ```bash
   # Your Discord bot token (REQUIRED)
   DISCORD_TOKEN=your_actual_bot_token_here
   
   # Channel ID where the bot should operate (optional)
   CHANNEL_ID=1376519136762658948
   
   # Custom emoji ID for reactions (optional)
   CUSTOM_EMOJI_ID=1353062179158626337
   ```

3. **Build and run the bot:**
   ```bash
   docker-compose up -d
   ```

## Commands

- **Start the bot:** `docker-compose up -d`
- **Stop the bot:** `docker-compose down`
- **View logs:** `docker-compose logs -f uwu-bot`
- **Rebuild after changes:** `docker-compose up --build -d`

## Features

- Runs in an isolated Docker environment
- Automatic restart if the bot crashes
- Environment variable configuration for security
- Proper logging setup
- Non-root user for enhanced security

## Bot Behavior

- Reacts with custom emoji when users post "uwu"
- Reacts with ❌ if the same user posts "uwu" twice in a row
- Reacts with ❌ for any other message in the configured channel