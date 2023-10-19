import os
import schedule
import time
from slack_sdk import WebClient

SLACK_TOKEN = "slack token" # Here, you will need the token generated through the slack API
CHANNEL_ID = "id chanel"
people_list = ["@personname", "@personname", "@personname", "@personname", "@personname"] 
counter = 0

slack_client = WebClient(token=SLACK_TOKEN)
# token validation

text = "Hey, :eyes: :dart: It's your day in the daily apresentation!"

def send_reminder():
    global counter
   
    mentioned_person = people_list[counter]
    message = f"{text} {mentioned_person}"
    response = slack_client.chat_postMessage(
        channel=CHANNEL_ID, 
        text=message
    )

    if response["ok"]:
        print(f" Successfully reminder sent for {mentioned_person}")
    else:
        print(f" Reminder error {response['error']}")

    counter = (counter + 1) % len(people_list)
    # moving to the next person on the list, according to the day

schedule.every().monday.at("09:25").do(send_reminder)
schedule.every().tuesday.at("09:25").do(send_reminder)
schedule.every().wednesday.at("09:25").do(send_reminder)
schedule.every().thursday.at("09:25").do(send_reminder)
schedule.every().friday.at("09:25").do(send_reminder)
# days that reminder will be sent

while True:
    schedule.run_pending()
    time.sleep(10000)
