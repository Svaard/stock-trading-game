from re import search, IGNORECASE
from commands.stocks import Stocks

class MessageHandler:

    def __init__(self, client):
        self.client = client
        self.commands = {}
        self.add_command(Stocks(client))
        print(f'Loaded {len(self.commands)} built-in commands.')

    async def handler(self, message):
        if message.author.bot:
            return

        for name, com in self.commands.items():
            match = search(com.pattern, message.content, IGNORECASE)
            if match:
                args = '' if not match.groups() else match.group(1)
                if com.wait:
                    return await com.command(message, args)
                return com.command(message, args)
                