import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="giverole", aliases=["grole"])
    @commands.has_permissions(administrator=True)
    async def giverole(self, ctx, member: discord.Member, role: discord.Role = None):
        if (role == None):
            return
        else:
            await member.add_roles(role)
            await ctx.message.add_reaction("👍")

    @commands.command(name="removerole", aliases=["rrole"])
    @commands.has_permissions(manage_roles=True)
    async def removerole(self, ctx, member: discord.Member, role: discord.Role = None):
        if (role == None):
            return
        else:
            if (role in member.roles):
                await member.remove_roles(role)
                await ctx.message.add_reaction("👍")
            else:
                await ctx.send(f"Wait. That's illegal. {member.mention} hasn't got this role.")

    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.message.add_reaction("👍")

    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} was banned.")

    @commands.command(name="unban")
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_nick, member_disc = member.split("#")
        for user in banned_users:
            if (user.user.name, user.user.discriminator) == (member_nick, member_disc):
                await ctx.guild.unban(user.user)
                await ctx.send(f"{member_nick}#{member_disc} was unbanned.")
                return
        await ctx.send(f"{member_nick}#{member_disc} not found.")

    @commands.command(name="clear")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=10):
        await ctx.channel.purge(limit=amount)

    @commands.command(name="newchannel", aliases=["nchan"])
    @commands.has_permissions(manage_messages=True)
    async def newChannel(self, ctx, text: bool, *, name):
        if (text):
            await ctx.message.guild.create_text_channel(f"{name}")
        else:
            await ctx.message.guild.create_voice_channel(f"{name}")

    @commands.command(name="newcategory", aliases=["ncat"])
    @commands.has_permissions(manage_messages=True)
    async def newCategory(self, ctx, *, name):
        await ctx.message.guild.create_category(f"{name}")

def setup(client):
    client.add_cog(Moderation(client))