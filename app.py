import imaplib
import re
import quopri
import pyttsx3
import slack
import os
from pathlib import Path
from dotenv import load_dotenv
import sched
import time
from datetime import datetime


def main():
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)
    scheduler_retry = sched.scheduler(time.time, time.sleep)
    scheduler_retry.enter(0, 1, prepare_news, (scheduler_retry,))
    scheduler_retry.run()


def check_email():
    host = 'imap.gmail.com'
    port = 993
    user = os.environ['USER']
    password = os.environ['PASSWORD']

    server = imaplib.IMAP4_SSL(host, port)
    server.login(user, password)
    server.select()
    status, data = server.search(
        None, '(FROM "newsletter@filipedeschamps.com.br" UNSEEN)')

    return server, data


def config_slack_client():
    client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
    channel = os.environ['SLACK_CHANNEL']
    return client, channel


def send_slack_blocks(blocks):
    client, channel = config_slack_client()
    client.chat_postMessage(channel=channel, blocks=blocks)


def send_slack_text(text):
    client, channel = config_slack_client()
    client.chat_postMessage(channel=channel, text=text)


def prepare_news(scheduler_retry):
    server, data = check_email()

    if data[0]:
        d = data[0].split()
        ind = d[-1]
        btext = server.fetch(
            ind, "(BODY[1] BODY[HEADER.FIELDS (SUBJECT FROM)])")
        email_msg = btext[1][1][1]

        utf = quopri.decodestring(email_msg)
        text = utf.decode('utf-8')
        text = re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)
        text = text.replace('\r\n\r\n', '###').replace(
            '\r\n', ' ').replace('###', '\r\n\r\n')

        text_lines = text.splitlines()
        text_lines = text_lines[4:-2]

        blocks = [
            {
                "type": "section",
                "text": {
                        "type": "mrkdwn",
                        "text": ":sunny: *Bom dia Fofuras!!!* :heart::heart::heart:\n Que tal aproveitar o almoço pra dar uma olhadinha no que tá rolando nas notícias do mundo da tecnologia?!"
                }
            },
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": ":newspaper:  Resumo diário das principais notícias de tecnologia  :newspaper:"
                }
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": "Fonte: Newsletter Deschamps"
                    }
                ]
            },
            {
                "type": "divider"
            }
        ]

        for line in text_lines:
            if line != '':
                index_end_title = line.find(':')
                line_list = list(line)
                line_list[index_end_title +
                          2] = line_list[index_end_title + 2].upper()
                line = ''.join(line_list)

                line = ':loud_sound: *' + line.replace(':', '*\n')
                news = {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": line
                    }
                }
                blocks.append(news)
                blocks.append({
                    "type": "divider"
                })
        send_slack_blocks(blocks)
    else:
        now = datetime.now()
        todayNoon = now.replace(hour=12, minute=00, second=0, microsecond=0)
        if now < todayNoon:
            scheduler_retry.enter(300, 1, prepare_news, (scheduler_retry,))
        else: 
            send_slack_text('Sem notícias publicadas pra hoje.')


if __name__ == '__main__':
    main()
