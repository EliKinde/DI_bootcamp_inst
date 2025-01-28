// Exercise 2 : Closure

const addTo = x => y => x + y;
const addToTen = addTo(10);
addToTen(3);

/*
 *addTo: This is a curried function that takes one argument x and
 returns another function that takes a second argument y.
 The inner function returns the sum of x and y.
Therefore, the outcome of addToTen(3) will be 13.
*/
