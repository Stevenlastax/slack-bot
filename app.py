import os
import slack
from slackeventsapi import SlackEventAdapter
import requests

SLACK_TOKEN = os.environ['SLACK_BOT_TOKEN']
SLACK_SIGNING_SECRET = os.environ['SLACK_SIGNING_SECRET']

client = slack.WebClient(token=SLACK_TOKEN)
slack_events_adapter = SlackEventAdapter(SLACK_SIGNING_SECRET, endpoint="/slack/events")

def send_message(message):
    response = client.chat_postMessage(channel='#sla-bot-testing', text=message)
    print(response["ok"])

@slack_events_adapter.on("reaction_added")
def reaction_added(event_data):
    emoji = event_data["event"]["reaction"]
    send_message(emoji)
    print(emoji)

@slack_events_adapter.on("app_mention")
def mention(event_data):
    mention_user = event_data["event"]["user"]
    send_message(f"Hey there <@{mention_user}>!")

# def main():
#     url = "http://www.forbes.com/forbesapi/thought/uri.json?enrich=true&query=1&relatedlimit=5"
#     response = requests.get(url)
#     data = response.json()
#     quote = data["thought"]["quote"]
#     send_message(quote)
#
# if __name__ == '__main__':
#     main()

slack_events_adapter.start(port=3000)