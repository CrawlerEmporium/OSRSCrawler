import typing
import discord
import utils.globals as GG
from discord.ext import commands
from utils import logger
from OSRS_Hiscores import Hiscores

log = logger.logger


class Player(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def lookup(self, ctx):
        user = Hiscores('Lord_Duskk','N')

        print(user.stats)

        await ctx.send(user.skill('total'))


def setup(bot):
    log.info("Loading Player Cog...")
    bot.add_cog(Player(bot))
