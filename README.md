# Teste Técnico Crawler
## Requisitos:
1. Python ``` 3.10 ``` ou superior com ``` virtualenv ``` instalado
2. ``` Ubuntu 20.4 ``` ou ``` Windows 11 ``` (utilizando ``` WSL ```) ou ``` MacOS ```
3. ``` Docker ```
4. Conexão estável a internet



## Enunciado
O objetivo deste teste é realizar web scraping e extrair informações da página:

```https://www.compassft.com/indices/```.

Escreva uma aplicação em Python que seja capaz de extrair os dados da fonte mencionada e 
realizar as seguintes tarefas. Requisitos necessários:
 1. Extraia as informações dos 10 primeiros tickers da URL.
 2. Salve os dados em um DataFrame pandas, com as colunas Ticker, Data e Valor.
 3. Transforme a Data para o padrão ano/mês/dia

## Setup:
1. Rode ``` python3 -r requirements.txt ``` para instalar todas as dependências.
2. Rode ``` sudo docker run -p 8050:8050 scrapinghub/splash  ``` para subir a instância do Splash.
3. Vá ao diretório ``` Compassft/Compassft/spiders ```.
4. Rode ``` scrapy crawl Ticker ```.
5. Vá ao diretorio ``` data/output ``` e abra o arquivo ``` data.csv``` para ver o resultado.
