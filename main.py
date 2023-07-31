import os
import schedule
import time
from slack_sdk import WebClient

#schedule.every(10).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)
#schedule.every().day.at("12:42", "Europe/Amsterdam").do(job)
#schedule.every().minute.at(":17").do(job)
# Schedule lib examples

SLACK_TOKEN = "endpoint/slack token"
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

schedule.every().monday.at("09:25").do(send_reminder)
schedule.every().tuesday.at("09:25").do(send_reminder)
schedule.every().wednesday.at("09:25").do(send_reminder)
schedule.every().thursday.at("09:25").do(send_reminder)
schedule.every().friday.at("09:25").do(send_reminder)


while True:
    schedule.run_pending()
    time.sleep(10000)
