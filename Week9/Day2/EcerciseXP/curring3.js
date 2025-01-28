// Exercise 3 : Currying

const curriedSum = (a) => (b) => a + b
curriedSum(30)(1)

/*
curriedSum: This is a curried function that takes one argument a
and returns another function that takes a second argument b.
The inner function returns the sum of a and b.
Therefore, the outcome of curriedSum(30)(1) will be 31.
*/
