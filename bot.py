import discord
from discord import Intents
import os

# Initialize intents
intents = Intents.all()
intents.messages = True

# Initialize the Discord client with intents
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    content = message.content.strip().lower()  # Remove leading/trailing whitespace and convert to lowercase
    if content == '!archive':
        channel = message.channel
        archive_folder = 'message_archive'
        os.makedirs(archive_folder, exist_ok=True)
        
        # Archive text messages
        async for msg in channel.history(limit=None):
            with open(f'{archive_folder}/{channel.name}_archive.txt', 'a', encoding='utf-8') as file:  # Specify UTF-8 encoding
                try:
                    file.write(f'{msg.created_at} - {msg.author}: {msg.content}\n')
                except UnicodeEncodeError:
                    print(f"Skipping message with Unicode characters: {msg.content}")
        
        # Archive images
        for attachment in message.attachments:  # Iterate over message attachments using a regular for loop
            await attachment.save(f'{archive_folder}/{attachment.filename}')


# Run the bot
client.run('ENTER BOT TOKEN HERE')
