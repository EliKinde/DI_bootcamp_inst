// Exercise 1 : Nested Functions


let landscape = () => {

 let result = "";

 let flat = (x) => {
   for(let count = 0; count<x; count++){
     result = result + "_";
   }
 }

 let mountain = (x) => {
   result = result + "/"
   for(let counter = 0; counter<x; counter++){
     result = result + "'"
   }
   result = result + "\\"
 }

 flat(4);
 mountain(4);
 flat(4)

 return result;
}

console.log(landscape());

/*
1.Function Definition:
The function landscape is defined, which initializes an empty
string result.

2.Inner Functions:
flat: This function takes a parameter x and appends x
underscores (_) to result.

mountain: This function also takes a parameter x. It appends a /,
followed by x apostrophes ('), and then appends a \.

3.Function Execution:
flat(4): This will append 4 underscores to result, so now
result is "____".

mountain(4): This will append /, followed by 4 apostrophes ('),
and then \. Thus, result becomes "____/''''\'.

flat(4): This will append another 4 underscores, making result
now "____/''''\____".


*/
