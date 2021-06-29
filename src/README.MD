# Slack Bot com as notícias do Deschamps
Slack Bot que publica a Newsletter do Deschamps recebida no Gmail

## Instalação
```bash
pip install slackbot-newsletter-deschamps
```

## Cadastro Newsletter
Por questão de segurança, sugiro que crie um e-mail só pra receber a newsletter.
Configure seu e-mail com autenticação de 2 fatores e habilite o acesso por senha de aplicativo.
- https://support.google.com/accounts/answer/185833?hl=pt  

Faça seu cadastro na Newsletter: 
- https://newsletter.filipedeschamps.com.br/  

## Crie um bot de slack
- https://slack.com/intl/pt-br/help/articles/115005265703-Criar-um-bot-para-o-workspace  
- https://www.youtube.com/watch?v=KJ5bFv-IRFM

## Código de Exemplo
```bash
from newsletter import Newsletter

newsletter = Newsletter('email@email.com', 'password_do_email','token_slack','#canal_do_slack')
newsletter.prepare_news()

```
Se por alguma questão estética as primeiras e últimas linhas do texto convertido com as notícias precisarem ser removidas, vc pode configurar passando parametros, conforme exemplo:  
```bash
from newsletter import Newsletter

newsletter = Newsletter('email@email.com', 'password_do_email','token_slack','#canal_do_slack', 4, -5) # Neste exemplo as 4 primeras e as 5 ultimas linhas são removidas
newsletter.prepare_news()

```

## No Slack
- Para funcionar mencione o nome do bot usando @
- Convide o bot pra sala

## Automação
- Crie um Crontab no seu sistema operacional pra chamar o script 1 vez por dia

- **Exemplo pra Mac OS** (mas é bem fácil de achar no google pra outros sistemas):
    - https://www.jcchouinard.com/python-automation-with-cron-on-mac/

- No meu caso, configurei pra todos os dias da semana as 11:30
    - Modelo pra Crontab: [https://crontab.guru/#30_11_*_*_1-5](https://crontab.guru/#30_11_*_*_1-5)

## Inspiração pra ideia
- https://newsletter.filipedeschamps.com.br/  
- https://www.youtube.com/watch?v=wm82gDsKN0E
