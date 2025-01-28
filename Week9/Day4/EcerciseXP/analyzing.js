// Exercise 3 : Analyzing


//------1------
const fruits = ["apple", "orange"];
const vegetables = ["carrot", "potato"];

const result = ['bread', ...vegetables, 'chicken', ...fruits];
console.log(result);

// The resulting array will combine the string 'bread',
// the elements of the vegetables array ('carrot', 'potato'),
// the string 'chicken', and the elements of the fruits array
// ('apple', 'orange').


//------2------
const country = "USA";
console.log([...country]);

// Each character of the string "USA" will be treated as a
// separate element in the new array.


//------Bonus------
let newArray = [...[,,]];
console.log(newArray);

// The array [[,,]] contains three empty slots. When you use the spread
// operator on an array with empty slots, it will create an array with
// no elements (i.e., it will not create undefined values).
// Thus, the resulting newArray will be an empty array.

