import requests
from json import loads
from commands.command import Command
from re import search
import config as config
from datetime import datetime, timedelta

HOST = 'https://api.polygon.io'
URL = '/v2/aggs/ticker/'
KEY = config.API_KEY

class Stocks(Command):

    def __init__(self, client):
        super().__init__(client)
        self.name: str = 'Stocks'
        self.pattern: str = r'^\$stock(.+)'
        #self.pattern: str = r'^(\$stock)\s(buy|sell|price)\s(\w{1,5})$'
        self.usage: str = '`usage: $stock {buy|sell|price} ticker'

    def get_latest_day(self):
        current: datetime = datetime.now()
        if current.isoweekday() >= 6:
            remove: int = current.isoweekday() - 5
            current = current - timedelta(days=remove)
        date_tuple: tuple = current.timetuple()
        year: int = date_tuple[0]
        month: int = date_tuple[1]
        day: int = date_tuple[2]
        return f'{year}-{month:02}-{day:02}'

    def is_valid(self, string):
        return all(ord(char) < 128 and char not in ('\\', '/') for char in string)

    def command(self, message, args):
        if not self.is_valid(args):
            return
        match = search(r'(\S+) (\S+)', args)
        arg1 = match.group(1)
        arg2 = match.group(2)
        if arg1 in ('buy','sell') and datetime.now().isoweekday() >= 6:
            return "```Chillax, it's the weekend!```"
        print(arg1)
        print(arg2)
        query: str = f'{HOST}{URL}{arg2}/range/1/day/{self.get_latest_day()}/{self.get_latest_day()}?adjusted=true&sort=asc&limit=120&apiKey={KEY}'
        response = requests.get(query)
        if response.status_code != 200:
            print(f'[ERROR] Bad response from {HOST}!')
            print(f'Status: {response.status_code}\n{response.raise_for_status}')
            print(query)
            return

        json: str = response.json()
        if arg1 == 'price':
            return f'```Open: {json["results"][0]["o"]}\nClose: {json["results"][0]["c"]}\n```'
