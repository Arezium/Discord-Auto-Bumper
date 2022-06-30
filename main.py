import discord
import asyncio
import os
from other import server
import json
from discord.ext import commands
from colorama import Fore
from bumper import Bumper
from config import Config

server.keep_alive()

CONFIG = Config()
print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Loaded config")

token = CONFIG.token
prefix = CONFIG.prefix
Bumper = Bumper()
print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Loaded Bumper class")

bot = commands.Bot(command_prefix=prefix, self_bot=True)
print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Loaded bot")



settings = Bumper.load_settings()
global count; count = 0
global channel_id; channel_id = settings["AUTOBUMP_CHANNEL"]
      
count = 0

@bot.event
async def on_connect():
  global count
  global ab

  print(f"Logged in {bot.user}")
  
  print(f"{Fore.LIGHTBLACK_EX}[?]{Fore.RESET} Getting the autobump channel ID...")
    
  try:
    autobump = bot.get_channel(channel_id)
    print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} AutoBump ID: {channel_id}\n")
    print(f"{Fore.LIGHTBLACK_EX}[?]{Fore.RESET} Getting the bump command object...")
    bump = await Bumper.get_slash_cmd(autobump)
    print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Succesfully got the bump command object.\n")

  except AttributeError:
    print(f"{Fore.RED}[-]{Fore.RESET} Failed to get the autobump channel. Make sure it's the correct ID.")
    exit()

  except UnboundLocalError:
    print(f"{Fore.RED}[-]{Fore.RESET} Failed to get the bump command object. Make sure you have permission and/or DISBOARD is in the server and it has slash command permissions.")
    exit()

  except Exception as e:
    print(f"{Fore.RED}[-]{Fore.RESET} An unknown error has happened while trying to get the bump command object. Please try running the bot again.\nError: {e}")
    exit()
    
  
  print(f"{Fore.LIGHTBLACK_EX}[?]{Fore.RESET} Starting bump loop...")
  while True:
    try:
      await Bumper.send_bump(bump, count)
      await asyncio.sleep(7200)

    except Exception as e:
      print(f"{Fore.RED}[-]{Fore.RESET} An unknown error has happened while trying to send the bump command.\nError: {e}")

bot.run(token)
