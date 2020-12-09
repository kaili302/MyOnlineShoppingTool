import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
TEXT_CHANNEL= os.getenv('TEXT_CHANNEL')
WEBHOOK = os.getenv('WEBHOOK')

class DiscordBot(discord.Client):
    """
    A webhook is enough for message sending actually. The rest is for fun
    """

    webhook = discord.Webhook.from_url(WEBHOOK,
                                       adapter=discord.RequestsWebhookAdapter())

    @staticmethod
    def send(msg):
        DiscordBot.webhook.send(str(msg))

    def run(self):
        super().run(TOKEN)

    async def on_ready(self):
        self.guild = discord.utils.find(lambda g: g.name == GUILD, self.guilds)
        print(
            f'{self.user} is connected to guild: '
            f'{self.guild.name}(id: {self.guild.id})'
        )
        self.text_channel = discord.utils.get(self.guild.text_channels,
                                              name=TEXT_CHANNEL)
        await self.text_channel.send('Bot is connected!')


if __name__ == "__main__":
    # client = DiscordClient()
    # client.run()
    DiscordBot.send("hello")
