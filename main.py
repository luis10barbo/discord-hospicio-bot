from keep_alive import keep_alive
from useful_functions import *
import discord
from discord.ext import tasks, commands
import get_token
import logging
import datetime
from os import system


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
            await self.send_message(msg.channel.id, f"Miqqqqqqqqs galera")

        if check_word_exists("sus", msg_lower) == True:
            user : discord.User = await client.fetch_user(ALPHEXX_USER_ID)
            await self.send_message(msg.channel.id, f"{user.mention}")
            
        if check_word_exists("tuyu", msg_lower) == True:
            user : discord.User = await client.fetch_user(GHOSSERT_USER_ID)
            await self.send_message(msg.channel.id, f"TUYUUUUUUUUUUUUUUUU??????????????? \U0001f5ff\U0001f5ff\U0001f5ff\U0001f5ff")
            
        if check_word_exists("840", msg_lower) == True or check_word_exists("R$840", msg_lower) == True:
            await self.send_message(msg.channel.id, f"Thominhas ♡\nhttps://www.guiadoscuriosos.com.br/wp-content/uploads/2021/03/default_fotoGenetica_58a1f4e712dd3_13-02-2017_16-03-19.jpg")

        if check_word_exists("gatinho", msg_lower) == True:
            await self.send_message(msg.channel.id, "meu gato\n" + get_random_list_value([
                "https://cdn.discordapp.com/avatars/183743234084700160/0749b7015f48656a22424dc8b9cd5011.png?size=1024", 
                "https://img-9gag-fun.9cache.com/photo/aog0nAn_460s.jpg",
                "https://static.wikia.nocookie.net/floppapedia-revamped/images/b/bb/Fat_Bingus.png/revision/latest/top-crop/width/360/height/450?cb=20210729011304",
                "https://64.media.tumblr.com/5b4dd14219f7778603f8ebd80af4910f/f1a2562118c069ab-af/s640x960/45220ef3d05c99d1c3a5fbca41cbdf2ba0697e33.jpg",
                "https://cdn.discordapp.com/attachments/821787696217063455/953767041326809098/unknown.png",
                "https://cdn.discordapp.com/attachments/821787696217063455/934557388122517605/938433.png",
                                                                           ]))
            
        if check_word_exists("pk", msg_lower) == True or "dumsleier" in msg_lower or "<@!300439218562531328>" in msg_lower:
            await self.send_message(msg.channel.id, "**Você quis dizer:**\n" + get_random_list_value([
                "https://wallpapercave.com/wp/wp8540475.jpg",
                "https://i.pinimg.com/originals/1f/fe/ae/1ffeae5a14d7b6ecf127ba60050f8418.jpg",
                "https://w0.peakpx.com/wallpaper/268/379/HD-wallpaper-fate-series-fate-apocrypha-anime-boys-braided-hair-fgo-femboy-bicolored-hair-black-ribbons-white-hair-pink-hair-2d-astolfo-fate-apocrypha-anime-open-mouth-purple-jacket-striped-clothing.jpg",
                "http://3.bp.blogspot.com/_2ae6xTLKBJ8/SHoKoW4pBZI/AAAAAAAACG0/0248GAAtB94/w1200-h630-p-k-no-nu/bombado.jpg",
                "https://cdn.myanimelist.net/images/anime/12/39497.jpg",
                "https://www.animeunited.com.br/oomtumtu/2019/05/thumb-1920-835255.jpg",
                "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjIaePiT3vNuFEBxGJZctETv0RzY2t2UX52A&usqp=CAU",
                "https://cdn.discordapp.com/attachments/670253872345907212/954813096147451974/American_Psycho_-_Patrick_Bateman.png",
                "https://cdn.discordapp.com/attachments/670253872345907212/954813166360096858/3112903.png",
                "https://cdn.discordapp.com/attachments/670253872345907212/954813387471220786/9aba3993b2a72f1866fdc8d7ac348cdf.png",
                "https://criticalhits.com.br/wp-content/uploads/2020/02/Berserk.jpeg",
                "https://static.wikia.nocookie.net/youkoso-jitsuryoku-shijou-shugi-no-kyoushitsu-e/images/b/bf/Episode_012-07.jpg/revision/latest/scale-to-width-down/1599?cb=20170928143111",
                "https://cdn.discordapp.com/attachments/670253872345907212/954813606166421584/230px-God_of_warPS4.png",
                "https://cdn.discordapp.com/attachments/670253872345907212/954813736886075452/latest.png",
                "https://cdn.discordapp.com/attachments/670253872345907212/954813906856067082/latest.png",
                "https://cdn.discordapp.com/attachments/670253872345907212/954814084510023750/450.png",
                "https://w7.pngwing.com/pngs/299/463/png-transparent-saitama-illustration-one-punch-man-ikkaku-madarame-anime-manga-saitama-one-punch-man-comics-cg-artwork-superhero-thumbnail.png",
                "https://media.discordapp.net/attachments/670253872345907212/954814259919986718/220px-John_Rambo.png",
                "https://cdn.discordapp.com/attachments/670253872345907212/954814337296523264/2f45fe73481891665b88c29d7a18a730bb5d6954_00.png",
                "https://media.discordapp.net/attachments/670253872345907212/954814472474742875/image.png",
                "https://i.kym-cdn.com/photos/images/facebook/001/330/809/d90.png",
                "https://cdn.discordapp.com/attachments/670253872345907212/954814830458601552/latest.png",
                "https://cdn.discordapp.com/attachments/670253872345907212/954814953498509312/texto1.png",
                "https://cdn.discordapp.com/attachments/670253872345907212/954815078354526228/master_chief_in_halo_4-1600x900_zLf7osr.png",
                "https://cdn.discordapp.com/attachments/670253872345907212/954815435621171210/HITMANE284A2_20160314214125.png",
                "https://cdn.discordapp.com/attachments/670253872345907212/954815627707695184/50.png",
                "https://cdn.discordapp.com/attachments/670253872345907212/954815732607246356/Destaque_Stefano_JetstreamSam.png",
                "mano o pk literalmente mandou umas 30 imagem pra eu colocar aqui, duvido q alguem pegue essa mensagem",
                "https://cdn.discordapp.com/attachments/670253872345907212/954815899041431562/Dead-Space-1.png",
                "https://cdn.discordapp.com/attachments/670253872345907212/954815994214363186/latest.png",
                "https://cdn.discordapp.com/attachments/670253872345907212/954816084870037605/maxresdefault.png",
                "https://cdn.discordapp.com/attachments/670253872345907212/954816180059766854/maxresdefault.png",
                "https://cdn.discordapp.com/attachments/670253872345907212/954816267179687996/6d608b3608d83841a225bd44d72551b0.png"
                "https://i.pinimg.com/originals/6d/51/d2/6d51d25c4d9df845bdddcaaeb8eaa719.jpg" ,
                "https://i.ytimg.com/vi/NRpNHcniTfE/maxresdefault.jpg" ,
                "https://static.wikia.nocookie.net/metalgear/images/1/16/Venom_Snake.Motherbase.jpg/revision/latest?cb=20210324042507" ,
                "http://4.bp.blogspot.com/-r3Y33rd59RM/TcQbVHeZUbI/AAAAAAAAA34/M580-j7WN8I/s1600/Alex+Mason+2.png" ,
                "https://static.wikia.nocookie.net/reddeadredemption/images/5/52/RDR2_Arthur_Morgan_Default.jpg/revision/latest?cb=20200602191534" ,
                "https://cdn.ome.lt/WsUApWyW816lb8owggex4NmJfrs=/1200x630/smart/extras/conteudos/Resident_Evil_4_Leom_s0Sbgie.jpg" ,
                "https://i.pinimg.com/originals/f6/99/9f/f6999fa0f04ab24b8dfe9321a9591be2.jpg" ,
                "https://images.gnwcdn.com/2013/articles/1/7/3/9/5/6/5/bloodborne-walkthrough-and-game-guide-1425044196532.jpg/EG11/resize/1200x-1/bloodborne-walkthrough-and-game-guide-1425044196532.jpg" ,
                "https://files.tecnoblog.net/meiobit/wp-content/uploads/2019/03/20190325sekiro-001.jpg" ,
                "https://static1.thegamerimages.com/wordpress/wp-content/uploads/2022/02/elden-ring.jpg" ,
                "https://observatoriodocinema.uol.com.br/wp-content/uploads/2021/07/dragon-ball-super-1200x900-1.jpg" ,
                "https://images2.alphacoders.com/433/thumb-1920-4330.jpg" ,
                "https://static.wikia.nocookie.net/villains/images/1/13/SCP-106Full.jpg/revision/latest/top-crop/width/360/height/450?cb=20220223203649&path-prefix=pt-br" ,
                "https://img.elo7.com.br/product/original/31BCFBF/placa-decorativa-mdf-jogos-mortais-billy-jigsaw-748-insidious.jpg" ,
                "https://i.ytimg.com/vi/TWB31WFomz4/maxresdefault.jpg" ,
                "https://i1.sndcdn.com/artworks-CdH7RBN6spzFjhZd-WPTsmw-t500x500.jpg"
                "https://pm1.narvii.com/5898/4feb67b1f519591f4c4177d4edd430ef22466982_hq.jpg" ,
                "https://taskandpurpose.com/uploads/2020/11/19035956-1.jpg?auto=webp" ,
                "https://img.ibxk.com.br/2020/05/21/21143121114239.jpg" ,
                "https://i.insider.com/5c47554a2bdd7f391532583b?width=700" ,
                "https://static.wikia.nocookie.net/berserk/images/8/8c/Nosferatu_Zodd_Mang%C3%A1.jpg/revision/latest?cb=20160308235957&path-prefix=pt-br" ,
                "https://i.kym-cdn.com/photos/images/original/002/206/094/06b.jpg",
                                                                           ]))
            
        # Willyrex functions
        if "willy" in msg_lower or check_word_exists("rex", msg_lower) == True:
            
            await self.send_message(msg.channel.id, f"{get_random_list_value(WILLYREX_IMAGES)}")

        # Guilherme functions
        if "filmin" in msg_lower:
            user : discord.User = await client.fetch_user(GUILHERME_USER_ID)
            await self.send_message(msg.channel.id, f"{user.mention}")
            
        
        
        print(f"Message from guild \"{msg.channel.guild.name}\" -> {msg.author}: {msg.content}")
                        
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
try:
    client.run(TOKEN)
except:
    print("Restarting")
    system("python restarter.py")
    system("kill 1")