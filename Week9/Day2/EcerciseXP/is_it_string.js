// 🌟 Exercise 3 : Is It A String ?

let isString = (value) => {
  return typeof value === 'string';
};

console.log(isString('hello'));
console.log(isString([1,2,3]));
console.log(isString(1));
console.log(isString("123"));
