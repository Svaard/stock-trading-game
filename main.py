import discord
import config
import re

class MyClient(discord.Client):

    def __init__(self):
        super().__init__()
        self.token = self.get_token()
        self.run(self.token)

    def get_token(self):
        return config.TOKEN

    async def on_ready(self):
        print(f'Logged on as {self.user} with  id {self.user.id}')

    async def on_message(self, message):
        content = message.clean_content
        content = re.sub(r'<(:[\w\d]+:)\d{18}>', r'\1', content)
        if type(message.channel) == discord.DMChannel:
            print(f'DM [{message.author}]: {message.content}')
        else:
            print(f'{message.channel.guild}#{message.channel} [{message.author}]: {content}')

        # don't respond to ourselves
        if message.author.bot:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

MyClient()
