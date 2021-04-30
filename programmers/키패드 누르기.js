function solution(numbers, hand) {
  var answer = '';
  
  function keypadInit() {
      const keypad = {};
      const keypadChar = [1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#'];
      let k = 0;
      for (let y=0; y<4; y++) {
          for (let x=0; x<3; x++) {
              const key = keypadChar[k];
              keypad[key] = [x, y];
              k++;
          }
      }
      return keypad;
  }
  
  const keypad = keypadInit();

  // x, y
  let leftHand = [0, 3];
  let rightHand = [2, 3];
  
  let numbersLength = numbers.length
  
  for (let i=0; i<numbersLength; i++) {
      let cur = numbers[i];
      let curdir = keypad[cur.toString()];
      
      if (cur == 1 || cur == 4 || cur == 7) {
          answer += 'L';
          leftHand = curdir;
      } else if (cur == 3 || cur == 6 || cur == 9) {
          answer += 'R';
          rightHand = curdir;
      } else {
          let [cx, cy] = curdir;
          let [lx, ly] = leftHand;
          let [rx, ry] = rightHand;
          
          const leftMove = Math.abs(cx - lx) + Math.abs(cy - ly);
          const rightMove = Math.abs(cx - rx) + Math.abs(cy - ry);
          
          if (leftMove > rightMove) {
              answer += 'R';
              rightHand = curdir;
          } else if (rightMove > leftMove) {
              answer += 'L';
              leftHand = curdir;
          } else {
              if (hand == 'right') {
                  answer += 'R';
                  rightHand = curdir;
              }
              else {
                  answer += 'L';
                  leftHand = curdir;
              }
          }
      }
  }
  
  return answer;
}