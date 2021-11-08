import discord
from discord.ext import commands
from config import settings
import json
import requests
import random 
from discord import message
from importlib.metadata import files
from pip._vendor.urllib3 import response



bot = commands.Bot(command_prefix = settings['prefix']) #Бот откликается на наш префикс установленный в config файле

gold_namber = random.randint(1, 99) # Выбираем победное число для нашей игры (послядняя команда)
print(str(gold_namber))




@bot.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON
    embed = discord.Embed(color = 0x00FFFF	, title = 'Random Fox') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed
    

@bot.command() # Игра Орёл или Решка
async def flip(ctx):
    author = ctx.message.author
    N = ('Орёл', 'Решка')
    M = random.choice(N)
    await ctx.send(M)

@bot.command() # Случайный выбор из данного списка (если, например, часто спорите из-за игры или фильма)
async def choic(ctx):
    Name = ('')
    NameChoic = random.choice(Name)
    await ctx.send('Выбрано: '+ NameChoic)


@bot.command()
async def cat(ctx):
    response = requests.get('https://some-random-api.ml/img/cat') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON
    embed = discord.Embed(color = 0xff9900, title = 'Random Cat') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

@bot.command()
async def dog(ctx):
    response = requests.get('https://some-random-api.ml/img/dog') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON
    embed = discord.Embed(color = 0x1A00FF, title = 'Random Dog') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

@bot.command()
async def randoms(ctx): # сообщение с запросом  на случайное число
    ran = random.randint(0, 100) # выбираем число
    if ran == gold_namber: # проверяем на равенство числу, которое выбрали мы
        N = ('Ваше число: ' + str(ran)+ ' Это золотое число! Вы победили!') # В случае соответствия
    else:
        N = ('Ваше число: ' + str(ran)) # В случае НЕ соответствия 
    await ctx.send(N) #Отправляем результат 

bot.run(settings['token']) #Подключение бота через токен из файла config