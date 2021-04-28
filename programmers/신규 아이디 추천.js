function solution(new_id) {
  var new_id_length = new_id.length;
  
  function changeLowerCase(new_id) {
      return new_id.toLowerCase();
  }
  
  function removeErrorChar(new_id, new_id_length) {
      let new_new_id = "";
      
      for (let i=0; i<new_id_length; i++) {
          let cur = new_id[i];
          
          if (cur == "-" || cur == "_" || cur == ".") {
              new_new_id += cur;
          } else if (cur >= 0 && cur < 10) {
              new_new_id += cur;
          } else if (cur.charCodeAt(0) >= 97 && cur.charCodeAt(0) < 123) {
              new_new_id += cur;
          }
      }
      
      return new_new_id;
  }
  
  function changeDotCount(new_id, new_id_length) {
      let new_new_id = "";
      
      let i = 0;
      while (i < new_id_length) {
          new_new_id += new_id[i]
          let j = 1;
          if (new_id[i] == ".") {
              while (i+j < new_id_length && new_id[i+j] == ".") {
                  j++;
              }
              i += j-1;
          }
          i++;
      }
      return new_new_id;
  }
  
  function removeDot(new_id, new_id_length) {
      if (new_id[0] == ".") {
          new_id = new_id.slice(1);
      } 
      new_id_length = new_id.length
      if (new_id[new_id_length-1] == ".") {
          new_id = new_id.slice(0, -1);
      }
      return new_id;
  }
  
  function checkEmpty(new_id, new_id_length) {
      if (new_id_length == 0) {
          return "a";
      }
      return new_id;
  }
  
  function cutString(new_id, new_id_length) {
      if (new_id_length > 15) {
          let tmp = new_id_length - 15;
          new_id = new_id.slice(0, -tmp);
          return removeDot(new_id, new_id.length);
          
      } else if (new_id_length <= 2) {
          let tmp = new_id[new_id_length-1];
          while (new_id.length != 3) {
              new_id += tmp;    
          }
      }
      return new_id
  }
  
  // 1
  new_id = changeLowerCase(new_id);
  new_id_length = new_id.length;
  
  // 2
  new_id = removeErrorChar(new_id, new_id_length);
  new_id_length = new_id.length;
  
  // 3
  new_id = changeDotCount(new_id, new_id_length);
  new_id_length = new_id.length;
  
  // 4
  new_id = removeDot(new_id, new_id_length);
  new_id_length = new_id.length;
  
  // 5
  new_id = checkEmpty(new_id, new_id_length);
  new_id_length = new_id.length;
  
  // 6, 7
  new_id = cutString(new_id, new_id_length)
  
  return new_id;
}