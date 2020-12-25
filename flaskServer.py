from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def default_get():
    return "Bot server is alive!"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    thread = Thread(target=run)
    thread.start()