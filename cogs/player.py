import typing
import discord
import utils.globals as GG
from discord.ext import commands
from utils import logger
from OSRS_Hiscores import Hiscores

log = logger.logger

SKILLTOEMO = {"attack": "ATT",
              "defense": "DEF",
              "strength": "STR",
              "hitpoints": "HIT",
              "ranged": "RAN",
              "prayer": "PRA",
              "magic": "MAG",
              "cooking": "COO",
              "woodcutting": "WOO",
              "fletching": "FLE",
              "fishing": "FIS",
              "firemaking": "FIR",
              "crafting": "CRA",
              "smithing": "SMI",
              "mining": "MIN",
              "herblore": "HER",
              "agility": "AGI",
              "thieving": "THI",
              "slayer": "SLA",
              "farming": "FAR",
              "runecrafting": "RUN",
              "hunter": "HUN",
              "construction": "CON",
              "total": "STA"}

EMOTOSKILL = {"ATT": "attack",
              "DEF": "defense",
              "STR": "strength",
              "HIT": "hitpoints",
              "RAN": "ranged",
              "PRA": "prayer",
              "MAG": "magic",
              "COO": "cooking",
              "WOO": "woodcutting",
              "FLE": "fletching",
              "FIS": "fishing",
              "FIR": "firemaking",
              "CRA": "crafting",
              "SMI": "smithing",
              "MIN": "mining",
              "HER": "herblore",
              "AGI": "agility",
              "THI": "thieving",
              "SLA": "slayer",
              "FAR": "farming",
              "RUN": "runecrafting",
              "HUN": "hunter",
              "CON": "construction",
              "STA": "total"}


class Player(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def lookup(self, ctx, username):
        guild = await self.bot.fetch_guild(584842413135101990)
        user = Hiscores(username, 'N')

        embed = GG.EmbedWithAuthor(ctx)

        embed.title = username
        for x in SKILLTOEMO:
            emoji = discord.utils.get(guild.emojis, name=SKILLTOEMO.get(x))
            embed.add_field(name=f"{emoji} {x.capitalize()}",value=f"{user.skill(x)}")
        await ctx.send(embed=embed)


def setup(bot):
    log.info("Loading Player Cog...")
    bot.add_cog(Player(bot))
