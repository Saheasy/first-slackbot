import os
import random
import requests
import re
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv
load_dotenv()

# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))
user = os.environ.get("SLACK_USER_TOKEN")


# My Dadjoke Slash Command
# Send a dadjoke via "icanhazdadjoke.com"'s api
@app.command("/dadjoke")
def dadjoke(ack, respond, payload):
  message = requests.get("https://icanhazdadjoke.com/",
                         headers={"Accept": "text/plain"}).text
  print(message)
  ack()
  respond(message)

@app.command("/duck")
def duck_command(ack, respond, payload):
  message = requests.get('https://random-d.uk/api/v2/random').json()
  blocks =  [
        {
    			"type": "section",
    			"text": {
    				"type": "mrkdown",
    				"text": ":duck: Here is a duck for you fine fellow :duck:"
    			}
    		},
		    {
    			"type": "image",
    			"image_url": message,
    			"alt_text": "An amazingly attractive picture of a duck"
    		}
    	]
  ack()
  respond(text="Here is a duck for you fine fellow", blocks=blocks)

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
            "type": "section",
            "text": {
              "type": "mrkdwn",
              "text": ":coffee: Someone mentioned coffee! :coffee:"
            }
          },
          {
            "type": "image",
            "title": {
              "type": "plain_text",
              "text": ":coffee:",
              "emoji": True
            },
            "image_url": requests.get('https://coffee.alexflipnote.dev/random.json').json()['file'],
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

@app.event("team_join")
def member_join(event, say):
  print("test")
  print(event.keys())
  
@app.event("app_home_opened")
def update_home_tab(client, event, logger):
    try:
        # Call views.publish with the built-in client
        client.views_publish(
            # Use the user ID associated with the event
            user_id=event["user"],
            # Home tabs must be enabled in your app configuration
            view={
                "type": "home",
                "blocks": [
                {
                  "type": "image",
                  "image_url": "https://picsum.photos/400/100",
                  "alt_text": "inspiration"
                },
                {
                  "type": "section",
                  "text": {
                    "type": "mrkdwn",
                    "text": "*Welcome to my Bot homepage, <@" + event['user'] + ">!*\nYou can access it's code at <https://bitbucket.pearson.com/users/usahusp/repos/spencer-sahu-slackbot/browse?at=refs%2Fheads%2Fdev | my BitBucket Repository>"
                  }
                }
              ]
            }
        )
    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")

# Start your app
if __name__ == "__main__":
  SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
