import discord
import os
import random
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def guess(ctx):
    await ctx.send('Guess a number between 1 and 10.')


@bot.command()
async def mem(ctx):
    images = os.listdir('images')
    with open('images/'+random.choice(images), 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

@bot.command()
async def answer(ctx, n):
    if n == random.randint(1, 10):
        await ctx.send("Good job!!!")
    else:
        await ctx.send("You're wrong!!!")

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''After we call the duck command, the program will call the get_duck_image_url function'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run("token")
