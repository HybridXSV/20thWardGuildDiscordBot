# import discord
# from discord.ext import commands, tasks
# from itertools import cycle
# from flask import Flask
# from threading import Thread

# # class flaskThread(Thread):
# #   def __init__(self, name, client, *args):

# app = Flask('__name__')

# @app.route('/')
# def hello_testing():
#   print("hello")
#   return "hello"


# def run():
#   app.run(host="0.0.0.0", port=8000)

# def keep_alive():
#   server = Thread(target=run)
#   server.start()

# bot = commands.Bot(command_prefix="py!")
# status = cycle(['with Python','JetHub'])

# # @bot.event
# # async def on_ready():
# #   change_status.start()
# #   print("Your bot is ready")

# # @tasks.loop(seconds=10)
# # async def change_status():
# #   await bot.change_presence(activity=discord.Game(next(status)))

# # if __name__ == "__main__":
# app.run(host='0.0.0.0', port=8080)