from keep_alive import keep_alive
from useful_functions import *
import discord
from discord.ext import tasks, commands
import get_token
import logging
import datetime
import json

logging.basicConfig(filename="discord.log", level=logging.DEBUG, format= "| {asctime} | {levelname:<8} > {message}", style="{",filemode="w")

BIRTHDAY_CHANNEL_ID = 901960741391839282
GENERAL_CHANNEL_ID = 787873019535163396
BOT_TEST_CHANNEL_ID = 953752125786173491

BOT_USER_ID = 953674224998953000
MFT_USER_ID = 285993498719682564
LUIS_USER_ID = 183743234084700160
YTALLO_USER_ID = 258282936313446401
GHOSSERT_USER_ID = 267423617078394883
ALPHEXX_USER_ID = 393555316765360128
GUILHERME_USER_ID = 258765854504648704

WILLYREX_IMAGES = ["https://cdn.discordapp.com/attachments/821787696217063455/953767041326809098/unknown.png", "https://cdn.discordapp.com/attachments/821787696217063455/934557388122517605/938433.png"]

def debug(msg):
    logging.debug(msg)
def error(msg):
    logging.debug(msg)

def open_token():
    return get_token.open_token()


      
# Documentaton : https://discordpy.readthedocs.io/en/stable/search.html
class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}")
        self.bot_user : discord.User = await client.fetch_user(BOT_USER_ID)
        #self.happy_birthday.start()
      
    async def on_message(self, msg:discord.Message):
        if msg.author.id == self.bot_user.id:
          return
      
        # Check if message is Happy Birthday
        msg_lower = str(msg.content).lower()
        if "feliz aniversario" in msg_lower.replace("á", "a"):
            await self.send_message(msg.channel.id, f"**obrigado chaves.**")

        if "obrigado chaves" in msg_lower:
            await self.send_message(msg.channel.id, f"**de nada quico.**")
        
        if check_word_exists("mix", msg_lower) == True:
            user : discord.User = await client.fetch_user(YTALLO_USER_ID)
            await self.send_message(msg.channel.id, f"{user.mention}")

        if check_word_exists("sus", msg_lower) == True:
            user : discord.User = await client.fetch_user(ALPHEXX_USER_ID)
            await self.send_message(msg.channel.id, f"{user.mention}")
            
        if check_word_exists("tuyu", msg_lower) == True:
            user : discord.User = await client.fetch_user(GHOSSERT_USER_ID)
            await self.send_message(msg.channel.id, f"{user.mention} \U0001f5ff\U0001f5ff\U0001f5ff\U0001f5ff")
        
        # Willyrex functions
        if "willy" in msg_lower or check_word_exists("rex", msg_lower) == True:
            
            await self.send_message(msg.channel.id, f"{get_random_list_value(WILLYREX_IMAGES)}")

        # Guilherme functions
        if "filmin" in msg_lower:
            user : discord.User = await client.fetch_user(GUILHERME_USER_ID)
            await self.send_message(msg.channel.id, f"{user.mention}")
            
        
        print(f"Message from {msg.author}: {msg.content}")
                        
    async def send_message(self, channel_id, msg):
        channel = client.get_channel(channel_id)
        await channel.send(msg)
        
    @tasks.loop(hours=1)    
    async def happy_birthday(self):
        today = datetime.date.today().strftime("%d/%m/%Y")
        check_date = check_if_date_exists(today) 
        
        if check_date == False:
            mft_user : discord.User = await client.fetch_user(MFT_USER_ID)
            CHANNEL = BIRTHDAY_CHANNEL_ID
            MSG = f"Feliz aniversário, {mft_user.mention} \U0001F973\U0001F973\U0001F974"
        
            await self.send_message(CHANNEL, MSG)
      
TOKEN = open_token()


keep_alive()

client = MyClient()
client.run(TOKEN)