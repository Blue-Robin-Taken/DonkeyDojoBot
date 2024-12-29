import discord
from discord.ext.commands import Cog
import json


class GemBot(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.jsonLoad = json.load(open('./config.json', 'r', encoding='utf-8'))['GemBot']  # https://stackoverflow.com/questions/65063828/emoji-problem-reading-json-file-in-python

    @Cog.listener()
    async def on_raw_reaction_add(self, payload):
        emoji = payload.data['emoji']['name']
        print('why', emoji, self.jsonLoad['GemEmoji'])
        if emoji == self.jsonLoad['GemEmoji']:
            print(payload)


def setup(bot: discord.Bot):
    bot.add_cog(GemBot(bot))
