import os
import discord
import asyncio
import emoji


from dotenv import load_dotenv
from googletrans import Translator
from threading import Thread

# TO DO:
# 1. Make bots detect themselves using group roles
# 2. Figure out why get_channel() doesn't work
# 3. Figure out why client.send() doesn't persist

load_dotenv()
TOKEN = os.getenv('AutoTranslatorBotToken')
client = discord.Client()

botName = '20th Ward Translator'
channelName = 'bot-testing'

botNames = ['20th Ward Translator', 'Smoogle Translate']






def translate(message):
    translator = Translator()
    detector = translator.detect(message)
    default = 'Either your spelling was terrible or this language is not supported.'

    if detector.lang == 'en':
        return translator.translate(message, dest='fr', src='en').text
    elif detector.lang == 'fr':
        return translator.translate(message, dest='en', src='fr').text
    elif detector.confidence.strip() == "None":
        return default
    else:
        return default


def isBotName(name):
  for botName in botNames:
    if name == botName:
      return True

  return False


def message_is_emoji(message):
  if len(message) == 1:
    return message in emoji.UNICODE_EMOJI
  else:
    return False

@client.event
async def on_message(message):
    current_channel = message.channel.name


    if current_channel == channelName and not isBotName(message.author.name):
        for channel in client.get_all_channels():
            if channel.name == 'bot-testing': 
              if message.content != "" and not message_is_emoji(message.content):
                responseMessage = message.author.name + ': ' + translate(message.content)
                await channel.send(responseMessage)

@client.event
async def on_ready():
    print(f'{client.user} is connected to the server.')


if __name__ == "__main__":
  loop = asyncio.get_event_loop()
  loop.create_task(client.start(TOKEN))
  Thread(target=loop.run_forever())