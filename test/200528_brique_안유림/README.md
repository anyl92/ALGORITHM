### 1. “Form1”에서 “Form2”로 아래의 네트워크 메시지를 보내고, 메시지가 “Form2”에 나타날 수 있도록 해주세요. 

#### - React Client

`form1client/` 환경설정

```bash
npm install socket.io-client
npm start
```

`form1client/src/App.js`

```react
import socketio from 'socket.io-client';
const socket = socketio.connect('http://localhost:4000')

const send = () => {
    socket.emit('init', {
      data: 'hello'
    });
  }

return (
    <div className="App">
      <button onClick={send}>send</button>
    </div>
  );
```





#### - Node.js Express Server

`form2server/` 환경설정

```bash
npm install socketio -save
npm start
```

`form2server/src/app.js`

```javascript
var app = express();
app.io = require('socket.io')();

app.io.on('connection', function(socket) {
  socket.on('init', function(data) {
    console.log(data.data);
  });
});
```





### 2. 아래의 String 타입의 Input과 Output에 기초한 Calculation function을 개발해주세요. 

`form1client/src/App.js`

#### - String 수정

```react
const [isEdit, setIsEdit] = useState(false);
const [editString, setEditString] = useState('y = 20+((10*x)/( 100-x) )');

const handleInputStr = () => {
    setIsEdit(true);
}

const handleChange = (e) => {
    const newString = e.target.value
    setEditString(newString)
}

const handleBlur = () => {
    setIsEdit(false)
}
```

#### - X 값 입력 후 계산하여 Y에 표현

```react
const [inputX, setInputX] = useState(null);
const [result, setResult] = useState(null);

const handleX = (e) => {
    setInputX(e.target.value)
}

const calc = (e) => {
    let nString = ''
    nString = editString.replace(/=/gi, '').replace(/y/gi, '').replace(/ /gi, '').replace(/x/gi, inputX.toString())
    setResult(eval(nString))
}
```





### 3. 버튼 클릭에 따라 선의 두께가 변화하는 Function을 개발하여, 선형차트에 표시해주세요. 







### 4. 데이터 추출 Function을 개발하세요. 주어진 파일을 읽은 후, 아래에 언급된 output을 출력 하세요. 

`question4.py`

```bash
pip install virtualenv
pip install numpy
```

p0
min 0
max 99
avg 49.5081444
standard deviation 28.85497734652983
median 50.0

p1
min 0
max 99
avg 49.4964066
standard deviation 28.87494656423586
median 49.0

p2
min 0
max 99
avg 49.5052776
standard deviation 28.859715642170464
median 50.0

p3
min 0
max 99
avg 49.482849
standard deviation 28.871755302426596
median 49.0

p4
min 0
max 99
avg 49.5078754
standard deviation 28.86825915738729
median 50.0

p5
min 0
max 99
avg 49.5120452
standard deviation 28.846384947045898
median 50.0

p6
min 0
max 99
avg 49.5100042
standard deviation 28.876646555927888
median 50.0

p7
min 0
max 99
avg 49.5045994
standard deviation 28.871017890706938
median 50.0

p8
min 0
max 99
avg 49.5046768
standard deviation 28.857502693884342
median 50.0

p9
min 0
max 99
avg 49.5042022
standard deviation 28.866167849950486
median 50.0

total line 5000000
time 36.023725509643555