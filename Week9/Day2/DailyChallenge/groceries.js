// Daily Challenge: Groceries


let client = "John";

const groceries = {
    fruits : ["pear", "apple", "banana"],
    vegetables: ["tomatoes", "cucumber", "salad"],
    totalPrice : "20$",
    other : {
        paid : true,
        meansOfPayment : ["cash", "creditCard"]
    }
}

let displayGroceries = item => {
  console.log(item);
}

groceries.fruits.forEach(displayGroceries);

let cloneGroceries = () => {
  let user = client;
  client = 'Betty';

  let shopping = groceries;
  groceries.totalPrice = "35$";
  groceries.other.paid = false;
  console.log(groceries, shopping);
};

cloneGroceries();
