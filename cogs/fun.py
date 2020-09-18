import discord
import giphy_client
from discord.ext import commands
from discord.ext.commands import clean_content
import praw
import random

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.reddit = praw.Reddit(client_id='DdknSuiLYTCk6w',
                             client_secret='_4UTRndvUA0N5nhPWlrPTdnpoms',
                             user_agent='dziobax1')
        self.giphy_token = "mdyWTPNKCtpdVZ75Q0C8Wnjpi0SX28LZ"
        self.api_instance = giphy_client.DefaultApi()

    @commands.command(name="meme")
    async def meme(self, ctx):
        memes = self.reddit.subreddit('ProgrammerHumor').top()
        post_to_picks = random.randint(0, 20)
        for i in range(0, post_to_picks):
            submission = next(x for x in memes if not x.stickied)
        embed = discord.Embed(title=submission.title, url=submission.url, color= discord.colour.Color.dark_grey())
        embed.set_image(url=submission.url)
        await ctx.send(embed=embed)

    @commands.command(name="howgay", aliases=["gay", "hgay"])
    async def howgay(self, ctx):
        num = random.randint(0, 100)
        state = emoji = ""
        if (num <= 33):
            state = f'{random.choice(["You are not gay", "No-homo", "**May** a little bit gay : )"])}'
            emoji = f'{random.choice([":no_mouth:", ":black-heart:", ":smirk:"])}'
        elif (num > 33 and num <= 66):
            state = f'{random.choice(["Wait. Are you gay?", "Half-homo", "Ho-ho, perhabs i smell gay ( ͡° ͜ʖ ͡°)", "My computer says you could be gay. Is he right, isn t he?"])}'
            emoji = f'{random.choice([":wink:", ":yellow-heart:", ":smirk:"])}'
        else:
            state = f'{random.choice(["~100% gay!", "HoMo", "U r gay BRO", "GAY"])}'
            emoji = f'{random.choice([":people_holding_hands:", ":heart:", ":rainbow_flag:", ":smirk:"])}'
        embed = discord.Embed(title=f'Gay-Machine', color=0xFFC0CB)
        embed.add_field(name=f'{num}% gay {emoji}', value=state)
        await ctx.send(embed=embed)

    @commands.command(name='8ball', aliases=["ball", "8b"])
    async def ball8(self, ctx, *, question: clean_content):
        num = random.randint(0, 10)
        option = ""
        if (num < 3):
            option = random.choice(['Yes', 'My answer: yes', 'Somebody told me the best answer is "yes"', 'In brief: yes',
                                    'My computer said: "Yes, it is obvious"'])
        elif (num >= 3 and num < 6):
            option = random.choice(
                ['Ask again later', 'I have not enough energy to answer. Give me the cookie, please', 'I cannot answer', 'My computer needs a break',
                 'I do not understand'])
        else:
            option = random.choice(
                ['No', 'In brief: no', 'No, obv',
                 'Definitely no',
                 'Do not count on it'])
        embed = discord.Embed(title=f'8bal [{ctx.author.name}] ', color=discord.colour.Color.green())
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name=f"Question:", value=f"{question}", inline=False)
        embed.add_field(name='Answer:', value=f'{option} :8ball:')
        await ctx.send(embed=embed)


    @commands.command(name='cute')
    async def cute(self, ctx):
        word = random.choice(['cute', 'uwu', 'cat', 'dog'])
        response = self.api_instance.gifs_search_get(self.giphy_token, 'cute', limit=99, rating='a')
        lst = list(response.data)
        gif = random.choices(lst)

        await ctx.send(gif[0].url)


def setup(client):
    client.add_cog(Fun(client))