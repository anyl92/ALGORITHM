import requests
import bs4

url = 'https://finance.naver.com/marketindex/'

response = requests.get(url)
text = bs4.BeautifulSoup(response, 'html.parser')

exchange_rate = text.select_one('#exchangeList > li.on > a.head.usd > div > span.value')

print(exchange_rate.text)
