import json
import discord
from discord import app_commands
from discord.ext import commands



class Buttons(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=30)


    @discord.ui.button(label="Reset Infractions",style=discord.ButtonStyle.red)
    async def reset_infractions(self, interaction: discord.Interaction, button: discord.ui.Button):

        guild = interaction.guild
        infraction_counts = {}
        for member in guild.members:
            infraction_counts[member.id] = 0
        with open(r'C:\Users\Mati\OneDrive\Desktop\Discord Slash Commands\moderation\moderation.json', 'w') as f:
            json.dump(infraction_counts, f)
            
        await interaction.response.edit_message(content='`resources\infractions.json reset`')


    @discord.ui.button(label="Reset Economy", style=discord.ButtonStyle.red)
    async def reset_economy(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild

        default_total_balance = 1000
        default_bank_balance = 1000
        default_wallet_balance = 0
        default_job = None



        for member in guild.members:

            user_data = {}
            user_data['total_balance'] = default_total_balance
            user_data['bank_balance'] = default_bank_balance
            user_data['wallet_balance'] = default_wallet_balance
            user_data['job'] = default_job



            with open(r'C:\Users\Mati\OneDrive\Desktop\Discord Slash Commands\economy\economy.json', 'r') as f:
                data = json.load(f)

            users = data['users']
            users[str(member.id)] = user_data

            with open(r'C:\Users\Mati\OneDrive\Desktop\Discord Slash Commands\economy\economy.json', 'w') as f:
                json.dump({'users': users}, f)

        await interaction.response.edit_message(content='`economy\economy.json reset`')



class Config(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @app_commands.checks.has_permissions(ban_members=True)
    @app_commands.command(name="config", description="administator permissions required")
    async def config(self, interaction: discord.Interaction):
        await interaction.response.send_message('`press buttons below to edit config files`', view=Buttons(), ephemeral=True)


    

    