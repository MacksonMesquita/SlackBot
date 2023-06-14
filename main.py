import os
import schedule
import time
from slack_sdk import WebClient
# Imports necessários 

#schedule.every(10).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)
#schedule.every().day.at("12:42", "Europe/Amsterdam").do(job)
#schedule.every().minute.at(":17").do(job)
# Exemplos de como usar a biblíoteca Schedule

SLACK_TOKEN = "endpoint do app criado no Slack API"
CHANNEL_ID = "id do canal no slack, que o bot irá enviar a menssagem"
people_list = ["@nomepessoa", "@nomepessoa", "@nomepessoa", "@nomepessoa", "@nomepessoa"] 
counter = 0
# Configuração de token do chat slack, lista de pessoas responsáveis pelas apresentações e counter responsável por gerir a seleção 

slack_client = WebClient(token=SLACK_TOKEN)
# Setando o token para a validação do web client (fazendo o token pegar)

lembrete = "Hey, :eyes: :dart: Não esqueça que hoje é o seu dia de apresentação na daily!"
# Lembrete que o bot vai enviar

def send_reminder():
    global counter
   
    mentioned_person = people_list[counter]
    message = f"{lembrete} {mentioned_person}"
    response = slack_client.chat_postMessage(
        channel=CHANNEL_ID, 
        text=message
    )

    if response["ok"]:
        print(f"Lembrete enviado com sucesso para {mentioned_person}")
    else:
        print(f"Erro ao enviar lembrete para {response['error']}")
# Função criada para enviar os lembretes e validar o envio de menssagen

    counter = (counter + 1) % len(people_list)

schedule.every().monday.at("09:25").do(send_reminder)
schedule.every().tuesday.at("09:25").do(send_reminder
schedule.every().wednesday.at("09:25").do(send_reminder)
schedule.every().thursday.at("09:25").do(send_reminder)
schedule.every().friday.at("09:25").do(send_reminder)
# Utilizando a biblíoteca Schedule do python, setamos e agendamos os dias e a hora em que o lembrete será enviado 

while True:
    schedule.run_pending()
    time.sleep(1500)
# Dizemos a função o sleep time dela, e a configuramos com run pending (não parar de rodar, apos uma execussão)