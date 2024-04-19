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
            with open(f'{archive_folder}/{channel.name}_archive.txt', 'a', encoding='utf-8') as file:
                try:
                    file.write(f'{msg.created_at} - {msg.author}: {msg.content}\n')
                    if msg.attachments:  # Check attachments of the current message
                        with open(f'{archive_folder}/{channel.name}_archive.txt', 'a', encoding='utf-8') as file:
                            for attachment in msg.attachments:
                                filename = attachment.filename
                                file.write(f'{msg.created_at} - {msg.author}: {filename}\n')
                                await attachment.save(f'{archive_folder}/{filename}')  # Save image
                except UnicodeEncodeError:
                    print(f"Skipping message with Unicode characters: {msg.content}")

# Run the bot
client.run('ENTER BOT TOKEN HERE')
