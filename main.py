import os
from discord.ext import commands

client = commands.Bot(command_prefix='px ')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

if __name__ == '__main__':
    client.run('NzU1NzQwNDQwNzYxNzI5MDk1.X2HsIg.Yv2hjQQeZwcbaPg4-gLbL9mYlNE')