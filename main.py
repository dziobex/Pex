import os, discord
from discord.ext import commands

client = commands.Bot(command_prefix='px ', help_command=None)

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "general" or str(channel) == "ogólny":
            await channel.send(f"Hello {member.mention}! :wave:")

@client.event
async def on_member_remove(member):
    for channel in member.guild.channels:
        if str(channel) == "general" or str(channel) == "ogólny":
            await channel.send(f"Bye {member.mention}! :wave:")

if __name__ == '__main__':
    client.run('token')
