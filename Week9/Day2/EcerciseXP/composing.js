// Exercise 5 : Composing

const compose = (f, g) => (a) => f(g(a));
const add1 = (num) => num + 1;
const add5 = (num) => num + 5;
console.log(compose(add1, add5)(10));

/*
Function Definitions:

compose: This function takes two functions f and g as arguments and returns a new function that takes a parameter a. Inside, it calls g with a and then passes the result to f.
add1: This function takes a number and returns that number plus 1.
add5: This function takes a number and returns that number plus 5.
Execution of compose(add1, add5)(10):

When you call compose(add1, add5), you're creating a new function that will first execute add5 and then add1.
Now, when you call this new function with the argument 10:
First, add5(10) is executed, which returns 10 + 5 = 15.
Next, add1(15) is executed, which returns 15 + 1 = 16.
So, the final outcome of the last line, compose(add1, add5)(10), will be 16.

*/
￼



