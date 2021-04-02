# Slack Bot com as notícias do Deschamps
Slack Bot que publica a Newsletter do Deschamps recebida no Gmail

## Virtualização
- Utilize o PIPENV pra gerenciar as dependencias  
    - https://medium.com/@wilfilho/porque-os-desenvolvedores-python-devem-usar-o-pipenv-ae3d3154c44

## Crie um bot de slack
- https://slack.com/intl/pt-br/help/articles/115005265703-Criar-um-bot-para-o-workspace  
- https://www.youtube.com/watch?v=KJ5bFv-IRFM

## Credenciais e tokens
- Renomeie o arquivo .env.example para .env
- Insira as credenciais do slack e acesso ao email no arquivo .env

## No Slack
- Para funcionar mencione o nome do bot usando @
- Convide o bot pra sala

## Automação
- Crie um Crontab no seu sistema operacional pra chamar o script 1 vez por dia

- **Exemplo pra Mac OS** (mas é bem fácil de achar no google pra outros sistemas):
    - https://www.jcchouinard.com/python-automation-with-cron-on-mac/

- No meu caso, configurei pra todos os dias da semana as 11:00
    - Modelo pra Crontab: [https://crontab.guru/#0_11_*_*_1-5](https://crontab.guru/#0_11_*_*_1-5)

## Inspiração pra ideia
- https://newsletter.filipedeschamps.com.br/  
- https://www.youtube.com/watch?v=wm82gDsKN0E
