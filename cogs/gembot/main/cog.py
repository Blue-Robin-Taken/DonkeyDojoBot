import discord
from discord.ext.commands import Cog
import json


class GemBot(Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot
        self.jsonLoad = json.load(open('./config.json', 'r', encoding='utf-8'))[
            'GemBot']  # https://stackoverflow.com/questions/65063828/emoji-problem-reading-json-file-in-python

    @Cog.listener()
    async def on_raw_reaction_add(self, payload):
        emoji = payload.data['emoji']['name']
        if emoji == self.jsonLoad['GemEmoji']:
            gemChannel = await self.bot.fetch_channel(self.jsonLoad['channelID'])
            m = await (await self.bot.fetch_channel(payload.channel_id)).fetch_message(payload.message_id)  # message
            gemScore = discord.utils.get(m.reactions, emoji=self.jsonLoad['GemEmoji']).count

            if gemScore == int(self.jsonLoad['minCount']):
                embed = discord.Embed(
                    title=f"Message by: {m.author.name}",
                    description=m.content,
                    color=discord.Color.teal()
                )
                embed.add_field(name=f'Message Link', value=f'https://discord.com/channels/{m.guild.id}/{m.channel.id}/{m.id}', inline=False)
                embed.add_field(name=f'Gem Score', value=f"{gemScore}")
                await gemChannel.send(embed=embed)
            elif gemScore >= int(
                    self.jsonLoad['minCount']):
                pass


def setup(bot: discord.Bot):
    bot.add_cog(GemBot(bot))
