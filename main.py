import discord
from discord.ext import commands

import os
TOKEN = os.getenv("")


WATCH_USER_ID = 1447561484040146985
SOURCE_CHANNEL_ID = 1403284630039433238
LOG_CHANNEL_ID = 1447864922053804042

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):

    if message.author.bot:
        return

    if message.author.id == WATCH_USER_ID and message.channel.id == SOURCE_CHANNEL_ID:

        log_channel = bot.get_channel(LOG_CHANNEL_ID)

        if log_channel:

            embed = discord.Embed(
                title="Message Logged",
                description=message.content,
                color=0x2f3136
            )

            embed.set_author(
                name=f"{message.author} ({message.author.id})",
                icon_url=message.author.display_avatar.url
            )

            embed.add_field(
                name="Channel",
                value=message.channel.mention,
                inline=True
            )

            embed.add_field(
                name="Message ID",
                value=message.id,
                inline=True
            )

            embed.set_footer(text="Message Logger")
            embed.timestamp = message.created_at

            await log_channel.send(embed=embed)

    await bot.process_commands(message)

bot.run(TOKEN)
