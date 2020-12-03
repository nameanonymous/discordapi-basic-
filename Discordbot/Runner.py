'''
Created on 2020/12/03

@author: Masaya Misaizu
'''

import discord
#TOKEN = 'token which you will use in here'
#comment out when you use this!
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in')

@client.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == 'Hello!':
        await message.channel.send('Hi!')
    if client.user in message.mentions: 
        await reply(message)
    print(get_data(message))         
@client.event
async def reply(message):
    reply = f'Did you call me,{message.author.mention}?' 
    await message.channel.send(reply) 

@client.event
def get_data(message):
    command = message.content
    data_table = {
        '/members': message.guild.members, 
        '/roles': message.guild.roles, 
        '/text_channels': message.guild.text_channels, 
        '/voice_channels': message.guild.voice_channels, 
        '/category_channels': message.guild.categories, 
            }
    return data_table.get(command, 'Invalid command! Check Runner.py to see what code can use.')

