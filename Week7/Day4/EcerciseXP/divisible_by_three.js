//Exercise 1 : Divisible By Three

let numbers = [123, 8409, 100053, 333333333, 7]

for (let i = 0; i < numbers.length; i++) {
  if ((numbers[i] % 3) == 0) {
    console.log("True");
  } else {
    console.log("Flase");
  }
}
