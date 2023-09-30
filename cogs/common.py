from discord.ext import commands

class common(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send("pong")

async def setup(bot: commands.Bot):
    await bot.add_cog(common(bot))
