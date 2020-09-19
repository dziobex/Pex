from discord.ext import commands
import discord

class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.client.user} is online')
        await self.client.change_presence(status=discord.Status.online, activity=discord.Game("Thinking about meaning of my life."))

    @commands.command(name="ping")
    async def ping(self, ctx):
        await ctx.send('pong!')

    @commands.command(name="help")
    async def help(self, ctx):
        embed = discord.Embed(title='Help:', color=discord.colour.Color.green(), description=f"Hello **{ctx.message.author.name}**! Use `px [command]` to use command.")
        embed.add_field(name=":smiley: Fun", value="`meme [programming meme? yes/no]`\n"
                                                   "`cute (send cute gif ovo)`\n"
                                                   "`howgay [who?]`\n"
                                                   "`8ball [question]`")
        embed.add_field(name=":tools: Moderation", value="`giverole [member, role]`\n"
                                                   "`removerole [member, role]]`\n"
                                                   "`kick [member, reason]`\n"
                                                   "`ban [member, reason]`\n"
                                                         "`unban [nickname#tag]`\n"
                                                         "`clear [amount of messages to delete]]`\n"
                                                         "`newchannel [text channel? - yes or voice channel? - no, channel's name]`\n"
                                                         "`newcategory [category's name]\n`")
        embed.add_field(name=":pencil: Text", value="`reverse [text]`\n"
                                                    "`crazy [text]`\n"
                                                    "`stammer [text]`\n"
                                                    "`scream [text]`\n")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Commands(client))
