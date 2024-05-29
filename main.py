from highrise import BaseBot
from highrise import __main__
from collections import UserDict
from asyncio import run as arun
from highrise.models import SessionMetadata, User
from highrise.models import Position
from highrise.models import SessionMetadata, User, CurrencyItem, Item, AnchorPosition, Reaction, ModerateRoomRequest, Position
from highrise import BaseBot, User, Position, SessionMetadata
import asyncio
import requests
from highrise import BaseBot, __main__
from highrise.models import (AnchorPosition, Item, Position, User,)
from highrise import *
from highrise.models import *
from asyncio import Task
from highrise.__main__ import *
from highrise.models import (AnchorPosition, CurrencyItem,Item,Position,SessionMetadata,User,)

class BotDefinition:
    def __init__(self, bot, room_id, api_token):
        self.bot = bot
        self.room_id = room_id
        self.api_token = api_token

class MyBot(BaseBot):

      def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.following_user = None 
          self.banned_users = {} 
          self.following_username = None
          super().__init__()
          self.user_positions = {}

      async def run(self, room_id, token):
           definitions = [BotDefinition(self, room_id, token)]
           await __main__.main(definitions)


if __name__== "__main__":
    room_id = "664fc6133846c1529586b370"
    token = "9c8a749e744e8505e0141bd982430210a8973e126def8610d5b3e8964f7c407b"
    arun(MyBot().run(room_id, token))