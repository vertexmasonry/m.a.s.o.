import discord
from discord import app_commands

class MyGroup(app_commands.Group):
    @app_commands.command()
    async def pong(self,interaction: discord.Interaction):
        await interaction.response.send_message(f"pong")

async def setup(bot):
    bot.tree.add_command(MyGroup(name="greetings2",description="Say Hello"))