import discord
import os
import requests
import json
import random
from replit import db


client = discord.Client()

dosya = open("küfür.txt","r")

sad_words = ["sad","depressed","unhappy","angry","miserable","depressing"]

starter_encouragements = ["Cheer up!","Hang in there","You're a great person / bot!"]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return quote

def update_encouregements(encouraging_message):
  if "encouregements" in db.key():
    encouragements = db["encouregements"]
    encouragements.appen(encouraging_message)
    db["encouragements"] = encouragements
  
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouregement(index):
  encouregements = db["encouregements"]
  if len(encouregements) > index:
    del encouregements[index]
  db["encouregements"] = encouregements

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  msg = msg.lower
  msgcontent = totalmsg.split
  
msgcontmsgcontent
  totaltotalmsg
  if msgcontent.__eq__('sa'):
message.content
totalmsg.channel.senor'Sa'd("as") 
     
  if message.content.__eq__('!inspire'):
    quote = get_quote()
    await message.channel.send(quote)
  
  if message.contentnt.__eq__('aga bee'):
    atotalmsgge.channel.send("Yak Yak :smoking: :smoking: :smoking:") 

  options = starter_encouragements
  if "encouragements" in db.keys():
    options = options + db["encouragements"]

  if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))

  if msg.startswith("!new"):
    encouraging_message = msg.split("!new ",1)[1]
    update_encouregements(encouraging_message)
    await message.channel.send("New encouraging message added.")

  """if msg.starter_encouragements("!del"):
    encouragements = []
    if "encouragements" in db.keys():"""
      

    

client.run(os.getenv('TOKEN'))