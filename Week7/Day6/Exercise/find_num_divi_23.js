// 🌟 Exercise 1 : Find The Numbers Divisible By 23

let numList = [];

function displayNumbersDivisible() {
  let j = 0;
  for(let i=0; i < 500; i++){
    if(i%23 == 0) {
      numList.push(i);
      j++;
    }
  }
}

displayNumbersDivisible();
console.log(`Outcome: ${numList}`);

function sumOfNum() {
  let sum = 0;
  for(let i of  numList) {
    sum += i;
  }
  console.log(`Sum: ${sum}`);
}

sumOfNum();
