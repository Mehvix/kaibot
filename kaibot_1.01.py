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

    # Puts "0" in front of number time
    if datetime.datetime.now().minute < 10:
        cur_min = "0{}".format(datetime.datetime.now().minute)
    else:
        cur_min = datetime.datetime.now().minute

    if datetime.datetime.now().second < 10:
        cur_sec = "0{}".format(datetime.datetime.now().second)
    else:
        cur_sec = datetime.datetime.now().second

    return "{0}:{1}:{2} {3}".format(cur_hour, cur_min, cur_sec, am_or_pm)


response_active = 0
region_message = 0

acc_name = "main"
jsontoken = 0

embed_color = 0x1abc9c
invis_color = 0x2f3136

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

    one_reformatted = ":onea:456319761312120877"
    two_reformatted = ":twoa:456319761601527808"
    three_reformatted = ":threea:456319761551196160"
    four_reformatted = ":foura:456319761375035393"
    five_reformatted = ":fivea:456319761601658890"
    six_reformatted = ":sixa:456319761492738058"
    seven_reformatted = ":sevena:456319761555521548"

    usa_role = "456649267948290049"
    canada_role = "454286208051314698"
    south_america_role = "456649264613949461"
    eu_role = "456649269303181314"
    asia_role = "456649266681610243"
    africa_role = "454426499273981952"
    middle_east_role = "454426500708564992"
    au_role = "456649263301263381"

    usa_role_name = "USA"
    canada_role_name = "Canada"
    sa_role_name = "South America"
    eu_role_name = "EU"
    asia_role_name = "Asia"
    Africa_role_name = "Africa"
    me_role_name = "Middle East"
    au_role_name = "AU & Oceania"

    northeast_role = "456653939148980235"
    great_lakes_role = "456653622785081354"
    northwest_role = "456653628011184138"
    southeast_role = "456653628745449494"
    west_role = "456653623242391557"
    south_role = "456653624731238403"
    heartland_role = "456653626308427797"

    nw_role_name = "Northwest"
    west_role_name = "West"
    hl_role_name = "Heartland"
    south_role_name = "South"
    gl_role_name = "Great Lakes"
    se_role_name = "Southeast"
    ne_role_name = "Northeast"

    admin_role_id = "454125039051210753"


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

    if message.content.startswith('$react'):
        msg = await client.send_message(message.channel, 'React with thumbs up or thumbs down.')
        res = await client.wait_for_reaction([one_reformatted, one_emote], message=msg)
        await client.send_message(message.channel, '{0.user} reacted with {0.reaction.emoji}!'.format(res))

    print("{0}: {1} sent message '{2}' in {3}".format(get_time(), user_name, message.content, message.channel.id))

    if message.channel.id == infochannel:
        print("{0}: {1} sent message in the info channel".format(get_time(), user_name))

        if admin_role_id in [role.id for role in message.author.roles]:
            if message.content.upper().startswith(".SHOWINFO"):
                print("{0}: {1} requested '.SHOWINFO'".format(get_time(), user_name))
                await asyncio.sleep(.1)
                await client.delete_message(message)
                embed = discord.Embed(title="\u200b", color=embed_color)
                embed.set_author(name="🚨🚨🚨 Read This! 🚨🚨🚨")
                embed.add_field(name="Set your nickname", value="Type '.setnick' and your desired nick name",
                                inline=True)
                embed.add_field(name="Set your real name", value="Type '.setrealname' and your real name",
                                inline=True)
                embed.add_field(name="Set your real name", value="Type '.setrealname' and your real name",
                                inline=True)
                embed.add_field(name="Set your location", value="Type '.setlocation' and follow the instructions",
                                inline=True)
                await client.send_message(message.channel, embed=embed)

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
            await client.edit_role(server, realname_role, name=realname, color=invis_color)
            await client.add_roles(user_name, realname_role)
            bot_message = await client.send_message(message.channel, "Success :tada:! Set name to `{}`".format(realname))

        if message.content.upper().startswith(".SETLOCATION"):
            embed = discord.Embed(title="\u200b")
            embed.set_author(name="Location Options")
            embed.add_field(name="🇺🇸 U.S.A", value="React with '1'", inline=True)
            embed.add_field(name="🇨🇦 Canada", value="React with '2'", inline=True)
            embed.add_field(name="🌎 South America", value="React with '3'", inline = True)
            embed.add_field(name="🇿🇦 Africa", value="React with '4'", inline=True)
            embed.add_field(name="🇪🇺 Europe", value="React with '5'", inline=True)
            embed.add_field(name="🌏 Asia", value="React with '6'", inline=True)
            embed.add_field(name="🇦🇺 AU & Oceania", value="React with '7'", inline=True)
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
            global response_active
            response_active = 1
            global region_message
            region_message = embed_message
            print(region_message)


