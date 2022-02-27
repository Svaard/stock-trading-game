class Command:
    def __init__(self, client):
        self.client = client
        self.name = None
        self.pattern = None
        self.usage = None

    def command(self, message, args):
        pass