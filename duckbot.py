import os
import random
import requests
import re
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

# My Dadjoke Slash Command
# Send a dadjoke via "icanhazdadjoke.com"'s api
@app.command("/dadjoke")
def dadjoke(ack, respond, payload):
  message = requests.get("https://icanhazdadjoke.com/",
                         headers={"Accept": "text/plain"}).text
  print(message)
  ack()
  respond(message)

# My xkcd Slash Command
# Using xkcd's url, can respond with a comic. 
# Either the day of, random, or respond with a direct comic
@app.command("/xkcd")
def xkcd(ack, say, payload):
  id_max = 2680
  message = ""
  if payload.get('text') == '': 
    message = requests.get("https://xkcd.com/info.0.json").json()

  # Uses the random library in python to generate a custom id to go to
  elif payload.get('text') == 'random':
    message = requests.get(f'https://xkcd.com/{random.randint(0,id_max)}/info.0.json').json()

  # Uses the slack input to fetch the comic of that id number
  elif re.fullmatch(r'[0-9]+', payload.get('text')) != None:
    value = int(payload.get('text').strip())
    if value < id_max + 1:
      message = requests.get(f'https://xkcd.com/{value}/info.0.json').json()
    else:
      say("wrong input, please try again")
  
  blocks =  [
        {
    			"type": "section",
    			"text": {
    				"type": "plain_text",
    				"text": f'{message["safe_title"]} | {message["month"]}/{message["day"]}/{message["year"]}'
    			}
    		},
		    {
    			"type": "image",
    			"image_url": message['img'],
    			"alt_text": message['alt']
    		}
    	]
  ack()
  say(text=f'{0} | {1}/{2}/{3}'.format(message['safe_title'], message['month'], message['day'],message['year']), blocks=blocks)


@app.message("coffee")
def message_hello(message, say):
  blocks = [
          {
            "type": "image",
            "image_url": "https://coffee.alexflipnote.dev/random",
            "alt_text": "some coffee"
          }
        ]
  # say() sends a message to the channel where the event was triggered
  say(text="have some coffee", blocks=blocks)
    #https://coffee.alexflipnote.dev/random


#Event loggers that record events that happen
#This leads to less errors in the terminal as well
@app.event("message")
def handle_message_events(body, logger):
  logger.info(body)

@app.event("pin_added")
def handle_pin_added_events(body, logger):
    logger.info(body)

@app.event("app_mention")
def handle_app_mention_events(body, logger):
  logger.info(body)

@app.event("link_shared")
def handle_link_shared_events(body, logger):
    logger.info(body)
  
@app.event("app_home_opened")
def app_home_open(event, say):
    say(f'Hello world, {event.user}!')

# Start your app
if __name__ == "__main__":
  SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
