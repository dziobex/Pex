from discord.ext import commands

class Text(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="reverse")
    async def reverse(self, ctx, *, text):
        await ctx.send(f"{ctx.message.author.name} said: {text[::-1]}")

    @commands.command(name="crazy")
    async def crazy(self, ctx, *, text):
        await ctx.send(f"{ctx.message.author.name} said: {self.crazySpeech(text)}")

    def crazySpeech(self, text):
        result = ''
        j = 0
        for i in range(0, len(text)):
            if j%2 == 0:
                result += text[i].lower()
            else:
                result += text[i].upper()
            if text[i].isspace():
                continue
            else:
                j = j + 1
        return result

    @commands.command(name="stammer")
    async def stammer(self, ctx, *, text):
        await ctx.send(f'{ctx.message.author.name} said: {"-".join(text)}')

    @commands.command(name="scream")
    async def scream(self, ctx, *, text):
        await ctx.send(f"{ctx.message.author.name} said: {text.upper()}")

def setup(client):
    client.add_cog(Text(client))