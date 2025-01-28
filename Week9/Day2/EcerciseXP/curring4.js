// Exercise 4 : Currying

const curriedSum = (a) => (b) => a + b;
const add5 = curriedSum(5);
console.log(add5(12));

/*
 curriedSum: This is a curried function that takes one argument a
 and returns another function that takes a second argument b.
 The inner function returns the sum of a and b.
 Therefore, the outcome of the last line, add5(12), will be 17.
*/
