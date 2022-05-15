from re import search, IGNORECASE
from commands.stocks import Stocks
from commands.register import Register

class MessageHandler:

    def __init__(self, client):
        self.client = client
        self.commands = {}
        self.add_command(Stocks(client))
        self.add_command(Register(client))
        print(f'Loaded {len(self.commands)} built-in commands.')

    def add_command(self, command):
        if command.name not in self.commands:
            self.commands[command.name] = command

    async def handler(self, message):
        if message.author.bot:
            return
        for name, com in self.commands.items():
            match = search(com.pattern, message.content, IGNORECASE)
            if match:
                args = '' if not match.groups() else match.group(1)
                return com.command(message, args)
                