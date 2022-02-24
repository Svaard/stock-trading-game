import discord
import config

token: str = config.TOKEN

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        author: str = message.author
        server: str = message.guild
        content: str = message.content
        print(f'{author} {server} {content}')

        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

client = MyClient()
client.run(token)