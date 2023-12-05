# README for Telegram Bot Script

## Overview
This script creates a simple Telegram bot using Python's `telegram.ext` module. The bot features basic commands and message forwarding capabilities.

## Features
- **Start Command**: Greets the user with a personalized message.
- **Help Command**: Provides a generic help message.
- **Message Forwarding**: Automatically forwards received messages to a predefined target chat.

## Requirements
- Python 3.6 or higher.
- `python-telegram-bot` library.

## Installation
1. Install `python-telegram-bot` via pip:
   ```
   pip install python-telegram-bot
   ```

2. Clone or download this script to your local machine.

## Setup
1. Obtain a bot token from the @BotFather on Telegram.
2. Replace `'YOUR_BOT_TOKEN'` in the script with your actual bot token.
3. Set the `TARGET_CHAT_ID` to the desired chat ID where messages should be forwarded.
4. Do not forget to give bot access to massage it @Botfather.

## Usage
1. Run the script:
   ```
   python bot_script.py
   ```
2. Interact with your bot on Telegram using the supported commands.

## Commands
- `/start` - Sends a welcome message.
- `/help` - Displays help information.
- Any text message (not a command) will be forwarded to the specified target chat.

## Logging
The script uses Python's `logging` module for logging basic information.

## Notes
- Do not share your bot token.
- Ensure the bot has the necessary permissions in any chats it is part of.

## Disclaimer
This script is for educational purposes. The author is not responsible for any misuse or damage.
