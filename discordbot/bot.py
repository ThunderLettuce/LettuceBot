# musicbot by Lettuce

import discord
import asyncio
from discord.ext import commands

TOKEN = 'NTU0MDI0OTI0MTMwNDQzMzE1.D2XH7w.yo10Diqwl37HXEUKtgS6r_vBlHU'

client = commands.Bot(command_prefix = '#')

@client.event
async def on_ready():
    print('We good, les go!')

@client.run(TOKEN)
