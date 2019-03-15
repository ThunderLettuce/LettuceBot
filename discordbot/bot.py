# musicbot by Lettuce

import asyncio
from itertools import cycle

import discord
from discord.ext import commands

TOKEN = 'NTU0MDI0OTI0MTMwNDQzMzE1.D2XyeA.MofqDQv5RDGznXHikfeRe0PjsOk'

client = commands.Bot(command_prefix="$")
client.remove_command('help')
status = ["Type $help for more info", "Welcome Frendo!", "Get em!"]


async def change_status():
    await client.wait_until_ready()
    msg = cycle(status)

    while not client.is_closed:
        current_status = next(msg)
        await client.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(120)


@client.event
async def on_ready():
    print('We good, les go!')


@client.event
async def on_message(message):
    print("A user has sent a message.")
    await client.process_commands(message)

@client.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    await client.send_message(channel, '{} has added {} to the message: {}'.format(user.name, reaction.emoji, reaction.message.content))

@client.event
async def on_reaction_remove(reaction, user):
    channel = reaction.message.channel
    await client.send_message(channel, '{} has removed {} from the message: {}'.format(user.name, reaction.emoji, reaction.message.content))

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_author(name='Help')
    embed.add_field(name='$ping', value='Returns Pong!', inline=False)
    embed.add_field(name='$echo', value='Copies what you say', inline=False)
    embed.add_field(name='$clear value', value='clears the defined amount of messages', inline=False)
    embed.add_field(name='$play', value='Searches YouTube for a song', inline=False)


    await client.send_message(author, embed=embed)


@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)


@client.command()
async def ping():
    await client.say('Pong!')

@client.command(pass_context=True)
async def join(ctx):
    #channel = ctx.channel.author.voice.voice_channel
    await client.join_voice_channel(channel)


@client.command()
async def echo(*args):
    output = ""
    for word in args:
        output += word
        output += " "
    await client.say(output)

@client.command
async def logout():
    await client.logout()


client.loop.create_task(change_status())
client.run(TOKEN)
