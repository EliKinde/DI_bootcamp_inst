// Exercise 3 : What’s In My Wallet ?
function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

let quarters = getRandomInt(0, 100) * 0.25;
let dimes = getRandomInt(0, 50) * 0.10;
let nickel = getRandomInt(0, 75) * 0.05;
let penny = getRandomInt(0, 25) * 0.01;

let itemPrice = Math.random() * (40 - 1 + 1);

let changeList = [quarters, dimes, nickel, penny];

function changeEnough(itemPrice, amountOfChange) {
  let sumChange = 0;
  for(let i=0; i < amountOfChange.length; i++) {
    sumChange += amountOfChange[i];
  }
  if(itemPrice > sumChange) {
    return false;
  }
  else {
    return true;
  }
}

let priceSum = changeEnough(itemPrice, changeList);

console.log(`the price items is ${itemPrice.toFixed(3)}\nand you buy it? ${priceSum}`);

