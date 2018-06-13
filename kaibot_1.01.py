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
    one_emote = ":onea:456319761312120877"
    two_emote = ":twoa:456319761601527808"
    three_emote = ":threea:456319761551196160"
    four_emote = ":foura:456319761375035393"
    five_emote = ":fivea:456319761601658890"
    six_emote = ":sixa:456319761492738058"
    seven_emote = ":sevena:456319761555521548"

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

        if message.content.upper().startswith(".SETLOCATION"):
            embed = discord.Embed(title="\u200b")
            embed.set_author(name="Location Options")
            embed.add_field(name="U.S.A", value="React with '1'", inline=True)
            embed.add_field(name="Canada", value="React with '2'", inline=True)
            embed.add_field(name="South America", value="React with '3'", inline = True)
            embed.add_field(name="Africa", value="React with '4'", inline=True)
            embed.add_field(name="Europe", value="React with '5'", inline=True)
            embed.add_field(name="Asia", value="React with '6'", inline=True)
            embed.add_field(name="AU & Oceania", value="React with '7'", inline=True)
            embed_message = await client.send_message(message.channel, embed=embed)
            await client.add_reaction(embed_message, emoji=one_emote)
            await asyncio.sleep(.1)
            await client.add_reaction(embed_message, emoji=two_emote)
            await asyncio.sleep(.1)
            await client.add_reaction(embed_message, emoji=three_emote)
            await asyncio.sleep(.1)
            await client.add_reaction(embed_message, emoji=four_emote)
            await asyncio.sleep(.1)
            await client.add_reaction(embed_message, emoji=five_emote)
            await asyncio.sleep(.1)
            await client.add_reaction(embed_message, emoji=six_emote)
            await asyncio.sleep(.1)
            await client.add_reaction(embed_message, emoji=seven_emote)
            global responseactive
            responseactive = 1

        await asyncio.sleep(120)
        await client.delete_message(message)
        try:
            await asyncio.sleep(.2)
            await client.delete_message(bot_message)
        except AttributeError:
            pass  # Bot didn't send a message
        except UnboundLocalError:
            pass  # Bot didn't send a message
        except:
            pass  # Bot didn't send a message



client.run(token)
