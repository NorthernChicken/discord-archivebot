# discord-archivebot
A Discord bot that makes and stores an archive of every message sent in a Discord text channel. Still under development.

# How to install
## Requirements
- [Python 3.12]([url]https://www.python.org/downloads/)
- A [Discord Developer Portal]([url]https://discord.com/developers/applications) Account

## Setup
_Basic Python and Discord bot knowledge may be required for setup._
1. Download this repo (big green button "code", download zip). Unzip the folder, open it, and open a terminal in that folder (right click+open terminal on Windows)
2. Install Discord Python library: `pip install discord.py`
3. Discord bot setup: go to the Discord Developer Portal, and create a new application. Click on "Bot," then "Bot permissions." Check "Administrator." Scroll up and reset token, then save it somewhere.
4. Enter the Discord bot token at the bottom of the bot.py script.
5. Invite the bot to your server in the Discord Developer portal - Go to your bot, click "installations," and check "Bot" and "Administrator." Copy the invite link to your browser and select the server you want to invite it to.
6. Send the message "!archive" in the text channel you want to archive.
7. The folder with the bot now has a subfolder called "message_archive" with the archived content.

# DISCLAIMERS
* This bot requires Administrator on your Discord server. This is a dangerous permission to give out. I am not doing anything malicious, but please check my code for yourself, don't take my word for it.
* Do not use this bot for malicious purposes, and only archive a server with the server member's consent. 
