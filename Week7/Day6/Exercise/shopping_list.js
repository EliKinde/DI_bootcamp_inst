// 🌟 Exercise 2 : Shopping List

const stock = {
    "banana": 6,
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}

const prices = {
    "banana": 4,
    "apple": 2,
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
}

let shoppinglist = ['banana', 'orange', 'apple'];

function myBill() {
  for(let i=0; i < shoppinglist.length; i++) {
    let nameOffr = '';
    if(shoppinglist[i] in stock) {
      nameof = shoppinglist[i];
      console.log(`the stock of ${shoppinglist[i]} is ${stock[nameof]}`);
      console.log(`the price of the ${shoppinglist[i]} is ${prices[nameof]}`);
    }
  }
}

myBill();

