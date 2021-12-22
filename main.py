from typing import ContextManager
import discord
import os
from dotenv import load_dotenv
import random
import logging

# logging to stdout
logging.basicConfig(level=logging.INFO)
load_dotenv()

# token stuff
token = os.getenv('TOKEN')
if token == None:
    logging.critical("No TOKEN found in env")
    exit()

client = discord.Client()

quotes = [
    "This floor's freezing.",
    "Whoooah! No shit? I'm impressed.",
    "Is this going to be a stand-up fight, Sir, or another bug-hunt?",
    "Somebody said alien... she thought they said illegal alien and signed up.",
    "Anytime. Anywhere.",
    "How do I get out of this chicken-shit outfit?",
    "I am ready, man. Ready to get it on. Check-it-out. I am the ultimate badass... state of the badass art. You do not want to fuck with me.",
    "Independently targetting particle-beam phalanx. VWAP! Fry half a city with this puppy.",
    "Don't  worry. Me and my squad of ultimate badasses will protect you. Check-it-out...",
    "Hey, if you like that, you're gonna love this...",
    "Hah! Stop your grinnin' and drop your linen! Found 'em.",
    "You tell me. I only work here.",
    "He's coming in. I feel safer already.",
    "If they're within twenty klicks we'll read it out here, but so far... zip.",
    "Yeah... but it's a dry heat.",
    "What're we supposed to use, man? Harsh language?",
    "Multiple signals. All round. Closing.",
    "Let's get the fuck out of here!",
    "We're getting juked! We're gonna die in here!",
    "Jesus... Jesus... I don't believe it.",
    "They must be like Gorman. Their signs are real low but they ain't dead!",
    "Oh, God. Jesus. This ain't happening.",
    "Look, man, let's just bug out and call it even, okay?",
    "Maybe you haven't been keeping up on current events, but we just got out asses kicked, pal!",
    "Well that's great! That's just fucking great, man. Now what the fuck are we supposed to do, man? We're in some real pretty shit now!",
    "Just tell me what the fuck we're supposed to do now. What're we gonna do now?",
    "Man, we're not going to make it seventeen hours! Those things are going to come in here, just like they did before, man... they're going to come in here and get us, man, long before...",
    "Aye-firmative. I'm on it.",
    "Yeah, right, it runs from the processing station right into the sublevel here.",
    "Hudson here. A and B sentries are in place and keyed. We're sealing the tunnel.",
    "They must be wall to wall in there. Look  at those ammo counters go. It's a shooting gallery down there.",
    "Oh, man. And I was gettin' short, too! Four more weeks and out. Now I'm gonna buy it on this fuckin' rock. It ain't half fair, man!",
    "Oh, right! Right! With those things running around. No way.",
    "Maybe we got 'em demoralized.",
    "I say we grease this rat-fuck son of a bitch right now!",
    "Fuuuck! He's dead. (to Burke) You're dogmeat, pal.",
    "What do you mean, they cut the power? How could they cut the power, man? They're animals.",
    "It's inside the complex.",
    "No. No! It ain't you. They're inside. Inside the perimeter. They're in here.",
    "This signal's weird...must be some interference or something. There's movement all over the place...",
    "Movement! Signal's clean. Range twenty meters... Seventeen meters..... fifteen meters...",
    "Twelve meters. Man, this is a big fucking signal. Ten meters.",
    "Let's go! Let's go!",
    "Hudson screams as floor panels lift under him, and clawed arms seize him lightning fast, dragging him down..."

]

abouttext = "I am Private First Class William L. Hudson. I respond to the words \"Alien\" or \"Aliens\"."

@client.event
async def on_ready():
    logging.info('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user.mentioned_in(message):
        print(message)
        if "@everyone" in message.content:
            logging.info("This was a call to everyone which I'll quietly ignore ...")
        else: 
            logging.info(abouttext)
            await message.channel.send(abouttext)

    if "hicks" in message.content.lower():
        quote = "Hudson, Sir. He's Hicks."
        logging.info(quote)
        await message.channel.send(quote)

    if "hudson" in message.content.lower():
        if message.author == client.user:
            return
        logging.info(abouttext)
        await message.channel.send(abouttext)

    if "alien" in message.content.lower():
        quote = random.choice(quotes)
        logging.info(quote)
        await message.channel.send(quote)

client.run(token)