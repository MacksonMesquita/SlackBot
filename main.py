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

SLACK_TOKEN = "endpoint do app criado no Slack API"
CHANNEL_ID = "id do canal no slack, que o bot irá enviar a menssagem"
people_list = ["@nomepessoa", "@nomepessoa", "@nomepessoa", "@nomepessoa", "@nomepessoa"] 
counter = 0
# Slack token configuration, and people list to make something

slack_client = WebClient(token=SLACK_TOKEN)
# token validation

text = "Hey, :eyes: :dart: Não esqueça que hoje é o seu dia de apresentação na daily!"
# scheduler menssage 

def send_reminder():
    global counter
   
    mentioned_person = people_list[counter]
    message = f"{text} {mentioned_person}"
    response = slack_client.chat_postMessage(
        channel=CHANNEL_ID, 
        text=message
    )

    if response["ok"]:
        print(f"Lembrete enviado com sucesso para {mentioned_person}")
    else:
        print(f"Erro ao enviar lembrete para {response['error']}")

    counter = (counter + 1) % len(people_list)

schedule.every().monday.at("09:25").do(send_reminder)
schedule.every().tuesday.at("09:25").do(send_reminder
schedule.every().wednesday.at("09:25").do(send_reminder)
schedule.every().thursday.at("09:25").do(send_reminder)
schedule.every().friday.at("09:25").do(send_reminder)
# message scheduling

while True:
    schedule.run_pending()
    time.sleep(10000)
