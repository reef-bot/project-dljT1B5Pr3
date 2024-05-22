import discord
from discord.ext import commands
from commands import moderation, music, information, settings
from utils import error_handling, logging

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)
logger = logging.BotLogger()
error_handler = error_handling.ErrorHandling()

@bot.event
async def on_ready():
    logger.log_info('Bot is ready!')

# Add commands here
bot.add_cog(moderation.ModerationCommands(bot))
bot.add_cog(music.MusicCommands(bot))
bot.add_cog(information.InformationCommands(bot))
bot.add_cog(settings.SettingsCommands(bot))

# Handle errors
@bot.event
async def on_command_error(ctx, error):
    error_handler.handle_error(error)

# Run the bot
bot.run('YOUR_DISCORD_BOT_TOKEN')