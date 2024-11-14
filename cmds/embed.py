import discord
from discord.ext import commands

@commands.hybrid_command()
@commands.has_role(1295718123923832862)
async def rules(ctx):
        embed = discord.Embed(
            colour=discord.Color.brand_green(),
            description="🙈 NSFW content has no place here. \n🙊 Don't go out of your way to offend others using slurs or derogatory terms. \n🙉 Keep spam at a minimum.\n\nWe are a laid back community, please practice common sense when it comes to your interactions with the server, staff members have full discretion over handling unforeseen actions from users\n\n**Wish to invite friends over?**\nhttps://discord.gg/warpups",
            title="Rules & Philosophy"
        )
        
        embed.set_footer(text="rules can be subject to changes and modifcations")
        embed.set_author(name="Welcome to WARPUPS", url="https://discord.gg/warpups")

        await ctx.send(embed=embed)

@commands.hybrid_command()
@commands.has_role(1295718123923832862)
async def roles(ctx):
        embed = discord.Embed(
            colour=discord.Color.blue(),
            description="<@&1295693696922292226>\nautomatically granted to server nitro boosters (comes with perks)\n\n<@&1296739223340060673>\ngranted weekly to the best works posted in <#1295651400977612831> that also get featured in our servers banner art\n\n<@&1295654074112413716> pingable staff member role\n\n<@&1295672627008114708> granted to members of the old discord\n\n<@&1300860664264396840> for special people\n\n<@&1295681393585684552> mute role for naughty people\n\n **We offer custom named roles for studios and their employees, please DM any of the staff members if you or your studio wishes to claim this.**",
            title="Roles"
        )

        await ctx.send(embed=embed)

@commands.hybrid_command()
@commands.has_role(1295718123923832862)
async def channels(ctx):
        embed = discord.Embed(
            colour=discord.Color.brand_red(),
            description="this is the description",
            title="this is the tittle"
        )

        embed.set_footer(text="this is the footer")
        embed.set_author(name="Richard", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")

        await ctx.send(embed=embed)

async def setup(bot):
        bot.add_command(rules)
        bot.add_command(roles)
        bot.add_command(channels)