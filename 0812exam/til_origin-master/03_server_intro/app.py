# 최고 중간 관리자.
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')  # Domain 뒤에 아무말이 없으면
def index():
    return render_template('index.html')


@app.route('/cube/<int:number>')
def cube(number):
    return f'{number} 의 3제곱은 {number**3} 입니다.'


@app.route('/dict/<string:word>')
def my_dict(word):
    d = {
        'apple': '사과',
        'banana': '바나나',
    }
    result = d.get(word)
    if result:
        return f'{word} => {result}'
    else:
        return f'{word} 는 없어ㅠ'

if __name__ == '__main__':
    app.run(debug=True)
