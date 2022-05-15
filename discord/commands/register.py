from multiprocessing.connection import Client
import requests
from json import loads
from commands.command import Command
from re import search
import config as config
from datetime import datetime, timedelta
from database import Database
from pymongo import errors

class Register(Command):

    def __init__(self, client):
        super().__init__(client)
        self.name: str = 'Register'
        self.pattern: str = r'\$register'
        self.usage: str = '`usage: $register'

    def is_valid(self, string):
        return all(ord(char) < 128 and char not in ('\\', '/') for char in string)

    def command(self, message, args):
        print(f'Register command used by { message.author }')
        if not self.is_valid(args):
            return
        try:
            Database.initialize()
            user = message.author.name + '#' + message.author.discriminator
            if(Database.find_one('stonks', {'author': user})):
                print(f'{ message.author } tried to register again.')
                Database.close()
                return '```User already registered```'
            else:
                data = {'author': user}
                Database.insert('stonks', data)
                Database.close()
                return '```You are now registered, Welcome to the stonk market```'
        except errors.ConnectionFailure:
            print(f'[ERROR] Connection to the database cannot be made or was lost')
            return '```Connection to the database could not be made.```'
        except errors.ExecutionTimeout:
            print(f'[ERROR] Database operation timed out')
            return '```Database operation timed out.```'