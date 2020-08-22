const $keyword = document.querySelector(".keyword");
const $keywords = document.querySelector(".keywords");
const $searchResults = document.querySelector(".search-results");
const recommendBox = document.querySelector(".recommend-box");

const recommendView = document.querySelector(".recommend-view");
const recommendLoading = document.querySelector(".recommend-loading");
const searchLoading = document.querySelector(".search-loading");

const SHOWING = "showing", NOSHOWING = "noshowing", PAINT = "paint-item";

let liSelected = null;  //
let checkSelected = "";  // 

function getImage(val) { 
  searchLoading.classList.remove(NOSHOWING);
  searchLoading.classList.add(SHOWING);
  fetch(
    `https://jf3iw5iguk.execute-api.ap-northeast-2.amazonaws.com/dev/api/cats/search?q=${val}`
  )
    .then((res) => res.json())
    .then((results) => {
      searchLoading.classList.remove(SHOWING);
      searchLoading.classList.add(NOSHOWING);

      if (results.data) {
        $searchResults.innerHTML = results.data
          .map((cat) => `<article><img src="${cat.url}" /></article>`)
          .join("");
      }
    }).catch((err) => {
      alert("검색 중 에러 발생")
    });
}

function getData(val) {
  while (recommendBox.firstChild) {
    recommendBox.removeChild(recommendBox.firstChild);
  }
  if (!val) { return; }
  recommendLoading.classList.remove(NOSHOWING);
  recommendLoading.classList.add(SHOWING);
  fetch(`https://jf3iw5iguk.execute-api.ap-northeast-2.amazonaws.com/dev/api/cats/keywords?q=${val}`)
  .then((res) => res.json())
  .then((results) => {
    recommendLoading.classList.remove(SHOWING);
    recommendLoading.classList.add(NOSHOWING);
    let searchList = [];
    searchList = results;

    searchList.forEach(element => {
      const li = document.createElement("li");
      li.addEventListener("click", selectItem)
      li.innerText = element;
      recommendBox.appendChild(li);
    });
  }).catch((err) => {})
}

function selectItem(e) {  // Item 선택 시 input.value로
  checkSelected = "";
  $keyword.value = e.target.innerText
  getData($keyword.value)
  getImage($keyword.value)
  recommendBox.classList.remove(SHOWING);
  recommendBox.classList.add(NOSHOWING);
}

$keyword.addEventListener("focus", (e) => {  // focus 시 ul 보이게
  recommendBox.classList.remove(NOSHOWING);
  recommendBox.classList.add(SHOWING);
})

recommendView.addEventListener("blur", (e) => {
  recommendBox.classList.remove(SHOWING);
  recommendBox.classList.add(NOSHOWING);
})


$keyword.addEventListener("keyup", (e) => {  // 한 글자 입력마다 getData로 api받아오기
  const { key } = e;
  let val = e.target.value;
  
  let li = document.querySelector("li");
  // 키보드 화살표 누를 때
  if (key === "ArrowDown") {
    if (liSelected) {
      liSelected.classList.remove(PAINT)
      next = liSelected.nextSibling;
      next.classList.add(PAINT)
      checkSelected = next.innerHTML;
      liSelected = next;
    } else {
      li.classList.add(PAINT)
      checkSelected = li.innerHTML;
      liSelected = li;
    }
  } else if (key === "ArrowUp") {
    if (liSelected) {
      liSelected.classList.remove(PAINT)
      pre = liSelected.previousSibling;
      pre.classList.add(PAINT)
      checkSelected = pre.innerHTML;
      liSelected = pre;
    } else {
      li.classList.add(PAINT)
      checkSelected = li.innerHTML;
      liSelected = li;
    }
  } else { // 그 외 키 입력 시
    liSelected = null;
    recommendBox.classList.remove(SHOWING);
    recommendBox.classList.add(NOSHOWING);
    if (key === "Enter") {
      if (checkSelected) {
        $keyword.value = checkSelected;
        val = checkSelected;
      }
      getImage(val)
    } else if (e.key === "Escape") {
      recommendBox.classList.remove(SHOWING);
      recommendBox.classList.add(NOSHOWING);
    } else {  // 일반 문자 입력 시
      recommendBox.classList.remove(NOSHOWING);
      recommendBox.classList.add(SHOWING);
      getData(val)
    }
  }
})