// Daily Challenge GOLD: Bubble Sort


const numbers = [5,0,9,1,7,4,2,6,3,8];

let strNum = numbers.toString();

let numJoinOne = numbers.join("+");
let numJoinTwo = numbers.join("");
let numJoinThree = numbers.join("*");


//for(let i=0; i< numbers.length; i++) {

let n = numbers.length;

for (let i = 0; i < n; i++) {
    for (let j = 0; j < n - i - 1; j++) {
        if (numbers[j] < numbers[j + 1]) {
          [numbers[j], numbers[j+1]] = [numbers[j+1],numbers[j]];
        }
    }
}
console.log(numbers);