@client.event
async def on_reaction_add(reaction, user):
    emoji_used = str(reaction.emoji)[1:-1]
    print("{0}: {1} reacted with `{2}` to {3}'s message"
          .format(get_time(), user, emoji_used, reaction.message.author))
    global response_active
    global region_message
    if response_active == 1:
        if emoji_used == one_emote:
            role = discord.utils.get(reaction.message.server.roles, name=usa_role_name)
            await client.add_roles(user, role)
            await client.delete_message(region_message)
            fp = "./regions.jpg"
            bot_message = await client.send_file(reaction.message.channel, fp)

            embed = discord.Embed(title="\u200b", color=embed_color)
            embed.set_author(name="Location Options")
            embed.add_field(name="Northwest", value="React with '1'", inline=True)
            embed.add_field(name="West", value="React with '2'", inline=True)
            embed.add_field(name="Heartland", value="React with '3'", inline=True)
            embed.add_field(name="South", value="React with '4'", inline=True)
            embed.add_field(name="Southeast", value="React with '5'", inline=True)
            embed.add_field(name="Great Lakes", value="React with '6'", inline=True)
            embed.add_field(name="Northeast", value="React with '7'", inline=True)
            embed_message = await client.send_message(reaction.message.channel, embed=embed)
            response_active = 0
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
            response_active = 2

        if emoji_used == two_emote:
            role = discord.utils.get(reaction.message.server.roles, name=canada_role_name)
            await client.add_roles(user, role)

        if emoji_used == three_emote:
            role = discord.utils.get(reaction.message.server.roles, name=sa_role_name)
            await client.add_roles(user, role)

        if emoji_used == four_emote:
            role = discord.utils.get(reaction.message.server.roles, name=africa_role)
            await client.add_roles(user, role)

        if emoji_used == five_emote:
            role = discord.utils.get(reaction.message.server.roles, name=eu_role_name)
            await client.add_roles(user, role)

        if emoji_used == six_emote:
            role = discord.utils.get(reaction.message.server.roles, name=asia_role_name)
            await client.add_roles(user, role)

        if emoji_used == seven_emote:
            role = discord.utils.get(reaction.message.server.roles, name=au_role_name)
            await client.add_roles(user, role)

    if response_active == 2:
        if emoji_used == one_emote:
            role = discord.utils.get(reaction.message.server.roles, name=nw_role_name)
            await client.add_roles(user, role)

        if emoji_used == two_emote:
            role = discord.utils.get(reaction.message.server.roles, name=west_role_name)
            await client.add_roles(user, role)

        if emoji_used == three_emote:
            role = discord.utils.get(reaction.message.server.roles, name=hl_role_name)
            await client.add_roles(user, role)

        if emoji_used == four_emote:
            role = discord.utils.get(reaction.message.server.roles, name=south_role_name)
            await client.add_roles(user, role)

        if emoji_used == five_emote:
            role = discord.utils.get(reaction.message.server.roles, name=se_role_name)
            await client.add_roles(user, role)

        if emoji_used == six_emote:
            role = discord.utils.get(reaction.message.server.roles, name=gl_role_name)
            await client.add_roles(user, role)

        if emoji_used == seven_emote:
            role = discord.utils.get(reaction.message.server.roles, name=ne_role_name)
            await client.add_roles(user, role)


client.run(token)
