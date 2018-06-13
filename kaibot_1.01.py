#!/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio
import datetime
import json
import os
import random
import string
import sys
import math
import discord
from discord.ext import commands


def get_json(file_path):
    with open(file_path, 'r') as fp:
        return json.load(fp)


def get_time():
    # Decides if startup is during AM or PM ours (yea damn 'murica time)
    if datetime.datetime.now().hour > 13:
        cur_hour = datetime.datetime.now().hour - 12
        am_or_pm = "PM"
    else:
        cur_hour = datetime.datetime.now().hour
        am_or_pm = "AM"


acc_name = "main"
jsontoken = 0

if acc_name == "main":
    print("Using MAIN account")
    jsontoken = get_json('C:/Users/maxla/PycharmProjects/kaibot/main_token.json')
    token = jsontoken.get("token")
    infochannel = "456293805453475872"

print("Token being used: {}".format(jsontoken.get("token")))
print("Connecting...")

client = discord.Client()
client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    users = len(set(client.get_all_members()))
    channels = len([c for c in client.get_all_channels()])
    file_name = os.path.basename(sys.argv[0])  # Gets file name

    r = random.randint(3, 3)
    if r == 1:
        await client.change_presence(game=discord.Game(name="Live for {0}:{1}:00".format(hours, minutes),
                                                       url="https://twitch.tv/mehvix", type=1))
    if r == 2:
        await client.change_presence(game=discord.Game(name="Version {}".format(file_name[7:-3]),
                                                       url="https://twitch.tv/mehvix", type=1))
    if r == 3:
        await client.change_presence(game=discord.Game(name="Created by Mehvix#7172", url="https://twitch.tv/mehvix",
                                                       type=1))
    server_list = list(client.servers)

    print("============================================================")
    print("• Version:                   {}".format(discord.__version__))
    print("• Start Time:                {}".format(get_time()))
    print("• Client Name:               {}".format(client.user))
    print("• Client ID:                 {}".format(client.user.id))
    print("• Channels:                  {}".format(channels))
    print("• Users:                     {}\n".format(users))
    print("• Connected to " + str(len(client.servers)) + " server(s):")
    for x in range(len(server_list)):
        print("     > " + server_list[x - 1].name)
    print("============================================================")


# Tbh I have no idea what resumed is. If you know hmu on discord @ Mehvix#7172
@client.event
async def on_resumed():
    print("{}: Resumed ".format(get_time()))


@client.event
async def on_message(message):
    #if message.author == client.user:
     #   print("{}: The bot tried to reply to itself, but it was stopped".format(get_time()))
      #  return

    server = message.server

    # Message author variables
    user_id = message.author.id
    user_name = message.author

    print("{0}: {1} sent message '{2}' in {3}".format(get_time(), user_name, message.content, message.channel.id))

    if message.channel.id == infochannel:
        print("{0}: {1} sent message in the info channel".format(get_time(), user_name))
        if message.content.upper().startswith(".PING"):
            print("{0}: {1} requested 'PING'".format(get_time(), user_name))
            bot_message = await client.send_message(message.channel, "Pong! :ping_pong:")

        if message.content.upper().startswith(".SETNICK"):
            name = str(message.content[8:])
            print("{0}: {1} set there nick to {2}".format(get_time(), user_name, name))
            await client.change_nickname(user_name, name)
            bot_message = await client.send_message(message.channel, "Success :tada:! Set nick to `{}`".format(name))

        if message.content.upper().startswith(".SETREALNAME"):
            realname = str(message.content[12:])
            print("{0}: {1} set there real name to {2}".format(get_time(), user_name, realname))
            realname_role = await client.create_role(server)
            await client.edit_role(server, realname_role, name=realname)
            await client.add_roles(user_name, realname_role)
            bot_message = await client.send_message(message.channel, "Success :tada:! Set name to `{}`".format(realname))



        await asyncio.sleep(10)
        await client.delete_message(message)
        await asyncio.sleep(.2)
        try:
            await client.delete_message(bot_message)
        except AttributeError:
            pass  # Bot didn't send a message
        except UnboundLocalError:
            pass  # Bot didn't send a message


client.run(token)
