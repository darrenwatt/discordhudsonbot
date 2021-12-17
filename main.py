import discord
import os
from dotenv import load_dotenv
import random

load_dotenv()

client = discord.Client()

quotes = [
    "Is this going to be a stand-up fight, Sir, or another bug-hunt?",
    "Somebody said alien... she thought they said illegal alien and signed up.",
    "Anytime.  Anywhere.",
    "How do I get out of this chicken-shit outfit?",
    "I am ready, man. Ready to get it on.  Check-it-out.  I am the ultimate badass... state of the badass art.  You do not want to fuck with me.",
    "Independently targetting particle-beam phalanx.  VWAP! Fry half a city with this puppy.",
    "Don't  worry. Me and my squad of ultimate badasses will protect you. Check-it-out...",
    "Hey, if you like that, you're gonna love this...",
    "Hah! Stop your grinnin' and drop your linen! Found 'em.",
    "You tell me. I only work here."
]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

#    if message.content.lower().contains('alien'):
    if "alien" in message.content.lower():
        await message.channel.send(random.choice(quotes))


client.run(os.getenv('TOKEN'))