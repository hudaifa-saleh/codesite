import os

from django.core.management.base import BaseCommand, CommandError
import discord

from os.path import dirname, basename, isfile, join
from importlib import import_module
import glob

from django.conf import settings
from .bot.mods.commands import print_command, register_command, find_commands

client = discord.Client(intents=discord.Intents.all())


class Command(BaseCommand):
    help = 'Runs the discord bot'

    def handle(self, *args, **options):
        print('Running discord bot')

        client.run(settings.DISCORD_TOKEN)
