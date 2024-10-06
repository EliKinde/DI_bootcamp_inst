// 🌟 Exercise 1 : List Of People

const people = ["Greg", "Mary", "Devon", "James"];
console.log(people);
people.shift();
console.log(people);
people[2] = "Jason";
people.push("Elihyu");
console.log("take a look at the Mary index: " + people.indexOf("Mary"));


let names = people.slice(1,people.length-1);
console.log(names);
people.indexOf("Foo");
// if the method returns -1, it indicates that the specified
// element is not found in the array.

let last = people[people.length - 1];
console.log(last);
console.log("*********\n");

for(let i = 0; i < people.length; i++) {
  console.log(people[i]);
}

for(let k = 0; k < people.length; k++) {
  if(people[k] == "Devon"){
    break;
  }
  console.log(people[k]);
}
