let age = [20,5,12,43,98,55];
let sum = 0;

for(let i=0; i < age.length; i++) {
  sum += age[i];
}
console.log(`The sum of the ages is ${sum}`);

let height = age[0];

for(let i=0; i < age.length; i++) {
  if(age[i] > height) {
    height = age[i];
  }
}

console.log("Highest age:", height);

