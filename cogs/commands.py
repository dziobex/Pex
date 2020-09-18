from discord.ext import commands

class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.client.user} is online')

    @commands.command(name="ping")
    async def ping(self, ctx):
        await ctx.send('pong!')

def setup(client):
    client.add_cog(Commands(client))