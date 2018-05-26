
#! python3
# coding: utf-8

import json
import logging
import random
import sys
import datetime

import discord
from discord.ext import commands

from ext.utils import checks

# logging
logging.basicConfig(level=logging.WARNING)


# JSON load
def load_db():
    with open('db.json') as f:
        return json.load(f)