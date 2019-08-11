import datetime

from art import *
from flask import Flask, render_template, request
from iexfinance.stocks import Stock

app = Flask(__name__)


@app.route('/art')
def art():
    return render_template('art.html')


@app.route('/result')
def result():
    input_text = request.args.get('input_text')
    font = request.args.get('font')
    result = text2art(input_text, font=font)
    
    return render_template('result.html', result=result)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send')
def send():
    return render_template('send.html')


@app.route('/receive', methods=['POST'])
def receive():
    data = request.form.get('msg')
    token = 'pk_63c229409ff14b67a6cc81e38927f1c4'
    stock = Stock(data, token=token).get_quote()
    company_name = stock['companyName']
    latest_price = stock['iexRealtimePrice']

    return render_template(
        'receive.html',
        c_name=company_name,
        l_price=latest_price
    )


@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    end_date = datetime.datetime(2019, 11, 29)
    left = end_date - today
    return render_template('dday.html', left_days=left.days)


@app.route('/boxoffice')
def boxoffice():
    top_5 = [
        '스파이더맨 파 프롬 홈',
        '알라딘',
        '토이스토리4',
        '존윅3',
        '라이온킹'
    ]
    return render_template('boxoffice.html', movies=top_5)


if __name__ == '__main__':
    app.run(debug=True)
