// 🌟 Exercise 5 : Kg And Grams

// function declaration
function KgToGrams(kilo) {
  return kilo * 1000;
};
console.log(KgToGrams(1));
console.log(KgToGrams(2.21));

// function expression
let kgToGrams = function(kilo) {
  return kilo * 1000;
};
console.log(kgToGrams(8));
console.log(kgToGrams(2.21));

// A function declaration defines a named function and is hoisted,
// while a function expression defines a function as part of an expression and is not hoisted.



let KgTOGrams = kilo => kilo * 1000;
console.log(KgTOGrams(9));
console.log(KgTOGrams(2.21));

