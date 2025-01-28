//🌟 Exercise 5 : Star Wars

const epic = ['a', 'long', 'time', 'ago', 'in a', 'galaxy', 'far far', 'away'];

let reduceEpic = epic.reduce(epicFunction);

function epicFunction(total, value) {
  return `${total} ${value}`;
};

console.log(reduceEpic);
