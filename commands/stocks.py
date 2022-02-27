import http.client
from commands.command import Command

class Stocks(Command):

    def __init__(self, client):
        super().__init__(self, client)
        self.name = 'Stocks'
        self.pattern = None
        self.usage = None