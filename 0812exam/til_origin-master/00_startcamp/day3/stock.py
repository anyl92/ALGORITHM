from iexfinance.stocks import Stock
import random

companies = ['AAPL', 'GOOGL', 'TSLA', 'FB', 'AMZN']
company = Stock(random.choice(companies), token='pk_34947d6f20564c52a9dcd62bf4d4ab5f')

print(company.get_quote())
