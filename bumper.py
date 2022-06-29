import discord
import asyncio
import os
import json
from discord.ext import commands
from colorama import Fore

class Bumper:
  def __init__(self):
    pass

  @staticmethod
  def load_settings():
    """
    Loads and returns the bump_settings.json file
    """
    try:
      with open("bump_settings.json", "r+") as s:
        settings = json.load(s)
  
      return settings
    
    except FileNotFoundError:
      print(f"{Fore.RED}[-]{Fore.RESET} Couldn't find bump settings file.")
      print(f"{Fore.LIGHTBLACK_EX}[?]{Fore.RESET} Making one for you...")
      with open("bump_settings.json", "x") as s:
        channel_id = input(f"{Fore.LIGHTBLACK_EX}[?]{Fore.RESET} Please enter the AutoBump channel ID: ")
        default = f"""{{
    "AUTOBUMP_CHANNEL": {channel_id}
}}
"""
        s.write(default)
        print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Done.")
  
      with open("bump_settings.json", "r+") as s:
        settings = json.load(s)
  
        return settings
  
    except json.decoder.JSONDecodeError:
      with open("bump_settings.json", "r+") as s:
        default = """{
    "AUTOBUMP_CHANNEL": 0
}
"""
        s.write(default)
        
    with open("bump_settings.json", "r+") as s:
      settings = json.load(s)
  
      return settings

  @staticmethod
  async def get_slash_cmd(autobump):
    """
    Gets the bump command object in the autobump channel
    """
    async for slash in autobump.slash_commands(
      query = "bump",
      application = 302050872383242240
    ):
      bump = slash
  
    return bump

  @staticmethod
  async def send_bump(bump, count) -> None:
    """
    Sends the bump command in the autobump channel
    """
    await bump()
    count += 1
    print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Succesfully sent bump command - {count}")