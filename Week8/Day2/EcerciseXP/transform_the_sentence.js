// 🌟 Exercise 3 : Transform The Sentence

let allBoldItems;
function getBoldItems() {
  allBoldItems = document.querySelectorAll("strong");
}

getBoldItems();

function highLight() {
  for(let i=0; i < allBoldItems.length; i++) {
    allBoldItems[i].style.color = "blue";
  }
}

function returnItemsToDefault() {
  for(let i=0; i < allBoldItems.length; i++) {
    allBoldItems[i].style.color = "black";
  }
}

document.querySelector("p").onmouseover = function(){highLight()};
document.querySelector("p").onmouseout = function(){returnItemsToDefault()};
