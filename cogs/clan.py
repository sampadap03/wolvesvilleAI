import discord
from discord.ext import commands
from datetime import datetime

from wovapi.clan import ClanApi
# import cogs.support as s

class Clan(commands.Cog, ClanApi):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        ClanApi.__init__(self)


    @commands.command()
    async def clan(self, ctx: commands.Context):
        response = self.get_clan_info()

        embed = discord.Embed(title= response["name"], 
                            description = response["description"], 
                            color= int(response["iconColor"].lstrip('#'), 16),
                            timestamp= datetime.strptime(response["creationTime"], "%Y-%m-%dT%H:%M:%S.%fZ"))

        # embed.set_thumbnail(url= s.Support().get_fontawesome_url(response["icon"])) -- taking too much time
        embed.add_field(name="XP", value=response["xp"], inline=True)
        embed.add_field(name="Members", value=response["memberCount"], inline=True)
        embed.add_field(name="Tag", value=response["tag"], inline=True)
        embed.add_field(name="Type", value=response["joinType"], inline=True)
        embed.add_field(name="Joining Level", value=response["minLevel"], inline=True)
        embed.add_field(name="Language", value=response["language"], inline=True)
        embed.add_field(name="Quests", value=response["questHistoryCount"], inline=True)
        embed.add_field(name="Gold", value=response["gold"], inline=True)
        embed.add_field(name="Gems", value=response["gems"], inline=True)
        
        await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Clan(bot))
