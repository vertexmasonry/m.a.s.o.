import discord
from discord.ext import commands

@commands.command()
async def ping(ctx):
        embed = discord.Embed(
            colour=discord.Color.dark_teal(),
            description="this is the description",
            title="this is the tittle"
        )

        embed.set_footer(text="this is the footer")
        embed.set_author(name="Richard", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")

        await ctx.send(embed=embed)

async def setup(bot):
        bot.add_command(ping)