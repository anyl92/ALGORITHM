import React, { useState } from 'react';
import socketio from 'socket.io-client';
const socket = socketio.connect('http://localhost:4000')

function App() {

  const send = () => {
    socket.emit('init', {
      data: 'hello'
    });
  }

  // Q2
  const [isEdit, setIsEdit] = useState(false);
  const [editString, setEditString] = useState('y = 20+((10*x)/( 100-x) )');
  const [inputX, setInputX] = useState(null);
  const [result, setResult] = useState(null);

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
  
  const handleX = (e) => {
    setInputX(e.target.value)
  }
  
  const calc = (e) => {
    let nString = ''
    nString = editString.replace(/=/gi, '').replace(/y/gi, '').replace(/ /gi, '').replace(/x/gi, inputX.toString())
    setResult(eval(nString))
  }


  return (
    <div className="App">
      <button onClick={send}>send</button>

      {/* Q2 */}
      <p>String: {isEdit ? 
        <input type="text" value={editString} autoFocus onChange={handleChange}  onBlur={handleBlur}></input>
        : <span onClick={handleInputStr}>{editString}</span>}
      </p>
      <p>X: <input type="text" name="X" onChange={handleX}></input> <button onClick={calc}>계산</button></p>
      <p>Y: <span>{result}</span></p>
    </div>
  );
}

export default App;
