import imaplib
import re
import quopri
import slack
from datetime import datetime


class Newsletter:
    def __init__(self, email, password, slack_token, slack_channel, startline_from_top=4, endline_from_bottom=-5) -> None:
        self.host = 'imap.gmail.com'
        self.port = 993
        self.email = email
        self.password = password
        self.slack_token = slack_token
        self.slack_channel = slack_channel
        self.startline_from_top = startline_from_top
        self.endline_from_bottom = endline_from_bottom

    def check_email(self):
        server = imaplib.IMAP4_SSL(self.host, self.port)
        server.login(self.email, self.password)
        server.select()
        status, data = server.search(
            None, '(FROM "newsletter@filipedeschamps.com.br" UNSEEN)')

        return server, data

    def config_slack_client(self):
        client = slack.WebClient(token=self.slack_token)
        channel = self.slack_channel
        return client, channel

    def send_slack_blocks(self, blocks):
        client, channel = self.config_slack_client()
        client.chat_postMessage(channel=channel, blocks=blocks)

    def send_slack_text(self, text):
        client, channel = self.config_slack_client()
        client.chat_postMessage(channel=channel, text=text)

    def prepare_news(self):
        server, data = self.check_email()

        if data[0]:
            blocks = self.config_blocks(data, server)
            self.send_slack_blocks(blocks)

    def config_blocks(self, data, server):
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
        d = data[0].split()
        ind = d[-1]
        btext = server.fetch(
            ind, "(BODY[1] BODY[HEADER.FIELDS (SUBJECT FROM)])")
        email_msg = btext[1][1][1]

        utf = quopri.decodestring(email_msg)
        text = utf.decode('utf-8')
        text = re.sub(r'^https?:\/\/.*[\r\n]*',
                      '', text, flags=re.MULTILINE)
        text = text.replace('\r\n\r\n', '###').replace(
            '\r\n', ' ').replace('###', '\r\n\r\n')

        text_lines = text.splitlines()

        startline = 0
        if self.startline_from_top > 0:
            startline = self.startline_from_top

        endline = 0
        if self.endline_from_bottom < 0:
            endline = self.endline_from_bottom
        else:
            text_lines = text_lines[startline:]

        text_lines = text_lines[startline:endline]

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
        return blocks
